import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def load(transformed_data):

    mysql_host = os.getenv("MYSQL_HOST")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    mysql_db_name = os.getenv("MYSQL_DB_NAME")
    mysql_table = os.getenv("MYSQL_TABLE")


    config = {
        "host": mysql_host,
        "user": mysql_user,
        "password": mysql_password
    }

    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {mysql_db_name}")
    cursor.execute(f"USE {mysql_db_name}")
    cursor.execute(f"DROP TABLE IF EXISTS {mysql_table}")
    cursor.execute(f"""            
        CREATE TABLE IF NOT EXISTS {mysql_table}(
            id INT AUTO_INCREMENT PRIMARY KEY,
            city VARCHAR(50),
            country VARCHAR(50),
            latitude DECIMAL(10,4),
            longitude DECIMAL(10,4),
            weather VARCHAR(50),
            weather_description VARCHAR(50),
            weather_icon VARCHAR(255),
            temperature DECIMAL(10,4),
            temperature_feels_like DECIMAL(10,4),
            temperature_min DECIMAL(10,4),
            temperature_max DECIMAL(10,4)    
        ) """
    )
    values = [(d["city"], d["country"], d["latitude"], d["longitude"], d["weather"], d["weather_description"], d["weather_icon"], d["temperature"], d["temperature_feels_like"], d["temperature_min"], d["temperature_max"]) for d in transformed_data]
    cursor.executemany(f"INSERT INTO {mysql_table} (city, country, latitude, longitude, weather, weather_description, weather_icon, temperature, temperature_feels_like, temperature_min, temperature_max) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)
    con.commit()
    cursor.close()
    con.close()
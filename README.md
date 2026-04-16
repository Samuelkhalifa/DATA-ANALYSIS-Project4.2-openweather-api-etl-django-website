Project in the context of ETL Data Analysis self-learning

<br>

## &#128295; Used tools
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-5BC0EB?style=for-the-badge)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-000000?style=for-the-badge&logo=gnubash&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<br>

## [Subject : Display Django website serving openweather-API's data]

<br>

## &#x1F4DD; Project graph

<br>

<p align="center";>
  <img width="934" height="178" alt="Capture d’écran 2026-04-16 à 10 37 20" 
  src="https://github.com/user-attachments/assets/7a51ae98-5569-448b-a222-505a2862987e" />
</p>

<br>

## &#127919; Project steps
* Retrieve and transform data from the openweather API with `Python`.
* Import cleaned data into `csv` file.
* Display results on a website page using `html`, `CSS` and `Django` framework. 

<br>

## &#128640; Project setup and activation

<br>

`Git clone` the project and get inside, to project root.
  ```bash
  git clone <repository-url> openweather-api-elt-django-website
  cd openweather-api-elt-django-website
  ```
<br>

Write into a `env.` file your personal API key.
  ```bash
  touch .env # (for Mac)
  ```
  ```dotenv
  API_KEY=""
  ```

<br>

Run the following script `init.sh`, which will activate Django server by getting into backend and running the command `python manage.py runserver`.
  ```bash
  chmod +x init.sh # (make the shell script executable)
  ./init.sh
  ```
<br>

Go to `localhost:8000` to use the website dashboard.





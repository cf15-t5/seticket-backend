
# Se Ticket

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

[![Flask](https://img.shields.io/badge/Next.js-13-green.svg)](https://flask.palletsprojects.com/en/)

[![Mysql](https://img.shields.io/badge/MongoDB-lastest-green.svg)](https://www.mysql.com/)

[![SQLAlchemy](https://img.shields.io/badge/Prisma-lastest-green.svg)](https://www.SQLAlchemy.io/)

## How to Install and Run the Project
To install and run the SeTicket project locally, please follow these steps:

 1.Clone the repository from GitHub:    
```bash
  git clone https://github.com/cf15-t5/seticket-backend.git
```

Navigate to the project directory:
```bash
  cd seticket-backend
```
craete venv and activate venv
```bash
    python3 -m venv venv  # on Windows, use "python -m venv venv" instead
    . venv/bin/activate   # on Windows, use "venv\Scripts\activate" instead
```

Install the project dependencies using a package manager such as pip:
```bash
    pip install -r requirement.txt
```

Copy example environment file to new file
```bash
  cp .env.example .env
```
Configure .env 

To run this project, you will need to add the following environment variables to your .env file

`DATABASE_URL`
`BASE_URL`
`DEBUG`
`PORT`
`JWT_ACCESS_TOKEN_EXPIRES`
`JWT_ACCESS_TOKEN_SECRET`
`JWT_ACCESS_TOKEN_ALGORITHM`
`PORT`
`MAIL_SERVER`
`MAIL_PORT`
`MAIL_USERNAME`
`MAIL_PASSWORD`
`MAIL_USE_TLS`
`MAIL_USE_SSL`

for setup the email service, you must configure email and app password in .env, for get the  app password you can stup 2fa first in your email and inside 2fa on bottom you get the app password

export FLASK_APP on windows
```bash
    set FLASK_APP=main.py
```
or on (mac/linux)
```bash
    export FLASK_APP=main.py
```
run the migration 
```bash
   flask db upgrade
```
Run the development server.
```bash
  flask run
```
or 
```bash
  flask --app=main.py run
```
Access the website locally at http://localhost:5000.

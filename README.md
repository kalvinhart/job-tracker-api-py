# Job Tracker Back End API

This project is a custom back end for a [job tracking application](https://github.com/kalvinhart/job-tracker) with a React front end.

It is built in Python using the Flask framework.

Authentication is handled with JSON Web Tokens.

It is deployed with AWS using Elastic Beanstalk as well as a PostgreSQL database deployed with AWS RDS.

## Running Locally

#### Prerequisites

- Python 3

#### 1. Clone the repo and create a virtual environment

On Windows:

```bash
git clone
py -m venv venv
venv\Scripts\activate
```

On Mac:

```bash
git clone
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create a .ENV file in the root folder

This should include the following variables:

- `SECRET_KEY` - a secret string used by the JWT package when creating access tokens.
- `DATABASE_URL` - a string containing the URL to your production database. If this is not present then a local Sqlite database is used.

#### 4. Create your first database migrations

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

#### 5. Run the application

```bash
flask --debug run
```

## Features

- User registration and sign in.
- Create, read, update and delete jobs.

## Technologies/Packages

The packages used in creating this application are:

- python 3
- python-dotenv
- flask
- flask-sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy
- pyjwt

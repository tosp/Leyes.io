# leyes
How to use the template

## System Requirements

* [Python 3.5](https://www.python.org/downloads/)
* [PostgreSQL 9.5+](https://wiki.postgresql.org/wiki/Detailed_installation_guides)
* [Node 4+](https://docs.npmjs.com/getting-started/installing-node)

## Database Setup

After downloading (https://www.postgresql.org/download/) and installing PostgreSQL, you should be able to switch to the postgres user on your system and start a session in the postgresql interpreter.

```bash
$ su postgres

$ psql
```

Next, we will create a database and an admin user for our project. Later on we will use this information to setup the database on our project and to activate it through our virtual environments.
```sql
CREATE DATABASE project_name_db;
CREATE ROLE project_db_admin WITH LOGIN PASSWORD 'db_admin_password';
GRANT ALL PRIVILEGES ON DATABASE project_name_db TO project_db_admin;
ALTER USER project_db_admin CREATEDB;
```


## Virtual Environments

You will need to create a virtual environment in order to isolate all the packages that are required for the project. We provide instructions on how to do it with [`virtualenv`](https://virtualenv.pypa.io/en/stable/)

First find the path to your `python 3.5` installation by running

```bash
$ which python3.5
PATH TO PYTHON 3.5
```

Then create the virtual environment like this. (We use different virtualenvironments for different functions, such as testing, development, production, and CI, each of them has different requirements, you should at least create an environment for development and one for testing.)
```bash
$ virtualenv --python='PATH TO PYTHON 3.5' /path/to/your/venv/NAME_OF_YOUR_ENV
```

We use environment variables to separate sensitive information and keys from the code, you should set the following ones.

```bash
DJANGO_SETTINGS_MODULE='leyes.settings.development' // The last part depends on the environment you are on
SECRET_KEY='Generate one here. (http://www.miniwebtool.com/django-secret-key-generator/)'
DB_NAME='project_name_db' // From Database Setup
DB_USER='project_user_admin'
DB_PASSWORD='db_admin_password'
DB_HOST='you.rho.stn.ame' // For local development 127.0.0.1 or localhost
DB_PORT=''
```

The template also uses python-social-auth, in order to allow users to log in with Facebook, and Google. You will need to get your app key from them, and then set the following environment variables.

```
GOOGLE_KEY
GOOGLE_SECRET
FACEBOOK_KEY
FACEBOOK_SECRET
```

In order to set them in your virtualenv just go to `/path/to/your/venv/NAME_OF_YOUR_ENV/bin/activate` and in the section for deactivate add at the end

```bash
unset NAME_OF_ENV_VAR
```
And set the variable at the end of the file like this

```bash
export NAME_OF_ENV_VAR='VALUE OF VAR'
```

After you are finished you can activate your virtual environment by running
```bash
$ source /path/to/your/venv/NAME_OF_YOUR_ENV/bin/activate
```

And deactivate it just by running this command on the terminal
```bash
$ deactivate
```

## Installing the Project Requirements

You will need to install different packages depending on the environment you are working on. For example if you are setting up the `development` environment you will need to run

```bash
$ pip install -r requirements/development.txt
```
Then install the npm required with
```bash
$ npm install
```
## Running the namechanger

```bash
$ python nameChanger.py project_name
```

## Running the project

Once you have finished the setup, you can run the project.

```bash
Run the migrations
$ python manage.py migrate
Start the development server
$ python manage.py runserver
```
After this you can go to your browser and go to http://localhost:8000, and you should be able to see the project running.

# Thank you!!!

All your contributions are highly appreciated. You are awesome and we hope you have a great day.
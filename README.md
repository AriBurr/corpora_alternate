------ Setting up the virtual environment ------

1) Install python3 via home brew if still using python2 (check python --version, should be 3.7.2)
$ brew install python

2) Install virtualenv
$ pip3 install virtualenv

4) Make a note of the full file path to the version of Python you just installed:
$ which python3
ex. output:
/usr/local/bin/python3

5) Create a virtual environment:
$ virtualenv -p /usr/local/bin/python3 [my_project_name]

6) Clone project and navigate to backend folder:
$ cd corpora/backend

7) To activate the new virtual environment, run the following:
$ source [my_project_name]/bin/activate

8) Active virtual environment and install dependencies:
$ pip3 install -r requirements.txt

9) You can deactivate it by running the following:
$ deactivate

------ Setting up the database ------

10) Make sure you have Postgres installed:
$ postgres --version
ex. output:
postgres (PostgreSQL) 11.2

11) Activate psql CLI:
$ psql postgres

12) Create a user (to view current databases and users active on your computer -- type \l -- you may skip this step and use one of these users instead)
$ CREATE USER sample_user WITH PASSWORD 'sample_password';

13) Create database:
$ CREATE DATABASE sample_database WITH OWNER sample_user;

------ Configuring the database and running the Django sever ------

14) Navigate to backend/corpora/corpora, and in the same folder as settings.py create .env file, fill out the following template with the database information you just created:

DB_NAME=" "
DB_USER='" "
DB_PASSWORD=" "   
DB_HOST=" "
DB_PORT='" "
SECRET_KEY="ARANDOMSECRETKEY"

15) cd .. and in the same folder as manage.py run:
$ python3 manage.py makemigrations
then run:
$ python3 manage.py migrate

16) To start backend server, run python3 manage.py runserver

------ Setting up the client server ------

17) From root directory, navigate to frontend and run yarn

18) To start client server, run yarn serve 




# [Pitch Perfect](https://pitchperfectly.herokuapp.com/)
## This app allow the a user to login a view pitch of various add a catergory and a pitch in an a exsisting catergory. 
### SEP 07th, 2018
#### By **[Ian Odhiambo](https://github.com/ianodad)**

## Description
After a user has singed in the user can take a chance to do the various tasks

    1. View Pitches based on category
    2. View all Pitches
    3. Create a new category
    4. Add a pitch to a category
    5. Comment on a pitch 
    6. Like or dislike a pitch
    

## Specifications
Get the specs [here](https://github.com/Ianodad/Pitch-Perfect.git)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software
	

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
 *pip install python3.6
 *pip install flask
 *pip install flask-SQLAlchemy
 *pip install Flask-Bootstrap4==4.0.2
 *pip install flask-script
 *pip install flask-wtf
 *pip install flask-migrate
 *pip install flask-login
 *pip install Flask-Mail
 *pip install flask-uploads

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitch'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
SQLAlchemy errors, automatic sign out has a short time span

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on developer.ianodad@gmail.com for any comments, reviews or advice.

### License
This project is licensed under the MIT Open Source license, (c) Ian Odhimabo

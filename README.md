# homeboard
A web app for roommates to organize rent/expenses, track to-dos, and communicate via a common chat space.
This is the back-end server. See https://github.com/birkholz/homeboard_frontend/ for the front-end.

## Development
Set up virtualenv
```
pip install -r requirements.txt
python manage.py syncdb
```
Run local server
```
python manage.py runserver
```
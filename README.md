# portfolio-performance

##setup (i think this should work)
1. git clone https://github.com/shwetareddy/portfolio-performance
2. cd (folder name)
3. virtualenv .venv
4. source .venv/bin/activate
5. pip install requitements.txt
6. python manage.py runserver


## Migrate db
1. python manage.py makemigrations (app name)
2. python manage.py sqlmigrate (app name) (migration number)
3. python manage.py migrate
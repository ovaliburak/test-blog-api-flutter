*Install*
docker, 
docker-compose,  
python3

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d --build
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser #Enter user information
python manage.py runserver #8000 Port
```
```
Go to URL
127.0.0.1:8000/api/docs/
```

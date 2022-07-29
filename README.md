# Price-Alert-Application (Django + Redis + SQLite)

# To run
- install redis from :- https://github.com/tporadowski/redis/releases
- open ‪C:\Program Files\Redis\redis-cli.exe
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver 


### POST Methods:
- http://127.0.0.1:5000/users/create : Body={"user_name":"nikhil","email":"employee@gmail.com"}
- http://127.0.0.1:8000/users/Login : Body={"user_name":"nikhil"}
- http://127.0.0.1:8000/alerts/create : Body={"alert_name": "Fifth Alert","alert_crypto_currency": "Bitcoin","alert_price": "23829"}

### GET Methods:
- http://127.0.0.1:5000/alerts
- http://127.0.0.1:8000/alerts/status/triggered
- http://127.0.0.1:8000/alerts/status/deleted
- http://127.0.0.1:8000/alerts/status/created
- http://127.0.0.1:8000/alerts/check - triggers alert and sends mail

### PATCH Methods:
- http://127.0.0.1:8000/alerts/delete<id<id>>

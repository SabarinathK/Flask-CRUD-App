# CRUD Flask application 

NOTE :
- Frontend      : Bootstrap
- Database      :  Sqlite
- Extension     :  Flask-SQLAlchemy

FILES: 
 - templates - for frontend
 - app.py   - for flask
 - models.py - for database 
 - database.db- is sqlite database (serverless)


----------------

Step 1:

Download this repo and

create a virtual Environment (env) fro windows 👇

```
python -m venv env

```

Step 2 :

Activate the virtual environment 


```
cd env/Scripts
```

```
actiavte
```

Install required all libraries from requirements.txt


```
pip install -r requirements.txt

```


Step 3:
Create your serveless database (sqlite)

```
python

```

```
from models.py import db
db.create_all()
exit()

```

It will create a database.db file


Step 4:
Run your flask app 


```
python app.py

```

Then follow your local port http://127.0.0.1:5000 
 
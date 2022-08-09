from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "super secret key"
db = SQLAlchemy(app)


class BLOG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)

    def __init__(self, company_name, email, phone_number, address):
        self.company_name = company_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

from flask_sqlalchemy import SQLAlchemy
from faker import Faker

db = SQLAlchemy()
fake = Faker()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

def generate_random_data():
    for _ in range(10):
        user = User(username=fake.user_name(), password=fake.password())
        db.session.add(user)
    
    for _ in range(10):
        product = Product(name=fake.word(), description=fake.text(), price=fake.random_number(digits=2))
        db.session.add(product)
    
    for _ in range(10):
        contact = Contact(name=fake.name(), email=fake.email(), message=fake.text())
        db.session.add(contact)
    
    db.session.commit()


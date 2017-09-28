from db import db

def init():
    db.create_all()
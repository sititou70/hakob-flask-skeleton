from flask import Flask
from app import app
from db import db

@app.route('/')
def show_all():
    return "hello flask!!"

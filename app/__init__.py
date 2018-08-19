from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)
from app import routes
from config import Config

app.config.from_object(Config)

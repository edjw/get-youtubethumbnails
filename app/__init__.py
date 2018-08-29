from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
csp = {
    "default-src": "'self'",
    "style-src": ["'self'", "stackpath.bootstrapcdn.com"],
    "img-src": ["'self'", "img.youtube.com"],
}

Talisman(app, referrer_policy="same-origin", content_security_policy=csp)

from app import routes
from config import Config

app.config.from_object(Config)

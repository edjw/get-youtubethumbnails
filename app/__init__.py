from flask import Flask
from flask_talisman import Talisman
from flask_seasurf import SeaSurf

app = Flask(__name__)
csp = {
    "default-src": "'self'",
    "style-src": ["'self'", "https://stackpath.bootstrapcdn.com"],
    "img-src": ["'self'", "https://img.youtube.com", "https://matomo.edjw.co.uk"],
    "script-src": ["'self'", "https://matomo.edjw.co.uk"],
}

Talisman(app, referrer_policy="same-origin", content_security_policy=csp)
csrf = SeaSurf(app)

from app import routes
from config import Config

app.config.from_object(Config)

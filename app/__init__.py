from flask import Flask
from app.config import DevConfig as config

app = Flask(__name__)
app.config.from_object(config)

from app import models, views


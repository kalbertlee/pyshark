from flask import Flask, url_for, request, redirect, render_template
from app.config import DevConfig
app = Flask(__name__)
app.config.from_object(DevConfig)

from app.templates import views,models
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app import app

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

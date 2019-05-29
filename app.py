from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy(app)
app.config.from_pyfile('config.py')

ma = Marshmallow(app)

from views import *

if __name__ == '__main__':
    app.run()

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Init App
app = Flask(__name__)

# Configure Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init addons
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
import models

# Schemas
import schemas

# Routes
import routes


# Run Server
if __name__ == "__main__":
    app.run(debug=True)

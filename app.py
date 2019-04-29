from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, hashlib, base64

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Link Model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    hash = db.Column(db.String(6),unique=True)
    hint = db.Column(db.Integer)

    def __init__(self,url,hash,hint):
        self.url = url
        self.hash = hash
        self.hint = hint

# Link Schema
class LinkSchema(ma.Schema):
    class Meta:
        fields = ('id','url','hash','hint')

link_schema = LinkSchema(strict=True)
links_schema = LinkSchema(many=True, strict=True)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)

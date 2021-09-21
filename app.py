import os, hashlib, base64
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from hashids import Hashids


# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SECRET_KEY'] = 'supersecret'
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Init Hashids
# hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

# Link Model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    hash = db.Column(db.String(6), unique=True)
    hint = db.Column(db.Integer)

    def __init__(self, url, hash, hint):
        self.url = url
        self.hash = hash
        self.hint = hint


# Link Schema
class LinkSchema(ma.Schema):
    class Meta:
        fields = ("id", "url", "hash", "hint")


link_schema = LinkSchema()
links_schema = LinkSchema(many=True)

# Routes

# Create a Link
@app.route("/", methods=["POST"])
def create_link():
    url = request.json["url"]
    # Hash from url
    hash = base64.urlsafe_b64encode(hashlib.md5(url.encode('utf-8')).digest())[:6]
    hint = 0
    # Validate hash (Unique)
    if Link.query.filter(Link.hash == hash).first():
        return jsonify({"hash": hash})
    else:
        new_link = Link(url, hash, hint)

        db.session.add(new_link)
        db.session.commit()

        return link_schema.jsonify(new_link)


# Get all Links
@app.route("/", methods=["GET"])
def get_links():
    links = Link.query.all()
    res = links_schema.dump(links)
    return jsonify(res.data)


# Get link
@app.route("/<hash>", methods=["GET"])
def get_link(hash):
    link = Link.query.filter(Link.hash == hash).first()
    if link:
        link.hint += 1
        db.session.commit()
    return link_schema.jsonify(link)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)

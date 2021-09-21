import hashlib
from flask import request, jsonify, redirect
from app import app, db, Link, link_schema, links_schema

def url_to_hash(url, digits=6):
    return hashlib.sha256(url.encode('utf-8')).hexdigest()[0:digits]

# Create a Link
@app.route("/", methods=["POST"])
def create_link():
    url = request.json["url"]
    hash = url_to_hash(url)

    link = Link.query.filter(Link.hash == hash).first()
    if link:
        return link_schema.jsonify(link)

    hint = 0
    new_link = Link(url, hash, hint)
    db.session.add(new_link)
    db.session.commit()
    return link_schema.jsonify(new_link)


# Get all Links
@app.route("/", methods=["GET"])
def get_links():
    links = Link.query.all()
    res = links_schema.dump(links)
    return jsonify(res)


# Get link
@app.route("/<hash>", methods=["GET"])
def get_link(hash):
    link = Link.query.filter(Link.hash == hash).first()
    if link:
        link.hint += 1
        db.session.commit()
    return redirect(link.url)
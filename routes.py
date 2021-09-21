from flask import request, jsonify, redirect
from app import app, db
from models import Link
from schemas import link_schema, links_schema
from utils import url_to_hash
from services import add_hit_to_link, get_all_links, get_link_by_hash, create_new_link

# Create a new Link
@app.route("/", methods=["POST"])
def create_link():
    url = request.json["url"]
    hash = url_to_hash(url)

    link = get_link_by_hash(hash)
    if link:
        return link_schema.jsonify(link)

    data = {"url": url, "hash": hash, "hint": 0}
    new_link = create_new_link(data)
    return new_link


# Get all Links
@app.route("/", methods=["GET"])
def get_links():
    res = get_all_links()
    return jsonify(res)


# Redirect to Link
@app.route("/<hash>", methods=["GET"])
def get_link(hash):
    link = get_link_by_hash(hash)
    if link:
        add_hit_to_link(link)
    return redirect(link.url)

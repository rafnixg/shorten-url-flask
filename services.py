from models import Link
from schemas import link_schema, links_schema
from app import db

def get_all_links():
    links = Link.query.all()
    return links_schema.dump(links)

def get_link_by_hash(hash):
    return Link.query.filter_by(hash=hash).first()

def add_hit_to_link(link):
    link.hint += 1
    db.session.commit()
    return link

def create_new_link(data):
    link = Link(**data)
    db.session.add(link)
    db.session.commit()
    return link_schema.jsonify(link)
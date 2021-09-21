from app import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    hash = db.Column(db.String(6), unique=True)
    hint = db.Column(db.Integer)

    def __init__(self, url, hash, hint):
        self.url = url
        self.hash = hash
        self.hint = hint
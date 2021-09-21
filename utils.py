import hashlib


def url_to_hash(url, digits=6):
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[0:digits]

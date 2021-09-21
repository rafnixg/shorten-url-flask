from app import ma


class LinkSchema(ma.Schema):
    class Meta:
        fields = ("id", "url", "hash", "hint")


link_schema = LinkSchema()
links_schema = LinkSchema(many=True)

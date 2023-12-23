from marshmallow import Schema, fields, post_load
from article import Article  # Assuming you have an article.py for the Article class
from source import Source

class SourceSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    
    @post_load
    def make_source(self, data, **kwargs):
        return Source(**data)

class ArticleSchema(Schema):
    source = fields.Nested(SourceSchema)
    author = fields.Str()
    title = fields.Str()
    description = fields.Str()
    url = fields.Url()
    urlToImage = fields.Url()
    publishedAt = fields.DateTime()
    content = fields.Str()

    @post_load
    def make_article(self, data, **kwargs):
        return Article(**data)

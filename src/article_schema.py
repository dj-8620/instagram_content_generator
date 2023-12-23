from marshmallow import Schema, fields, post_load
from article import Article  # Assuming you have an article.py for the Article class
from source import Source

class SourceSchema(Schema):
    id = fields.Str(allow_none=True)
    name = fields.Str(allow_none=True)
    
    @post_load
    def make_source(self, data, **kwargs):
        return Source(**data)

class ArticleSchema(Schema):
    source = fields.Nested(SourceSchema, allow_none=True)
    author = fields.Str(allow_none=True)
    title = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
    url = fields.Url(allow_none=True)
    urlToImage = fields.Url(allow_none=True)
    publishedAt = fields.DateTime(allow_none=True)
    content = fields.Str(allow_none=True)

    @post_load
    def make_article(self, data, **kwargs):
        return Article(**data)

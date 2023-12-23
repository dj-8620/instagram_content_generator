import os
import sys
from marshmallow import ValidationError
import requests
import json
from article import Article
from api_util import make_http_request
from loguru import logger
from article_schema import ArticleSchema

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from config import NEWS_BASE_URL

def build_request_url(api_key,  query='technology', page_size=10):
    base_url = NEWS_BASE_URL
    params = {
        'q': query,
        'pageSize': page_size,
        'apiKey': api_key,
    }
    return base_url, params

    
def fetch_news(api_key, query='technology', page_size=10):
    url, params = build_request_url(api_key, query, page_size)
    json_response = make_http_request(url, params)
    article_list = create_article_list(json_response)
    return article_list
    

def create_article_list(json_data):
    article_schema = ArticleSchema(many=True)  # 'many=True' allows deserializing multiple objects
    try:
        # Load JSON data into Article objects
        return article_schema.load(json_data['articles'])
    except ValidationError as err:
        # Handle validation errors, e.g., print them or log them
        print(err.messages)
        return []
    
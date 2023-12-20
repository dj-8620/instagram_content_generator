import os
import sys
import requests
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'config'))
from config import NEWS_API_KEY

def main():
    response = fetch_news(NEWS_API_KEY,page_size=3)
    pretty_response = json.dumps(response, indent=4)
    print(pretty_response)

    
def fetch_news(api_key, query='technology', page_size=10):
    base_url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'pageSize': page_size,
        'apiKey': api_key,
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erorr fetching news: {response.status_code}")
    
if __name__ == "__main__":
    main()
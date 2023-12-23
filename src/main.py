from loguru import logger
import news_fetcher
from config import NEWS_API_KEY
from logger import setup_logger

setup_logger()

def main():
    logger.info("Starting application")
    article_list = news_fetcher.fetch_news(NEWS_API_KEY, page_size=3)
    for article in article_list:
        print(article)
    ...
    
if __name__ == "__main__":
    main()
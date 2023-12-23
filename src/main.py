from loguru import logger
import news_fetcher
from config import NEWS_API_KEY
from logger import setup_logger
import prompt_engineering

setup_logger()

def main():
    logger.info("Starting application")
    article_list = news_fetcher.fetch_news(NEWS_API_KEY, page_size=5)
    description_list = news_fetcher.get_desc_of_articles(article_list)
    
    instagram_caption_prompt = prompt_engineering.create_instragram_prompt_from_description_list(description_list)
    print(instagram_caption_prompt)
    logger.info("Ending application")
    
if __name__ == "__main__":
    main()
import requests
from loguru import logger


def make_http_request(url, params):
    logger.debug(f"Requesting {url} with params {params}")
    response = requests.get(url, params=params)
    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")
    if response.status_code == 200:
        logger.info("Request successful")
        return response.json()
    else:
        logger.error(f"Request failed with status code {response.status_code}")
        raise Exception(f"Erorr making request: {response.status_code}")
    


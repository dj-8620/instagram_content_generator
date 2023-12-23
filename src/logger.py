from loguru import logger

def setup_logger():
    logger.add("../logs/application.log", rotation="500 MB", level="DEBUG")
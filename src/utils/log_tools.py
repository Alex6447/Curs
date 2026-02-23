from loguru import logger

logger.add("logs/log.log", level="DEBUG", rotation="10 MB")

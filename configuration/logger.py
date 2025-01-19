import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


def get_logger(name):
    return logging.getLogger(name)

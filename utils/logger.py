"""
logger
"""

import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file, level=logging.INFO, max_size=1000000, backup_count=3):
    """
    Sets up the logger
    :param backup_count:
    :param max_size:
    :param name:
    :param log_file:
    :param level:
    :return:
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    handler.setFormatter(formatter)

    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.addHandler(handler)
    logger.addHandler(stdout_handler)

    return logger

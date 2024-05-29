import pytest
import logging
from dotenv import load_dotenv
import os


load_dotenv()

@pytest.fixture(scope="session")
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('step_logger')
    yield logger


@pytest.fixture(scope="session")
def base_url():
    """
    Fixture to define the base URL for API requests.
    """
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def config():
    """
    Fixture to load test configuration from a file.
    """
    config_data = {
        "endpoints": {
            "author": "/author/",
            "title": "/title",
            "non_existent": "/unknown/"
        }
    }
    return config_data

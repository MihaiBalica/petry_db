from utils.logger import setup_logger
from contextlib import contextmanager


@contextmanager
def step_logger(step_type: str, description: str):
    logger = setup_logger(__name__, 'poetry_tests.log')
    logger.info(f"{step_type}: {description}")
    yield
    logger.info(f"{step_type} completed: {description}")


@contextmanager
def given(description: str):
    with step_logger("GIVEN", description):
        yield


@contextmanager
def when(description: str):
    with step_logger("WHEN", description):
        yield


@contextmanager
def then(description: str):
    with step_logger("THEN", description):
        yield


@contextmanager
def also(description: str):
    with step_logger("AND", description):
        yield

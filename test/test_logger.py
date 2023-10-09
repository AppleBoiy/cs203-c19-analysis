import logging

import pytest

from src.logger import Logger


@pytest.fixture
def logger():
    return Logger()


def test_setup_logger_write(logger):
    logger.is_write = True
    logger.setup_logger()
    handlers = logger.console.handlers
    assert isinstance(handlers[0], logging.FileHandler)


def test_setup_logger_debug(logger):
    logger.debug = True
    logger.setup_logger()
    handlers = logger.console.handlers
    assert isinstance(handlers[0], logging.StreamHandler)


def test_log_debug_true(logger, caplog):
    logger.debug = True
    logger.log("info", "test message")
    assert "test message" in caplog.text


def test_log_debug_false(logger, caplog):
    logger.debug = False
    logger.log("info", "test message")
    assert "test message" not in caplog.text


def test_log_debug_true_write_true(logger, caplog):
    logger.debug = True
    logger.is_write = True
    logger.log("info", "test message")
    assert "test message" in caplog.text

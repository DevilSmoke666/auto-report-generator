import os
import pytest
from app import config


def test_service_account_path():
    assert config.SERVICE_ACCOUNT_PATH is not None
    assert isinstance(config.SERVICE_ACCOUNT_PATH, str)
    assert config.SERVICE_ACCOUNT_PATH.endswith(".json")


def test_gmail_credentials_path():
    assert config.GMAIL_CREDENTIALS_PATH is not None
    assert isinstance(config.GMAIL_CREDENTIALS_PATH, str)
    assert config.GMAIL_CREDENTIALS_PATH.endswith(".json")


def test_email_user():
    assert config.EMAIL_USER is not None
    assert "@" in config.EMAIL_USER


def test_email_password():
    assert config.EMAIL_APP_PASSWORD is not None
    assert isinstance(config.EMAIL_APP_PASSWORD, str)


def test_email_to():
    assert config.EMAIL_TO is not None
    assert "@" in config.EMAIL_TO

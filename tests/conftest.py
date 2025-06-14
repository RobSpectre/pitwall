"""
Shared test configuration and fixtures for Pitwall - The agentic AI companion to MultiViewer.
"""

import pytest
from unittest.mock import patch
import os


@pytest.fixture
def mock_env_openrouter_key():
    """Mock environment variable for OpenRouter API key."""
    with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-api-key"}):
        yield


@pytest.fixture
def mock_multiviewer_running():
    """Mock MultiViewer as running successfully."""
    with patch("pitwall.cli._check_multiviewer", return_value=True):
        yield


@pytest.fixture
def mock_multiviewer_not_running():
    """Mock MultiViewer as not running."""
    with patch("pitwall.cli._check_multiviewer", return_value=False):
        yield


@pytest.fixture
def mock_requests_success():
    """Mock successful HTTP requests."""
    with patch("requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        yield mock_get


@pytest.fixture
def mock_requests_failure():
    """Mock failed HTTP requests."""
    with patch("requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        yield mock_get


@pytest.fixture
def sample_model_shortcuts():
    """Sample model shortcuts for testing."""
    return {
        "test-model": "provider/test-model",
        "another-model": "provider/another-model",
    }


@pytest.fixture(autouse=True)
def clean_environment():
    """Clean up environment variables after each test."""
    yield
    # Clean up any test environment variables
    test_vars = ["OPENROUTER_API_KEY", "ANTHROPIC_API_KEY"]
    for var in test_vars:
        if var in os.environ:
            del os.environ[var]

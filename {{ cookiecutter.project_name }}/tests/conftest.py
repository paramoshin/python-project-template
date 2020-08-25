"""Package-wide test fixtures."""
import pytest
from _pytest.config import Config


def pytest_configure(config: Config) -> None:
    """Example pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def mock_example():
    """Example fixture."""
    yield

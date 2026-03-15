import importlib
import pytest
import src.app as app_module


@pytest.fixture
def reload_app():
    """Reload the `src.app` module to reset in-memory state between tests."""
    def _reload():
        importlib.reload(app_module)
        return app_module
    return _reload

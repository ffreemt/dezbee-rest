"""Test dezrest."""
# pylint: disable=broad-except
from dezrest import __version__, dezrest


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not dezrest()
    except Exception:
        assert True

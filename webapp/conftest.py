import pytest


def pytest_runtest_protocol(item, nextitem):
    """Custom protocol to show test docstrings during execution."""
    docstring = item.function.__doc__
    if docstring:
        print(f"\n\n\nDescription: {docstring.strip()}")
    return None

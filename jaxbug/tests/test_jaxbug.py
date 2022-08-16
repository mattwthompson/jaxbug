"""
Unit and regression test for the jaxbug package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import jaxbug


def test_jaxbug_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "jaxbug" in sys.modules

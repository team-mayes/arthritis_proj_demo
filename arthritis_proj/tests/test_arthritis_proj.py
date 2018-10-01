"""
Unit and regression test for the arthritis_proj package.
"""

# Import package, test suite, and other packages as needed
import arthritis_proj
import pytest
import sys


def test_arthritis_proj_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "arthritis_proj" in sys.modules

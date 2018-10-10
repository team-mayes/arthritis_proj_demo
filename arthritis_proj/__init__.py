"""
arthritis_proj
Demo including processing data from a csv
"""

# Make Python 2 and 3 imports work the same
# Safe to remove with Python 3-only code
from __future__ import absolute_import

# Add imports here
from .data_proc import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

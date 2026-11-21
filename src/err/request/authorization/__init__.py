# src/err/request/authorization/__init__.py

"""
Module: err.request.authorization.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

# =========== ERR.REQUEST.AUTHORIZATION PACKAGE ===========#

# Packages
from .crud import *
from .attack import *
from .maneuver import *
from .promotion import *

# Modules
from .exception import PermissionRequestException
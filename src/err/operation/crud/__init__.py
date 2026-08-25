# src/err/operator/crud/__init__.py

"""
Module: err.operator.crud.__init__
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

# ============ ERR.OPERATOR.CRUD PACKAGE ===========#

# Packages
from .deleter import *
from .inserter import *
from .searcher import *

# Modules
from .exception import CrudOperatorException
# src/err/operator/crud/__init__.py

"""
Module: err.operation.crud.__init__
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

# ============ err.operation.CRUD PACKAGE ===========#

# Packages
from .deleter import *
from .inserter import *
from .searcher import *

# Modules
from .exception import CrudWorkerException
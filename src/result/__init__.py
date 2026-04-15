# src/result/__init__.py

"""
Module: result.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== RESULT PACKAGE ===========#

# Packages
from .analysis import *
from .build import *
from .computation import *
from .deletion import *
from .insertion import *
from .search import *
from .update import *
from .validation import*

# Modules
from .result import Result
from .category import ResultCategory
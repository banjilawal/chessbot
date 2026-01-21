# src/chess/system/data/result/__init__.py

"""
Module: chess.system.data.result.__init__
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

# =========== SYSTEM.DATA.RESULT PACKAGE CONTENTS ===========#

# Packages
from .search import *
from .update import *
from .deletion import *
from .insertion import *
from .computation import *
from .exception import *

# Modules
from .result import DataResult
from .state import ResultState
from .empty import  EmptyDataResultException

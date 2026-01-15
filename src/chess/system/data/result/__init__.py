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
from .deletion import *
from .insertion import *
from .calculation import *

# Modules
from .result import DataResult
from .empty import  EmptyDataResultException

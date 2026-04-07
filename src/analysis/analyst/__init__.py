# src/analysis/analyst/analyst/__init__.py

"""
Module: analysis.analyst.analyst.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== ANALYSIS.ANALYST PACKAGE ===========#

# Packages
from .collision import *

# Modules
from .analyst import  Analyst
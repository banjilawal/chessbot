# src/artifact/result/__init__.py

"""
Module: artfifact.result.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

# ============ ARTIFACT.RESULT PACKAGE ===========#

# Packages
from .analysis import *
from .attack import *
from .authorizable import *
from .builder import *
from .computation import *
from .encounter import *
from .event import *
from .interface import *
from .shell import *
from .turn import *
from .validation import*

# Modules
from .result import Result
from .state import ResultState
from .category import MethodResultType
# src/consistency/__init__.py

"""
Module: consistency.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


# =========== CONSISTENCY PACKAGE ===========#

# Packages
from .arena import *
from .board import *
from .game import *
from .maneuver import *
from .path import *
from .player import *
from .snapshot import *
from .square import *
from .team import *
from .token import *

# Module
from .checker import ConsistencyChecker

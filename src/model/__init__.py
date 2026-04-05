# src/model/__init__.py

"""
Module: model.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# =========== PACKAGE CONTENTS ===========#

# Packages
from .arena import *
from .board import *
from .game import *
from .hostage import *
from .player import *
from .query import *
from .rank import *
from .square import *
from .team import *
from .token import *

# Modules
None
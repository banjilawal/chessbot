# src/microservice/__init__.py

"""
Module: microservice.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

import logging

log = logging.getLogger("chessbot")

# ============= MICROSERVICE. PACKAGE ===========#

# Packages
from .arena import *
from .binder import *
from .board import *
from .catalog import *
from .coord import *
from .game import *
from .hostage import *
from .identity import *
from .player import *
from .rank import *
from .scalar import *
from .snapshot import *
from .square import *
from .team import *
from .token import *
from .vector import *

# Modules
from .microservice import Microservice
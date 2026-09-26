# src/err/client/validation/model/__init__.py

"""
Module: err.client.validation.model.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

# =========== ERR.CLIENT.MODEL PACKAGE ===========#

# Packages
from .arena import *
from .attack import *
from .board import *
from .coord import *
from .game import *
from .maneuver import *
from .path import *
from .player import *
from .rank import *
from .scalar import *
from .square import *
from .team import *
from .token import *
from .vector import *

# Modules
from .exception import ModelValidationClientException
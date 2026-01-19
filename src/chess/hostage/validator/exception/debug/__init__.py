# src/chess/hostage/validator/exception/debug/same/__init__.py

"""
Module: chess.hostage.validator.exception.debug.same.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

# =========== HOSTAGE.VALIDATOR.EXCEPTION.DEBUG.SAME PACKAGE CONTENTS ===========#

# Packages
from .null import *
from .same import *
from .same import *
from .formation import *
from .different import *

# Modules
from .king import KingCannotBeCapturedException
from .free import FreeEnemyContradictsCaptureException
from .friend import FriendCannotCaptureFriendException
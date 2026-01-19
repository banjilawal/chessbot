# src/chess/prisoner/validator/exception/debug/__init__.py

"""
Module: chess.prisoner.validator.exception.debug.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

# =========== HOSTAGE.VALIDATOR.EXCEPTION.DEBUG PACKAGE CONTENTS ===========#

# Packages
from .different import *
from .null import *
from .same import *

# Modules
from .king import KingCannotBeCapturedException
from .free import FreeEnemyContradictsCaptureException
from .friend import FriendCannotCaptureFriendException
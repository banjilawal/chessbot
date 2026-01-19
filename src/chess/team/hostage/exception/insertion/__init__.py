# src/chess/team/prisoner/exception/insertion/__init__.py

"""
Module: chess.team.prisoner.exception.insertion.__init__
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

# =========== TEAM.HOSTAGE.EXCEPTION.INSERTION PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .king import CannotCaptureKingException
from .active import AddingActiveTokenException
from .wrapper import AddingHostageTokenFailedException
from .duplicate import EnemyAlreadyCapturedException
from .friend import FriendCannotCaptureFriendException

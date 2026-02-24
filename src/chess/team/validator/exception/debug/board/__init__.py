# src/chess/team/validator/exception/debug/board/__init__.py

"""
Module: chess.team.validator.exception.debug.board.__init__
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

# =========== TEAM.VALIDATOR.EXCEPTION.DEBUG.BOARD PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .stale import BoardHasStaleTeamLinkException
from .register import TeamNotRegisteredBoardException
from .occupied import TeamSlotAlreadyOccupiedException
from .null import TeamBelongsToDifferentBoardException
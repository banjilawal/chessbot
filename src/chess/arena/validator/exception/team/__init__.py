# src/chess/arena/number_bounds_validator/exception/team/__init__.py

"""
Module: chess.game.arena.number_bounds_validator.exception.team.__init__
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

# =========== ARENA.VALIDATOR.EXCEPTION.TEAM PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .none import NoTeamsInArenaException
from .many import ToManyTeamsInArenaException
from .single import SingleTeamInArenaException
from .color import TeamColorCollisionException
from .duplicate import DuplicateTeamInArenaException

# src/chess/occupant/validator/exception/debug/registration/__init__.py

"""
Module: chess.occupant.validator.exception.debug.registration.__init__
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

#=========== TOKEN.VALIDATOR.EXCEPTION.REGISTRATION PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .catchall import TokenNotRegisteredException
from .team import TokenNotRegisteredWithTeamException
from .board import TokenNotRegisteredWithBoardException
from .square import TokenNotRegisteredWithSquareException
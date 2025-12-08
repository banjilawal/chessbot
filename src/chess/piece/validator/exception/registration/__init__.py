# src/chess/piece/validator/exception/registration/__init__.py

"""
Module: chess.piece.validator.exception.registration.__init__
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

# =========== PIECE.VALIDATOR.EXCEPTION.REGISTRATION PACKAGE CONTENTS ===========#

# Packages
None

# Modules
from .base import PieceRegistrationException
from .board import PieceNotRegisteredWithBoardException
from .team import PieceNotRegisteredWithTeamException
from .square import PieceNotRegisteredWithSquareException
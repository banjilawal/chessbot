# src/chess/dyad/validator/exception/base.py

"""
Module: chess.dyad.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system.err import ChessException
from chess.system import ValidationFailedException

class InvalidSchemaAgentPairException(ChessException, ValidationFailedException):
    pass
# src/chess/dyad/validator/exception/null.py

"""
Module: chess.dyad.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.dyad import InvalidSchemaAgentPairException

class NullSchemaAgentPairException(InvalidSchemaAgentPairException, NullException):
    pass
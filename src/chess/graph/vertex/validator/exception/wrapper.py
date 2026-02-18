# src/chess/graph/square/validator/exception/wrapper.py

"""
Module: chess.graph.square.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from chess.system import ValidationFailedException

__all__ = [
    # ======================# NODE_VALIDATION_FAILURE EXCEPTION #======================#
    "NodeValidationFailedException",
]

class NodeValidationFailedException(ValidationFailedException):
    pass
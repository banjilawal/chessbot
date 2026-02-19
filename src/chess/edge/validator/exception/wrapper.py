# src/chess/edge/validator/exception/wrapper.py

"""
Module: chess.edge.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.system import ValidationFailedException

__all__ = [
    # ======================# EDGE_VALIDATION_FAILURE EXCEPTION #======================#
    "EdgeValidationFailedException",
]

class EdgeValidationFailedException(ValidationFailedException):
    pass
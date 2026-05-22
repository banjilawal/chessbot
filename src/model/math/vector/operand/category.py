# src/model/math/vector/register/category.py

"""
Module: model.math.vectoroperand.category
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class OperandCategory(Enum):
    """
    Role:
        -   State

    Responsibilities:
        1.  Describes What type of operands are in the operand.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    COORD_OPERAND = auto(),
    VECTOR_OPERAND = auto(),
    NOT_INITIALIZED = auto(),
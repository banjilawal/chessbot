# src/model/state/math/vector/register/category.py

"""
Module: model.state.math.vector.register.category
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class OperandRegisterContentType(Enum):
    """
    Role:
        -   State

    Responsibilities:
        1.  Describes What type of operands are in the Vecregister.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    COORD_REGISTER = auto(),
    VECTOR_REGISTER = auto(),
    NOT_INITIALIZED= auto(),
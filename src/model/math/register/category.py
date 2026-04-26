# src/model/math/register/category.py

"""
Module: model.math.register.category
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class RegisterCategory(Enum):
    """
    Role:
        -   State

    Responsibilities:
        1.  Describes What type of operands are in the register.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    COORD_REGISTER= auto(),
    VECTOR_REGISTER= auto(),
    NOT_INITIALIZED= auto(),
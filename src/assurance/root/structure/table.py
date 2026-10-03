# src/assurance/validator/model/encounter/common/structure/table.py

"""
Module: assurance.validator.model.encounter.common.table.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Model

T = TypeVar("T", bound="Model")

class RootPropertyTable(ABC, Generic[T]):
    """
    Role
        - Structure Holder

    Responsibilities:
        1.  Stores a Super class's properties that a ReferencePropertyTableGenerator
            validates

    Attributes:
    
    Provides:

    Super Class:
    """
    pass
    

    
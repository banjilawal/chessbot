# src/assurance/validator/model/encounter/common/data/table.py

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

class ParentPropertyTable(ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores a Super class's properties that a ReferencePropertyTableGenerator
            validates

    Attributes:
    
    Provides:

    Super Class:
    """
    pass
    

    
# src/logic/schema/service/operation/properties/reporter.py

"""
Module: logic.schema.service.operation.properties.reporter
Author: Banji Lawal
Created: 2026-03-02
version: 1.0.0
"""

from __future__ import annotations

from typing import List

from build.scalar import Scalar
from catalog.schema import Schema
from logic.system import GameColor


class SchemaPropertyValuesReporter:
    """
    Role:Build Configuration Table, Schema, Metadata Set
    
    Responsibilities:
        1.  Provides lists of all the property values for easier iteration.

    Attributes:
        names: List[str]
        pawn_rows: List[int]
        rank_rows: List[int]
        colors: List[GameColor]
        advancing_steps: List[Scalar]
        
    Provides:
    
    Super Class:
    """
    
    @property
    def colors(self) -> List[GameColor]:
        return [entry.color for entry in Schema]
    
    @property
    def names(self) -> List[str]:
        return [entry.name for entry in Schema]
    
    @property
    def pawns_rows(self) -> List[int]:
        return [entry.pawn_row for entry in Schema]
    
    @property
    def rank_rows(self) -> List[int]:
        return [entry.rank_row for entry in Schema]
    
    @property
    def advancing_steps(self) -> List[Scalar]:
        return [entry.advancing_step for entry in Schema]
    
    
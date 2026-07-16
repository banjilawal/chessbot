# src/span/table/span.py

"""
Module: span.table.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from container import VectorSet
from model import Vector
from span.table import PawnVectorSetTable
from span.table.knight import VectorSetGroupTable


class RankVectorSetTable:
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfMovement errors by calculating the last point in the direction
            of travel

    Attributes:
        entries: Dict[str: VectorSet]
        
    Provides:

    Super Class:
    """
    _pawn_vector_table: PawnVectorSetTable
    _vector_group_table: VectorSetGroupTable
    
    def __init__(
            self,
            pawn_vector_table: PawnVectorSetTable | None = PawnVectorSetTable(),
            vector_group_table: VectorSetGroupTable | None = VectorSetGroupTable(),
    ):
        """
        """
        self._pawn_vector_table = pawn_vector_table
        self._vector_group_table = vector_group_table
        
    @property
    def knight_movement_vectors(self) -> VectorSet:
        return self._vector_group_table.knight_movement_vectors
    
    @property
    def king_movement_vectors(self) -> VectorSet:
        return self._vector_group_table._king_vectors
    

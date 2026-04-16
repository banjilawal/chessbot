# src/model/binder/arena/model.py

"""
Module: model.binder.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from microservice import PlayerService
from model import Binder, Arena, Schema, Player


class ArenaPlayerBinder(Binder[Arena, Player]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder

    Responsibility:
        1.  Separates responsibilities of managing players bound to a arena.

    Attributes:
        id: int
        primary: Arena
        satellite_list: List[Player]
        schema_list: List[Schema]
        white_satellite: Optional[Player]
        black_satellite: Optional[Player]
        satellite_table: Dict[Schema, S]
        satellite_service: Microservice[Player]
        is_empty: bool
        is_full: bool
        is_white_slot_occupied: bool
        is_black_slot_occupied: bool

    Provides:

    Super Class:
        Binder
    """
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            satellite_service: PlayerService,
            satellite_table: Dict[Schema, Player],
    ):
        """
        Args:
            id: int
            arena: Arena
            satellite_service: Microservice[Player]
            satellite_table: Dict[str, Player]
        """
        super().__init__(
            id=id,
            primary=arena,
            satellite_table=satellite_table,
            satellite_service=satellite_service
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaPlayerBinder):
            return super().__eq__(other)
        
    def __hash__(self):
        return hash(self.id)

        
    
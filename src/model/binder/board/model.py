# src/model/binder/board/model.py

"""
Module: model.binder.board.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from microservice import TeamService
from model import Binder, Board, Schema, Team


class BoardTeamBinder(Binder[Board, Team]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder

    Responsibility:
        1.  Separates responsibilities of managing teams bound to a board.

    Attributes:
        id: int
        primary: Board
        satellite_list: List[Team]
        schema_list: List[Schema]
        white_satellite: Optional[Team]
        black_satellite: Optional[Team]
        satellite_table: Dict[Schema, S]
        satellite_service: Microservice[Team]
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
            board: Board,
            satellite_service: TeamService,
            satellite_table: Dict[Schema, Team],
    ):
        """
        Args:
            id: int
            board: Board
            satellite_service: Microservice[Team]
            satellite_table: Dict[str, Team]
        """
        super().__init__(
            id=id,
            primary=board,
            satellite_table=satellite_table,
            satellite_service=satellite_service
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardTeamBinder):
            return super().__eq__(other)
        
    def __hash__(self):
        return hash(self.id)

        
    
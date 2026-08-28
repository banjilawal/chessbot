# src/domain/structure/binder/board/binder.py

"""
Module: domain.structure.binder.board.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, Iterator, Optional, cast

from domain import Archetype, ColorBinder, Board, Team
from microservice import TeamService


class BoardTeamColorBinder(ColorBinder[Board, Team]):
    """
    Role:
        - Model
        -  Stateless Data-Holder

    Responsibility:
        1.  Maps the Team correctly to its color slot on the Board.
    Attributes:
        id: int
        primary: Board
        white_satellite: Optional[Team]
        black_satellite: Optional[Team]
        satellite_service: TeamService
        
        has_both_slots_occupied: bool
        has_both_slots_empty: bool
        
        satellite_iter: Iterator[Team]
        
    Provides:
        is_empty: bool
        is_full: bool
        is_white_slot_occupied: bool
        is_black_slot_occupied: bool
        
    Super Class:
       ColorBinder
    """
    
    def __init__(
            self,
            id: int,
            board: Board,
            satellite_service: TeamService,
            satellite_table: Dict[Archetype, Team],
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
        
    @property
    def primary(self) -> Board:
        return cast(Board, super().primary)
    
    @property
    def satellite_service(self) -> TeamService:
        return cast(TeamService, super().satellite_service)
    
    @property
    def has_both_slots_occupied(self) -> bool:
        return len(self._satellite_table) == 2
    
    @property
    def has_both_slots_empty(self) -> bool:
        return len(self._satellite_table) == 0
    
    @property
    def has_white_slot_occupied(self) -> bool:
        return self._satellite_table[Archetype.WHITE] is not None
    
    @property
    def has_black_slot_occupied(self) -> bool:
        return self._satellite_table[Archetype.BLACK] is not None
    
    @property
    def white_satellite(self) -> Optional[Team]:
        if Archetype.WHITE not in self._satellite_table.keys():
            return None
        return self._satellite_table[Archetype.WHITE]
    
    @property
    def black_satellite(self) -> Optional[Team]:
        if Archetype.BLACK not in self._satellite_table.keys():
            return None
        return self._satellite_table[Archetype.BLACK]
    
    @property
    def satellite_iter(self) -> Iterator[Team]:
        return self._satellite_table.values().__iter__()
    
    @property
    def archetype_iter(self) -> Iterator[Archetype]:
        return self._satellite_table.keys().__iter__()
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardTeamColorBinder):
            return super().__eq__(other)
        return False
        
    def __hash__(self):
        return hash(self.id)

        
    
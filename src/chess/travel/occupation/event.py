# src/chess/owner/travel/occupation/validator.py

"""
Module: `chess.owner.travel.occupation.event`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from abc import ABC
from typing import Optional

from chess.board import Board
from chess.system import Event, LoggingLevelRouter
from chess.square import Square
from chess.piece import Piece, TravelEvent


class OccupationEvent(ABC, TravelEvent):
    _actor_square: Square
    
    @LoggingLevelRouter.monitor
    def __init__(
        self,
        id: int,
        actor: Piece,
        actor_square: Square,
        destination_square: Square,
        execution_environment: Board,
        parent: Optional[Event] = None
    ):
        super().__init__(
            id=id,
            actor=actor,
            parent=parent,
            destination_square=destination_square,
            execution_environment=execution_environment
        )
        self._actor_square = actor_square
    
    @property
    def actor_square(self) -> Square:
        return self._actor_square
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, OccupationEvent):
                return True
        return False

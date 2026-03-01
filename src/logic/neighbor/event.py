# src/logic/neighbor/factory.py

"""
Module: logic.neighbor.neighbor
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""
from typing import cast

from logic.piece import Piece
from logic.board import Board
from logic.coord import Coord
from logic.domain import Domain
from logic.system import Event
from logic.neighbor.table import VisitationTable


class VisitationEvent(Event[Domain, VisitationTable, Board]):
    _id: int
    _visitor: Piece
    _site: Coord
    
    def __init__(
            self,
            id: int,
            actor: Domain,
            resource: VisitationTable,
            execution_environment: Board,
            visitor: Piece
    ):
        super().__init__(id=id, actor=actor, resource=resource, execution_environment=execution_environment)
        self._visitor = visitor
        self._site = self._visitor.current_position
        
        
    @property
    def visitor(self):
        return self.visitor
    
    @property
    def domain(self) -> Domain:
        return cast(Domain, self.actor)
    
    @property
    def table(self) -> VisitationTable:
        return cast(VisitationTable, self.resource)
    
    @property
    def site(self) -> Coord:
        return self._site
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, VisitationEvent):
            return (
                self.domain.owner == other.domain.owner and self._visitor == other.visitor and self._site == other.site
            )
        return False
        
    
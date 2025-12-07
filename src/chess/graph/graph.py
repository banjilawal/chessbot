# src/chess/graph/graph.py

"""
Module: chess.graph.graph
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""
from re import search
from typing import List, Optional, cast

from chess.piece import OccupationEvent, OccupationEventValidator, Piece
from chess.board import Board, BoardPieceSearch, BoardSearchContext
from chess.domain import Domain
from chess.system.transaction import TransactionResult
from chess.neighbor import NeighborTuple, VisitationService
from chess.enviroment import BoardActorValidator


class Graph:
    """"""
    _id: int
    _board: Board
    _domains: List[Domain]
    _neighbors: List[NeighborTuple]

    def __init__(
            self,
            id: int,
            board: Board
    ):
        self._id = id
        self.board = board
        self._domains = List[Domain]
        self._neighbors = List[NeighborTuple]
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def domains(self) -> List[Domain]:
        return self._domains
    
    @property
    def neighbors(self) -> List[NeighborTuple]:
        return self._neighbors
    
   #  def update(self, event: OccupationEvent, visitation_service: VisitationService) -> TransactionResult:
   #      event_validation = OccupationEventValidator.validate(event)
   #      if event_validation.is_failure():
   #          return TransactionResult.errored(event_update=event, exception=event_validation.exception)
   #      domain_search_result = find_domain(piece=event.actor)
   #
   #      actor = event.actor
   #      domain = Domain(piece=event.actor)
   #      for point in actor.rank_name.compute_span(actor):
   #          search_result = BoardPieceSearch.searcher(self._board, TeamSearchContext(target=point))
   #          if search_result.is_failure():
   #              return TransactionResult.errored(event_update=event, exception=search_result.exception)
   #
   #          if search_result.is_success():
   #              domain.residents.append(cast(search_result.payload[0]))
   #
   #          if search_result.is_empty() and point not in domain.tree:
   #              domain.tree.append(point)
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #
   #      return TransactionResult.success(event_update=event)
   #
   #
   #
   #
   # def find_domain(self, piece: Piece) -> Optional[Domain]:
   #     hit = next((domain for domain in self._domains if domain.owner == piece), None)
   #     if hit is not None:
   #         return hit
   #     return None
       
       

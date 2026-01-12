# src/chess/board/service.py

"""
Module: chess.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""
from typing import cast

from chess.board import Board, BoardBuilder, BoardValidator
from chess.board.relation import BoardSquareRelationAnalyzer
from chess.system import id_emitter
from chess.system.service import EntityService
from chess.team import TeamService


class BoardService(EntityService[Board]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Board microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Board state by providing single entry and exit points to Board
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   BoardService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "BoardService"
    _square_relation_analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: BoardBuilder = BoardBuilder(),
            validator: BoardValidator = BoardValidator(),
            square_relation_analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer()
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (BoardFactory)
            *   validator (BoardValidator)

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._square_relation_analyzer = square_relation_analyzer
    
    @property
    def builder(self) -> BoardBuilder:
        """get BoardBuilder"""
        return cast(BoardBuilder, self.entity_builder)
    
    @property
    def validator(self) -> BoardValidator:
        """get BoardValidator"""
        return cast(BoardValidator, self.entity_validator)
    
    @property
    def square_relation_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._board_square_relation_analyzer
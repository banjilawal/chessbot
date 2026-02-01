# src/chess/board/service.py

"""
Module: chess.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from typing import cast

from chess.square import AddingDuplicateSquareException, Square
from chess.system import InsertionResult, LoggingLevelRouter, id_emitter, EntityService
from chess.board import (
    AddingBoardSquareFailedException, Board, BoardBuilder, BoardServiceException, BoardValidator,
    BoardSquareRelationAnalyzer, BoardServiceInsertionOpFailedException, SquareOnDifferentBoardException,
)


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
    None

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
    
    @LoggingLevelRouter.monitor
    def layout_board(self, board: Board) -> InsertionResult[Board]:
        method = "BoardService.layout_board"
        
        validation = self.validator.validate(candidate=board)
        if validation.is_failure:
            return InsertionResult.failure(
                BoardServiceException(
                    f"{method}: {BoardServiceException.DEFAULT_MESSAGE}",
                    ex=validation.exception,
                )
            )
        
        for entry in board.team_hash.table:
        
        


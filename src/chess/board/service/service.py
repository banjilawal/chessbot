# src/chess/board/service.py

"""
Module: chess.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from typing import cast

from chess.square import AddingDuplicateSquareException, Square
from chess.system import InsertionResult, id_emitter, EntityService
from chess.board import (
    AddingBoardSquareFailedException, Board, BoardBuilder, BoardServiceException, BoardValidator,
    SquareOnDifferentBoardException, BoardSquareRelationAnalyzer
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
    
    @property
    def square_relation_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._board_square_relation_analyzer
    
    def insert_square(self, board: Board, square: Square) -> InsertionResult[Square]:
        """
        # ACTION:
            1.  If the square fails validation send the wrapped exception in the InsertionResult.
            2.  If the square does not belong to the board a wrapped exception needs to be sent in the InsertionResult.
            3.  If square is a captured CombatantToked a wrapped exception needs to be sent in the InsertionResult.
            4.  If self._calculate_remaining_rank_quota returns an error or zero open slots then send the wrapped
                in the InsertionResult.
            5.  Send the number of open slots in the InsertionResult.
        # PARAMETERS:
            *   rank (Rank)
        # RETURN:
            *   InsertionResult[SQuare] containing either:
                - On failure: Exception
                - On success: Square
        # RAISES:
            *   BoardServiceException
            *   AddingDuplicateSquareException
            *   AddingBoardMemberFailedException
            *   SquareOnDifferentBoardException
        """
        method = "BoardService.insert_square"
        
        relation_analysis = self._square_relation_analyzer.analyze(
            candidate_primary=board,
            candidate_secondary=square
        )
        # Handle the case that the relation analysis is not completed.
        if relation_analysis.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"{method}: {BoardServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=relation_analysis.exception
                    )
                )
            )
        # Handle the case that the Square is assigned to a different Board.
        if relation_analysis.does_not_exist:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"{method}: {BoardServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=SquareOnDifferentBoardException(
                            f"{method}: {SquareOnDifferentBoardException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the square is already present on the board.
        if relation_analysis.fully_exists:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"{method}: {BoardServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=AddingDuplicateSquareException(
                            f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Run the insertion operation on using board.squares. ---#
        insertion_result = board.squares.add(square=square)
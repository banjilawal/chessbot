# src/chess/board/service.py

"""
Module: chess.board.service
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""
from pyexpat.errors import messages
from typing import cast

from chess.board import Board, BoardBuilder, BoardServiceException, BoardValidator, SquareOnDifferentBoardException
from chess.board.relation import BoardSquareRelationAnalyzer
from chess.square import Square
from chess.system import InsertionResult, id_emitter
from chess.system.service import EntityService
from chess.board import BoardService


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
            *   BoardRankQuotaFullException
            *   AddingDuplicateSquareException
            *   AddingCapturedBoardMemberException
            *   AddingBoardMemberFailedException
            *   EnemyCannotJoinBoardException
        """
        method = "BoardService.insert_square"
        
        relation_analysis = self._square_relation_analyzer.analyze(candidate_primary=board, candidate_secondary=square)
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
                        ex=SquareOnDifferentBoardException(f"{method}: {SquareOnDifferentBoardException.DEFAULT_MESSAGE}")
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
                        ex=DuplicateSquareAdditionException(
                            f"{method}: {DuplicateSquareAdditionException.DEFAULT_MESSAGE}"
                            )
                    )
                )
            )
        # --- Run the insertion operation on using board.squares. ---#
        insertion_result = board.squares.add_square(square=square)
        
        # Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardServiceException(
                    message=f"{method}: {BoardServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # On a successful insertion return the
        # Get the payload from insertion result. Decrease the rank's quota. Send the payload to the caller.
        payload = insertion_result.payload
        
        # Handle the case that the square is on a different board.
        if square.board != board:
            # Return exception chain.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=EnemyCannotJoinBoardException(f"{method}: {EnemyCannotJoinBoardException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the square is a captured combatant.
        if isinstance(square, CombatantSquare) and cast(CombatantSquare, square).captor is not None:
            # Return exception chain.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=AddingCapturedBoardMemberException(
                        f"{method}: {AddingCapturedBoardMemberException.DEFAULT_MESSAGE}"
                        )
                )
            )
        # --- Search the collection for the square. ---#
        search_result = self._squares.search_squares(context=SquareContext(square.id))
        
        # Handle the case that search did not complete.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )

        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=AddingDuplicateSquareException(f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}")
                )
            )
        # --- Find how many slots are open for the rank. ---#
        calculation_result = self._calculate_remaining_rank_quota(square.rank)
        
        # Handle the case that the calculation operation was not completed.
        if calculation_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        # --- Make sure the payload is an int. ---#
        remaining_slots = cast(int, calculation_result.payload)
        
        # Handle the case that the rank has been filled.
        if remaining_slots <= 0:
            # Return exception chain.
            return InsertionResult.failure(
                AddingBoardMemberFailedException(
                    message=f"{method}: {AddingBoardMemberFailedException.ERROR_CODE}",
                    ex=BoardRankQuotaFullException(f"{method}: {BoardRankQuotaFullException.DEFAULT_MESSAGE}")
                )
            )
        # --- Run the insertion operation on the DataService. ---#

        

        self._table.decrease_quota(rank=square.rank)
        return InsertionResult.success(payload=payload)
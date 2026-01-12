# src/chess/board/square/service.py

"""
Module: chess.board.square.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import (
    AddingBoardSquareFailedException, Board, BoardSquareRelationAnalyzer,
    BoardSquareServiceException
)
from chess.square import Square, UniqueSquareDataService
from chess.system import InsertionResult


class BoardSquareService:
    _data_service: UniqueSquareDataService
    _analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            data_service: UniqueSquareDataService = UniqueSquareDataService(),
            analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer(),
    ):
        self._analyzer = analyzer
        self._data_service = data_service
        
    @property
    def is_empty(self) -> bool:
        return self._data_service.is_empty
        
    @property
    def number_of_squares(self) -> int:
        return self._data_service.size
    
    @property
    def board_square_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._analyzer

    def member_insertion(self, board: Board, square: Square) -> InsertionResult[Square]:
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
            *   CalculationReport[int] containing either:
                - On failure: Exception
                - On success: int
        # RAISES:
            *   BoardRankQuotaFullException
            *   AddingDuplicateSquareException
            *   AddingCapturedBoardMemberException
            *   AddingRosterMemberFailedException
            *   EnemyCannotJoinRosterException
        """
        method = "RosterService.member_insertion"
        
        # Handle the case that the square fails validation.
        square_validation = self._data_service.square_service.validator.validate(square=square)
        if square_validation.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardSquareServiceException(
                    message=f"{method}: {BoardSquareServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the square is on a different board.
        if square.board != board:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=EnemyCannotJoinRosterException(f"{method}: {EnemyCannotJoinRosterException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the square is a captured combatant.
        if isinstance(square, CombatantSquare) and cast(CombatantSquare, square).captor is not None:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddingPrisonerToRosterException(f"{method}: {AddingPrisonerToRosterException.DEFAULT_MESSAGE}")
                )
            )
        # --- Search the collection for the square. ---#
        search_result = self._squares.search_squares(context=SquareContext(square.id))
        
        # Handle the case that search did not complete.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Handle the case that the square is already present.
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=AddingDuplicateSquareException(f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}")
                )
            )
        # --- Find how many slots are open for the rank. ---#
        calculation_result = self._calculate_remaining_rank_quota(square.rank)
        
        # Handle the case that the calculation operation was not completed.
        if calculation_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        # --- Make sure the payload is an int. ---#
        remaining_slots = cast(int, calculation_result.payload)
        
        # Handle the case that the rank has been filled.
        if remaining_slots <= 0:
            # Return exception chain.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=BoardRankQuotaFullException(f"{method}: {BoardRankQuotaFullException.DEFAULT_MESSAGE}")
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = self._squares.add_square(square=square)
        
        # Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                AddingRosterMemberFailedException(
                    message=f"{method}: {AddingRosterMemberFailedException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # Get the payload from insertion result. Decrease the rank's quota. Send the payload to the caller.
        payload = insertion_result.payload
        self._table.decrease_quota(rank=square.rank)
        return InsertionResult.success(payload=payload)
    
    

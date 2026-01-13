# src/chess/board/square/service.py

"""
Module: chess.board.square.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import (
    AddingBoardSquareFailedException, BoardSquareRelationAnalyzer, BoardSquareServiceException,
    BoardSquareServiceIsFullException
)
from chess.square import Square, SquareContext, UniqueSquareDataService
from chess.system import COLUMN_SIZE, InsertionResult, ROW_SIZE


class BoardSquareService:
    _capacity: int
    _data_service: UniqueSquareDataService
    _analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            capacity: int = ROW_SIZE * COLUMN_SIZE,
            data_service: UniqueSquareDataService = UniqueSquareDataService(),
            analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer(),
    ):
        self._capacity = capacity
        self._analyzer = analyzer
        self._data_service = data_service
        
    @property
    def is_empty(self) -> bool:
        return self._data_service.is_empty
    
    @property
    def is_full(self) -> bool:
        return self._data_service.size == self._capacity
        
    @property
    def number_of_squares(self) -> int:
        return self._data_service.size
    
    @property
    def board_square_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._analyzer

    def add(self, square: Square) -> InsertionResult[Square]:
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
        
        # Handle the case that the BoardSquareService is at capacity.
        if self.is_full:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardSquareServiceException(
                    message=f"{method}: {BoardSquareServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=BoardSquareServiceIsFullException(f"{method}: {BoardSquareServiceIsFullException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the square is not certified safe.
        square_validation = self._data_service.integrity_service.validator.validate(square=square)
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
        # --- Find out if a square is already at the coord ---#
        search_result = self._data_service.search_squares(context=SquareContext(coord=square.coord))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardSquareServiceException(
                    message=f"{method}: {BoardSquareServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the coord is already in use.
        if search_result.is_success:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardSquareServiceException(
                    message=f"{method}: {BoardSquareServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=BoardSquareCoordCollisionException(
                            f"{method}: {BoardSquareCoordColliionException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Run the insertion operation on the DataService. ---#
        insertion_result = self._data_service.add_unique_square(square=square)
        
        
        # Handle the case that the insertion was not completed
        if insertion_result.is_failure:
            # Return exception chain on failure.
            return InsertionResult.failure(
                BoardSquareServiceException(
                    message=f"{method}: {BoardSquareServiceException.ERROR_CODE}",
                    ex=AddingBoardSquareFailedException(
                        message=f"{method}: {AddingBoardSquareFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On insertion success extract the insertion payload and send in the BuildResult. ---#
        return InsertionResult.success(cast(Square, insertion_result.payload))
    
    

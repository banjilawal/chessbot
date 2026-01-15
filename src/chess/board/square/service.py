# src/chess/board/square/service.py

"""
Module: chess.board.square.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

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
            1.  If data_service is full then return an exception chain. Else hand off the square insertion to
                the data_service.
            2.  If the insertion was not successful then return an exception chain. Else the insertion was
                successful. Cast the insertion payload into a Square then send in the InsertionResult's payload.
                return the inserted square.
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception
                    - On success: Square
        # RAISES:
            *   BoardSquareServiceException
            *   AddingBoardSquareFailedException
            *   BoardSquareServiceIsFullException
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
        # --- Hand off the insertion to the self.data_service the DataService. ---#
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
    
    

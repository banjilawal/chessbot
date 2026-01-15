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
    BoardSquareListIsFullException
)
from chess.square import Square, UniqueSquareDataService
from chess.system import COLUMN_SIZE, InsertionResult, ROW_SIZE


class BoardSquareService:
    _capacity: int
    _member_service: UniqueSquareDataService
    _analyzer: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            capacity: int = ROW_SIZE * COLUMN_SIZE,
            member_service: UniqueSquareDataService = UniqueSquareDataService(),
            analyzer: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer(),
    ):
        self._capacity = capacity
        self._analyzer = analyzer
        self._member_service = member_service
        
    @property
    def is_empty(self) -> bool:
        return self._member_service.is_empty
    
    @property
    def is_full(self) -> bool:
        return self._member_service.size == self._capacity
        
    @property
    def number_of_members(self) -> int:
        return self._member_service.size
    
    @property
    def board_square_analyzer(self) -> BoardSquareRelationAnalyzer:
        return self._analyzer

    def add_member(self, square: Square) -> InsertionResult[Square]:
        """
        # ACTION:
            1.  If member_service is full then return an exception chain. Else hand off the square insertion to
                the member_service.
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
            *   BoardSquareListIsFullException
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
                        ex=BoardSquareListIsFullException(
                            f"{method}: {BoardSquareListIsFullException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Hand off the insertion to the self.member_service the DataService. ---#
        insertion_result = self._member_service.add_unique_square(square=square)
        
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
        # --- On insertion success forward the insertion_result to the caller. ---#
        return insertion_result
    
    

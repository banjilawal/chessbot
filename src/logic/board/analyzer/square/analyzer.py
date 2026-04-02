# src/logic/board/analyzer/validator.py

"""
Module: logic.board.analyzer.analyzer
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.square import Square, SquareContext, SquareService
from logic.system import LoggingLevelRouter, RelationAnalysis, RelationReport
from logic.board import Board, BoardSquareAnalysisException, BoardValidator


class BoardSquareRelationAnalysis(RelationAnalysis[Board, Square]):
    """
    Role:
        - Relation Analyzer
        - Report Generator

    Responsibilities:
        1.  Report the on the type of relationship is between the board and square.

    Attributes:

    Provides:
        -   analyze(
                    candidate_primary: Board,
                    candidate_satellite: Square,
                    board_validator: BoardValidator = BoardValidator(),
                    square_validator: SquareService = SquareService(),
            ) -> RelationReport[Board, Square]

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate_primary: Board,
            candidate_satellite: Square,
            board_validator: BoardValidator = BoardValidator(),
            square_service: SquareService = SquareService(),
    ) -> RelationReport[Board, Square]:
        """
        Generate a report on the relationship between a board and square.
        
        Action:
            1.  Send an AnalyzerFailure exception if either rank cannot be validated.
            2.  Otherwise, send the success result which can be:
                    -   No relation between them.
                    -   Board has expired link to square.
                    -   Square has not registered with board.
                    -   They have a fully bidirectional relation.
        Args::
            candidate_primary: Board
            candidate_satellite: Square
            board_validator: BoardValidator
            square_validator: SquareService
        Returns:
            RelationReport[Board, Square]
        Raises:
            BoardSquareAnalysisException
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the board is not secure.
        board_validation = board_validator.validate(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    msg=BoardSquareAnalysisException.MSG,
                    err_code=BoardSquareAnalysisException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Handle the case that, the square is unsecure.
        square_validation = square_service.validator.validate(candidate_satellite)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    msg=BoardSquareAnalysisException.MSG,
                    err_code=BoardSquareAnalysisException.ERR_CODE,
                    ex=square_validation.exception,
                )
            )
        square = cast(Square, square_validation.payload)
        

        # --- Search the board's squares for the satellite-rank. ---#
        square_search = board.squares.search(context=SquareContext(id=square.id))
        
        # Handle the case that, the search was aborted.
        if square_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    msg=BoardSquareAnalysisException.MSG,
                    err_code=BoardSquareAnalysisException.ERR_CODE,
                    ex=square_search.exception,
                )
            )
        # --- Route between the possible outcomes. ---#
        # Handle the case that, the square belongs to a different board.
        if board != square.board and square_search.is_empty:
            return RelationReport.no_relation()
        
        if len(square_search.payload) > 0 and square.board != board:
            return RelationReport.stale_link(primary=board)
        
        if len(square_search.payload) > 0 and square == board:
            return RelationReport.registration_missing(satellite=square)
        
        return RelationReport.bidirectional(primary=board, satellite=square)
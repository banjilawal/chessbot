# src/logic/board/analyzer/analyzer.py

"""
Module: logic.board.analyzer.analyzer
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.square import Square, SquareContext, SquareService
from logic.system import LoggingLevelRouter, RelationAnalyzer, RelationReport
from logic.board import Board, BoardSquareAnalyzerFailureException, BoardValidator


class BoardSquareRelationAnalyzer(RelationAnalyzer[Board, Square]):
    """
    Role:Reporting, Test for Relationship

    Responsibilities:
    1.  Test if whether a board-item tuple have either none, partial, or fully bidirectional relation
        between them.
    2.  If the testing was not completed send an exception chain to the caller.

    Super Class:
        *   RelationAnalyzer

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            candidate_primary: Board,
            candidate_satellite: Square,
            board_validator: BoardValidator = BoardValidator(),
            square_service: SquareService = SquareService(),
    ) -> RelationReport[Board, Square]:
        """
        # ACTION:
            1.  If either candidate fails its safety certification send the exception chain in the
                RelationReport.
            2.  Cast the candidate_primary to board instance; board and candidate_satellite to Square instance;
                item.
            3.  If the item.owner != owner they are not related. Else they are partially related.
            4.  If searching owner's squares for the satellite produces an error send the exception chain.
           5.  If the search produced aa match send a bidirectional report. Else send a partial relation report.
        # PARAMETERS:
            *   candidate_primary (Board)
            *   candidate_satellite (Square)
            *   board_validator (BoardValidator)
            *   square_service (SquareService)
        # RETURN:
            *   RelationReport[Board, Square] containing either
                *   No relation:
                *   On error: an Exception
        Raises:
            *   BoardValidationException
        """
        method = f"{cls.__name__}.analyze"
        
        # Handle the case that, the board is not secure.
        board_validation = board_validator.validate(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.analyzer_failure(
                BoardSquareAnalyzerFailureException(
                    msg=BoardSquareAnalyzerFailureException.MSG,
                    err_code=BoardSquareAnalyzerFailureException.ERR_CODE,
                    ex=board_validation.exception,
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Handle the case that, the square is unsecure.
        square_validation = square_service.validator.validate(candidate_satellite)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.analyzer_failure(
                BoardSquareAnalyzerFailureException(
                    msg=BoardSquareAnalyzerFailureException.MSG,
                    err_code=BoardSquareAnalyzerFailureException.ERR_CODE,
                    ex=square_validation.exception,
                )
            )
        square = cast(Square, square_validation.payload)
        
        # Handle the case that, the square belongs to a different board.
        if board != square.board:
            return RelationReport.no_relation()
        
        # --- Search the board's squares for the satellite-candidate. ---#
        square_search = board.squares.search(context=SquareContext(id=square.id))
        
        # Handle the case that, the search was aborted.
        if square_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.analyzer_failure(
                BoardSquareAnalyzerFailureException(
                    msg=BoardSquareAnalyzerFailureException.MSG,
                    err_code=BoardSquareAnalyzerFailureException.ERR_CODE,
                    ex=square_search.exception,
                )
            )
        # --- Route between the possible outcomes. ---#
        
        # Handle an empty search result.
        if square_search.is_empty:
            return RelationReport.registration_missing(satellite=square)
        
        # Handle nonempty search result.
        return RelationReport.bidirectional(primary=board, satellite=square)
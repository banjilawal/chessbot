# src/chess/board/item/analyzer/analyzer.py

"""
Module: chess.board.item.analyzer.analyzer
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.square import Square, SquareContext, SquareService
from chess.system import LoggingLevelRouter, RelationAnalyzer, RelationReport
from chess.board import Board, BoardSquareAnalysisException, BoardValidator


class BoardSquareRelationAnalyzer(RelationAnalyzer[Board, Square]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether a board-item tuple have either none, partial, or fully bidirectional relation
        between them.
    2.  If the testing was not completed send an exception chain to the caller.

    # PARENT:
        *   RelationAnalyzer

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

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
        # RAISES:
            *   BoardValidationFailedException
        """
        method = "BoardService.analyze"
        
        # Process the possible board_validation outcomes.
        board_validation = board_validator.validate(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    message=f"{method}: {BoardSquareAnalysisException.ERROR_CODE}",
                    ex=board_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Process the possible square_validation outcomes.
        square_validation = square_service.validator.validate(candidate_satellite)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    message=f"{method}: {BoardSquareAnalysisException.ERROR_CODE}",
                    ex=square_validation.exception
                )
            )
        square = cast(Square, square_validation.payload)
        
        # If the item is assigned to a different board it's not a satellite of the area. They are not related.
        if board != square.board:
            return RelationReport.not_related()
        
        # Search the board to find out if the item has a full or partial bidirectional relation with its board.
        square_search = board.squares.search(context=SquareContext(id=square.id))
        if square_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardSquareAnalysisException(
                    message=f"{method}: {BoardSquareAnalysisException.ERROR_CODE}",
                    ex=square_search.exception
                )
            )
        # On the empty search the item has not been added to the Board.
        if square_search.is_empty:
            return RelationReport.partial(satellite=square)
        # All other paths in the test chain have been exhausted. The roster-occupant tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=board, satellite=square)
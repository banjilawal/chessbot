# src/chess/board/occupant/analyzer/analyzer.py

"""
Module: chess.board.occupant.analyzer.analyzer
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.board import Board
from chess.token import Token
from chess.system import RelationAnalyzer


class BoardTokenRelationAnalyzer(RelationAnalyzer[Board, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether a board-occupant tuple have either none, partial, or fully bidirectional relation between them.
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
            candidate_satellite: Token,
            board_validator: BoardValidator = BoardValidator(),
            token_service: TokenService = TokenService(),
    ) -> RelationReport[Board, Token]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to board instance; board and candidate_satellite to Token instance; occupant.
        2.  If the occupant.owner != owner they are not related. Else they are partially related.
        3.  If searching owner's tokens for the satellite produces an error send the exception chain. If the search
            produced aa match send a bidirectional report. Else send a partial relation report.

        # PARAMETERS:
            *   candidate_primary (Board)
            *   candidate_satellite (Token)
            *   board_validator (BoardValidator)
            *   token_service (TokenService)

        # RETURN:
        RelationTest[Board, Token] containing either
            *   No relation:
            *   On error: an Exception

        # RAISES:
            *   BoardValidationException
        """
        method = "BoardService.analyze"
        
        # Process the possible board_validation outcomes.
        board_validation = board_validator.validate(candidate_primary)
        if board_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardTokenRelationAnalysisException(
                    message=f"{method}: {BoardTokenRelationAnalysisException.ERROR_CODE}",
                    ex=board_validation.exception
                )
            )
        # Just incase things aren't Liskovian on the candidate_primary, cast the validation payload instead,
        board = cast(Board, board_validation.payload)
        
        # Process the possible token_validation outcomes.
        token_validation = token_service.validator.validate(candidate_satellite)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardTokenRelationAnalysisException(
                    message=f"{method}: {BoardTokenRelationAnalysisException.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        token = cast(Token, token_validation.payload)
        
        # If the occupant is assigned to a different board it's not a satellite of the area. They are not related.
        if board != token.board:
            return RelationReport.not_related()
        
        # Search the board to find out if the occupant has a full or partial bidirectional relation with its board.
        token_search = board.tokens.search(context=TokenContext(id=token.id))
        if token_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                BoardTokenRelationAnalysisException(
                    message=f"{method}: {BoardTokenRelationAnalysisException.ERROR_CODE}",
                    ex=token_search.exception
                )
            )
        # On the empty search the occupant has not been added to the Board.
        if token_search.is_empty:
            return RelationReport.partial(satellite=token)
        # All other paths in the test chain have been exhausted. The roster-occupant tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=board, satellite=token)
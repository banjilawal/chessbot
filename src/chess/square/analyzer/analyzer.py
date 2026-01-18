# src/chess/square/analyzer/analyzer.py

"""
Module: chess.square.analyzer.analyzer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import cast

from chess.board import Board
from chess.square import Square, SquareTokenRelationAnalysisFailedException, SquareValidator
from chess.token import CombatantActivityState, CombatantToken, KingToken, Token, TokenBoardState, TokenService,
from chess.system import LoggingLevelRouter, RelationAnalyzer, RelationReport


class SquareTokenRelationAnalyzer(RelationAnalyzer[Square, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test if whether a square-token tuple have either none, partial, or fully bidirectional relation between them.
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
            candidate_primary: Square,
            candidate_satellite: Token,
            token_service: TokenService = TokenService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> RelationReport[Square, Token]:
        """
        # ACTION:
        1.  If either candidate fails its safety certification send the exception chain in the RelationReport. Else,
            cast the candidate_primary to square instance; square and candidate_satellite to Token instance; token.
        2.  If the token.owner != owner they are not related. Else they are partially related.
        3.  If searching owner's tokens for the satellite produces an error send the exception chain. If the search
            produced aa match send a bidirectional report. Else send a partial relation report.

        # PARAMETERS:
            *   candidate_primary (Square)
            *   candidate_satellite (Token)
            *   square_validator (SquareValidator)
            *   token_service (TokenService)

        # RETURN:
        RelationTest[Square, Token] containing either
            *   No relation:
            *   On error: an Exception

        # RAISES:
            *   SquareValidationFailedException
        """
        method = "SquareService.analyze"
        
        # Process the possible square_validation outcomes.
        square_validation = square_validator.validate(candidate_primary)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                SquareTokenRelationAnalysisFailedException(
                    message=f"{method}: {SquareTokenRelationAnalysisFailedException.ERROR_CODE}",
                    ex=square_validation.exception
                )
            )
        # Declare local square variable for additional testing and return.
        square = cast(Square, square_validation.payload)
        
        # Process the possible token_validation outcomes.
        token_validation = token_service.validator.validate(candidate_satellite)
        if token_validation.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                SquareTokenRelationAnalysisFailedException(
                    message=f"{method}: {SquareTokenRelationAnalysisFailedException.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Declare local token variable for additional testing and return.
        token = cast(Token, token_validation.payload)
        
        # --- Deal with cases where there is no relation between the square and token. ---#
        
        # If the token has not been placed on the board then, the square and token are not related.
        if token.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            return SquareTokenRelationReport.not_related()
        
        # If the square is empty then, the square and token are not related..
        if square.occupant != token and isinstance(token, KingToken) and token.current_position != square.coord:
            return RelationReport.not_related()
        if isinstance(token, KingToken):
            if square.occupant != token and square.coord != token.current_position:
                return SquareTokenRelationReport.not_related()
            if square.occupant == token and square.coord !=token.current_position:
                return SquareTokenRelationReport.square_not_submitted_lease_termination(primary=square, satellite=None)
            if square.occupant != token and square.coord == token.current_position:
                return SquareTokenRelationReport.token_not_registered_with_square(primary=None, satellite=token)
            return RelationReport.bidirectional(primary=square, satellite=token)
        
        if isinstance(token, CombatantToken):
            combatant = cast(CombatantToken, token)
            if square.occupant != token and square.coord != combatant.current_position:
                return SquareTokenRelationReport.not_related()
            if square.occupant != combatant and combatant.activity_state == CombatantActivityState.REGISTERED_HOSTAGE:
                return SquareTokenRelationReport.not_related()
            if square.occupant == combatant and square.coord != combatant.current_position:
                return SquareTokenRelationReport.lease_not_terminated(primary=square, satellite=None)
            if square.occupant == combatant and square.coord == combatant.current_position and combatant.activity_state != CombatantActivityState.FREE:
                return SquareTokenRelationReport.lease_not_terminated(primary=square, satellite=None)
            if square.occupant != token and combatant.activity_state != CombatantActivityState.FREE:
                return SquareTokenRelationReport.not_related()
            if square.occupant != token and combatant.activity_state == CombatantActivityState.FREE square.coord == token.current_position:
                return SquareTokenRelationReport.token_not_registered_with_square(primary=None, satellite=token)
            if square.occupant and combatant.activity_state == CombatantActivityState.FREE square.coord == token.current_position:
                return SquareTokenRelationReport.fully_bidirectional(primary=square, satellite=token)
        

        return RelationReport.failure(
            SquareTokenRelationAnalysisFailedException(
                message=f"{method}: {SquareTokenRelationAnalysisFailedException.DEFAULT_MESSAGE}",
                ex=SquareTokenAnalysisRouteException(
                    f"{method}: {SquareTokenRelationAnalysisFailedException.DEFAULT_MESSAGE}"
                )
            )
        )
        # --- Deal with cases where the square is ghostly occupied by the token. ---#
        
        
        
        # If square.occupant == square and token.current_position != square.coord and token.board_state = FORMED_ON_BARD
        if (
                square.occupant == token and square.coord != token.current_position and
                token.board_state == TokenBoardState.FORMED_ON_BOARD
        ):
            return TokenSquareRelationReport.square_not_submitted_lease_termination(primary=square, satellite=token)
        
        if (
                square.occupant == token and square.coord == token.current_position and
                (
                        token.board_state == TokenBoardState.FORMED_ON_BOARD or
                        (isinstance(token, CombatantToken) and token.activity_state != CombatantActivityState.FREE)
                )
        ):
            return TokenSquareRelationReport.square_not_submitted_lease_termination(primary=square, satellite=token)
        
        if
        if square.occupant == token and square.coord == token.current_position and isinstance(token, CombatantToken):
            combatant = cast(CombatantToken, token)
            if combatant.activity_state !=  CombatantActivityState.FREE:
                return TokenSquareRelationResult.square_not_submitted_lease_termination(primary=square, satellite=token)

            
        if
        
        # If the square and combatant_token have the same coord but the
        
        # Handle the case
        
        # If the token is assigned to a different square it's not a satellite of the area. They are not related.
        if square != token.square:
            return RelationReport.not_related()
        
        # Search the square to find out if the token has a full or partial bidirectional relation with its square.
        token_search = square.tokens.search(context=TokenContext(id=token.id))
        if token_search.is_failure:
            # Return the exception chain on failure.
            return RelationReport.failure(
                SquareTokenRelationAnalysisFailedException(
                    message=f"{method}: {SquareTokenRelationAnalysisFailedException.ERROR_CODE}",
                    ex=token_search.exception
                )
            )
        # On the empty search the token has not been added to the Square.
        if token_search.is_empty:
            return RelationReport.partial(satellite=token)
        # All other paths in the test chain have been exhausted. The roster-token tuple is fully bidirectional.
        return RelationReport.bidirectional(primary=square, satellite=token)
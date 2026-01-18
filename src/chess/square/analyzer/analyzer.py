# src/chess/square/analyzer/analyzer.py

"""
Module: chess.square.analyzer.analyzer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import cast

from chess.square import (
    Square, SquareTokenAnalysisFailedException, SquareTokenAnalysisRouteException,  SquareValidator
)
from chess.token import CombatantStatus, CombatantToken, KingToken, Token, TokenBoardState, TokenService
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
                SquareTokenAnalysisFailedException(
                    message=f"{method}: {SquareTokenAnalysisFailedException.ERROR_CODE}",
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
                SquareTokenAnalysisFailedException(
                    message=f"{method}: {SquareTokenAnalysisFailedException.ERROR_CODE}",
                    ex=token_validation.exception
                )
            )
        # Declare local token variable for additional testing and return.
        token = cast(Token, token_validation.payload)
        
        # --- Deal with cases that are not dependent on the subclass. ---#
        if (
                token.board_state == TokenBoardState.NEVER_BEEN_PLACED or
                square.occupant != token and square.coord != token.current_position
        ):
            return RelationReport.no_relation()
        
        if isinstance(token, KingToken):
            return cls._king_square_analysis(king=cast(KingToken, token), square=square)
        if isinstance(square, KingToken):
            return cls._combatant_square_analysis(king=cast(CombatantToken, token), square=square)
         
        return RelationReport.failure(
            SquareTokenAnalysisFailedException(
                message=f"{method}: {SquareTokenAnalysisFailedException.DEFAULT_MESSAGE}",
                ex=SquareTokenAnalysisRouteException(f"{method}: {SquareTokenAnalysisRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @LoggingLevelRouter.monitor
    def _combatant_square_analysis(self, combatant: CombatantToken, square: Square) -> RelationReport[Square, Token]:
        method = "SquareTokenRelationAnalyzer._token_square_analysis"
    
        # --- Neither the square nor the king share the same coord. (No transition event) ---#
        if square.occupant != combatant and square.coord != combatant.current_position:
            return RelationReport.no_relation()
        
        # --- The captured token has been transferred from the board to enemy_team.hostages. (No transition event) ---#
        if square.occupant != combatant and combatant.combat_status == CombatantStatus.REGISTERED_HOSTAGE:
            return RelationReport.no_relation()
        
        # --- The combatant occupies a different coord but is still set as the occupant (Evacuation event incomplete) ---#
        if (
                square.occupant == combatant and square.coord != combatant.current_position and
                combatant.combat_status == CombatantStatus.FREE
        ):
            return RelationReport.stale_link(primary=square)
        
        # --- The free combatant shares the coord but is not set as the occupant yet (Occupation event incomplete) ---#
        if (
                square.occupant != combatant and square.coord == combatant.current_position and
                combatant.combat_status == CombatantStatus.FREE
        ):
            return RelationReport.registration_missing(satellite=combatant)
        
        # --- The captive has not been removed from the square yet. (CaptiveTransfer event incomplete) ---#
        if square.occupant == combatant and combatant.combat_status == CombatantStatus.CAPTURE_ACTIVATED:
            return RelationReport.bidirectional(primary=square, satellite=combatant)
        
        # --- The free combatant and the square share the coord and the combatant is occupying a square. (No Transition event) ---#
        if (
                square.occupant == combatant and square.coord == combatant.current_position and
                combatant.combat_status == CombatantStatus.FREE
        ):
            return RelationReport.bidirectional(primary=square, satellite=combatant)
        
        return RelationReport.failure(
            SquareTokenAnalysisFailedException(
                message=f"{method}: {SquareTokenAnalysisFailedException.DEFAULT_MESSAGE}",
                ex=SquareTokenAnalysisRouteException(f"{method}: {SquareTokenAnalysisRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @LoggingLevelRouter.monitor
    def _king_square_analysis(self, king: KingToken, square: Square) -> RelationReport[Square, Token]:
        method = "SquareTokenRelationAnalyzer._king_square_analysis"
        
        # --- Neither the square nor the king share the same coord. (No transition event) ---#
        if square.occupant != king and square.coord != king.current_position:
            return RelationReport.no_relation()
        
        # --- The king occupies the same coord but is not set as the occupant. (Occupation event incomplete) ---#
        if square.occupant != king and square.coord == king.current_position:
            return RelationReport.registration_missing(satellite=king)
        
        # --- The king occupies a different coord but is still set as the occupant (Evacuation event incomplete) ---#
        if square.occupant == king and square.coord != king.current_position:
            return RelationReport.stale_link(primary=square)
        
        # --- Only case left is bidirectional. (No transition event) ---#
        return RelationReport.bidirectional(primary=square, satellite=king)
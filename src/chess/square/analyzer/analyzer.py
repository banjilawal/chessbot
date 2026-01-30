# src/chess/square/analyzer/analyzer.py

"""
Module: chess.square.analyzer.analyzer
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional, cast

from chess.square import (
    Square, SquareTokenAnalysisFailedException, SquareTokenAnalysisRouteException,  SquareValidator
)
from chess.token import CombatantToken, KingToken, Token, TokenService
from chess.system import LoggingLevelRouter, RelationAnalyzer, RelationReport


class SquareTokenRelationAnalyzer(RelationAnalyzer[Square, Token]):
    """
    # ROLE: Reporting, Test for Relationship

    # RESPONSIBILITIES:
    1.  Test what type of relationship a occupant and item have then issue a report of its analysis.
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
            1.  If either candidate fails its safety certification send the exception chain in the RelationReport.
            2.  Cast
                    *   candidate_primary to Square instance item
                    *   item and candidate_satellite to Token instance
            3.  Run tests between item and token_super class using super_token_square_analysis. If its able to
                discover no relation or stale link return RelationReport. Else, route to either
                    *   combatant_square_analyzer
                    *   king_square_analyzer.
            4.  If there is no analysis route for the predicate send an exception chain in the RelationReport.
                Else, the report will have a relation info.
        # PARAMETERS:
            *   candidate_primary (Square)
            *   candidate_satellite (Token)
            *   square_validator (SquareValidator)
            *   token_service (TokenService)
        # RETURN:
            *   RelationTest[Square, Token] containing either
                    * On Success:
                        - No relation:
                        - Stale link:
                        - Missing registration
                    - On Error:
                        - Exception
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
        # --- Declare local item and occupant variables for additional testing. ---#
        token = cast(Token, token_validation.payload)
        square = cast(Square, square_validation.payload)
        
        # Run tests cases which are independent of subclass type.
        super_token_square_analysis = cls._super_square_analysis(square=square, token=token)
        if super_token_square_analysis is not None:
            return super_token_square_analysis
        
        # --- If super_token-item analysis did not produce a result route subclass based analysis ---#
        
        # Run the analysis for a combatant.
        if isinstance(token, CombatantToken):
            return cls._combatant_square_analysis(square=square, combatant=cast(CombatantToken, token))
        # Run the analysis for a king.
        if isinstance(token, KingToken):
            return cls._king_square_analysis(square=square, token=cast(KingToken, token))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _super_square_analysis(
            cls,
            token: Token,
            square: Square,
    ) -> Optional[RelationReport[Square, Token]]:
        """
        # ACTION:
            1.  If it can be determined they have:
                    *   nothing in common
                    *   The item has a stale link
                Send the RelationReport to the caller. Else there is not enough information to determine the
                relation, send Null back to the caller.
        # PARAMETERS:
            *   item (Square)
            *   occupant (Token)
        # RETURN:
            *   None or RelationTest[Square, Token].
        # RAISES:
            None
        """
        method = "SquareTokenAnalyzer._type_independent_analysis"
        
        # --- The no-relation cases. ---#
        if (
                not token.has_been_formed or
                token.team.board != square.board or
                (square.occupant != token and square.coord != token.current_position)
        ):
            return RelationReport.no_relation()
        
        # --- The stale link case. ---#
        if square.occupant == token and square.coord != token.current_position:
            return RelationReport.stale_link(primary=square)
        
        # --- Token class does not have enough information to determine the relationship. ---#
        return None
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _combatant_square_analysis(
            cls,
            square: Square,
            combatant: CombatantToken,
    ) -> RelationReport[Square, Token]:
        """
        # ACTION:
            1.  If there is a predicate matching the conditions of the item and occupant return
                a RelationReport with that analysis. Else return an exception in the RelationReport.
        # PARAMETERS:
            *   item (Square)
            *   combatant (CombatantToken)
        # RETURN:
            *   RelationTest[Square, Token] containing either
                    * On Success:
                        - No relation:
                        - Stale link:
                        - Missing registration
                    - On Error:
                        - Exception
        # RAISES:
            *   SquareTokenAnalysisFailedException
            *   SquareTokenAnalysisRouteException
        """
        method = "SquareTokenRelationAnalyzer._combatant_square_analysis"
        
        # --- Combatant-specific, not related case. ---#
        if square.occupant != combatant and combatant.has_hostage_manifest:
            return RelationReport.no_relation()
        
        # --- Combatant not registered. ---#
        if (
                square.occupant != combatant and
                square.coord == combatant.current_position and
                combatant.is_active
        ):
            return RelationReport.registration_missing(satellite=combatant)
        
        # --- Combatant-specific bidirectional cases. ---#
        if (
                square.occupant == combatant and
                combatant.is_active or combatant.capture_is_activated
        ):
            RelationReport.bidirectional(primary=square, satellite=combatant)
        
        # Return the exception chain if a predicate doesn't have an analysis route.
        return RelationReport.failure(
            SquareTokenAnalysisFailedException(
                message=f"{method}: {SquareTokenAnalysisFailedException.DEFAULT_MESSAGE}",
                ex=SquareTokenAnalysisRouteException(
                    f"{method}: {SquareTokenAnalysisRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
    
    @LoggingLevelRouter.monitor
    def _king_square_analysis(
            self,
            square: Square,
            king: KingToken
    ) -> RelationReport[Square, Token]:
        """
        # ACTION:
            1.  If there is a predicate matching the conditions of the item and occupant return
                a RelationReport with that analysis. Else return an exception in the RelationReport.
        # PARAMETERS:
            *   item (Square)
            *   king (KingToken)
        # RETURN:
            *   RelationTest[Square, Token] containing either
                    * On Success:
                        - No relation:
                        - Stale link:
                        - Missing registration
                    - On Error:
                        - Exception
        # RAISES:
            *   SquareTokenAnalysisFailedException
            *   SquareTokenAnalysisRouteException
        """
        method = "SquareTokenRelationAnalyzer._king_square_analysis"
        
        # --- King not registered. ---#
        if square.occupant != king and square.coord == king.current_position:
            return RelationReport.registration_missing(satellite=king)
        
        # Return the exception chain if a predicate doesn't have an analysis route.
        return RelationReport.failure(
            SquareTokenAnalysisFailedException(
                message=f"{method}: {SquareTokenAnalysisFailedException.DEFAULT_MESSAGE}",
                ex=SquareTokenAnalysisRouteException(
                    f"{method}: {SquareTokenAnalysisRouteException.DEFAULT_MESSAGE}"
                )
            )
        )
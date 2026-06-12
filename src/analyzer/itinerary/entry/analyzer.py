# src/operation/square/entry/operation.py

"""
Module: operation.square.entry.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast


from util import LoggingLevelRouter
from validation import ItineraryValidator
from err import ItineraryAnalyzerException
from result import AnalysisResult, MethodResultType
from model import CombatantToken, Itinerary, KingToken
from report import (
    AttackItineraryApproval, BlockedItinerary, EnemyKingAttackItineraryApproval, ItineraryReport,
    PeaceItineraryApproval
)



class ItineraryAnalyzer:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square entry exception owner.
        2.  Preserve original and updated square data for rollbacks.
        3.  Ensure both the token and the squares are consistent throughout
            square entry lifecycle.

    Attributes:
    
    Provides:
        -   execute(
                itinerary: Itinerary,
                itinerary_validator: ItineraryValidator,
            ) -> AnalysisResult[ItineraryReport]:

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            itinerary: Itinerary,
            itinerary_validator: ItineraryValidator | None = None,
    ) -> AnalysisResult[ItineraryReport]:
        """
        Action:
            1.  Send the original square along with an exception chain in the validation result if:
                    -   The square or token are insecure.
                    -   The token is disabled
                    -   The token belongs to a different board.
                    -   The new token is being deployed to the wrong square.
                    -   The square is already occupied.
                    -   The square accepts the token but the token cannot update its position.
            2.  Otherwise, each updates its state.
            3.  Send the success result.
        Args:
            itinerary: Itinerary,
            itinerary_validator: ItineraryValidator
       Returns:
            AnalysisResult[ItineraryReport]
        Raises:
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if itinerary_validator is None:
            itinerary_validator = ItineraryValidator()
            
        # Handle the case that, the itinerary fails a validation check.
        validation_result = itinerary_validator.validate(itinerary)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                ItineraryAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryAnalyzerException.MSG,
                    err_code=ItineraryAnalyzerException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the destination is empty.
        if itinerary.destination.is_empty:
            return AnalysisResult.completed(
                PeaceItineraryApproval(
                    recipient=itinerary.token,
                    origin=itinerary.source,
                    destination=itinerary.destination,
                )
            )
        # Handle the case that, the destination is blocked by a friendly.
        destination = itinerary.destination
        
        if destination.is_occupied and not itinerary.token.is_enemy(destination.occupant):
            return AnalysisResult.completed(
                BlockedItinerary(
                    recipient=itinerary.token,
                    origin=itinerary.source,
                    blocked_destination=itinerary.destination,
                    friendly=itinerary.destination.occupant,
                )
            )
        if destination.is_occupied and itinerary.token.is_enemy(destination.occupant):
            if isinstance(destination.occupant, CombatantToken):
                enemy_combatant = cast(CombatantToken, destination.occupant)
                return AnalysisResult.completed(
                    AttackItineraryApproval(
                        recipient=itinerary.token,
                        origin=itinerary.source,
                        target_square=itinerary.destination,
                        enemy_combatant=enemy_combatant,
                    )
                )
            if isinstance(destination.occupant, KingToken):
                enemy_king = cast(KingToken, destination.occupant)
                return AnalysisResult.completed(
                    EnemyKingAttackItineraryApproval(
                        recipient=itinerary.token,
                        origin=itinerary.source,
                        target_square=itinerary.destination,
                        enemy_king=enemy_king,
                    )
                )
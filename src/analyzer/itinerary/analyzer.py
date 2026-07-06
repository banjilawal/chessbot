# src/analyzer/itinerary/analyzer.py

"""
Module: analyzer.itinerary.analyzer
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
    AttackApproval, BlockingReport, KingAttackApproval, ItineraryReport,
    ManeuverApproval
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
    def analyzer(
            cls,
            itinerary: Itinerary,
            itinerary_validator: ItineraryValidator | None = None,
    ) -> AnalysisResult[ItineraryReport]:
        """
        Action:
            1.  Send an exception chain in the validation result if the itinerary is flagged.
            2.  Otherwise, the analyzer produces one of the following products;
                    -   A ManeuverItineraryApproval
                    -   A BlockingReport
                    -   An AttackApprovalReport
                    -   A KingAttackApproval
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
        validation_result = itinerary_validator.execute(itinerary)
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
        # Handle the case that, the destination is not occupied.
        if itinerary.destination.is_empty:
            return AnalysisResult.completed(
                ManeuverApproval(
                    recipient=itinerary.token,
                    origin=itinerary.source,
                    destination=itinerary.destination,
                )
            )
        # Otherwise, produce a report for an occupied destination.
        return cls._occupied_destination_analyzer(itinerary)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _occupied_destination_analyzer(
            cls,
            itinerary: Itinerary
    ) -> AnalysisResult[ItineraryReport]:
        """
        Generate an itinerary report for an occupied destination.
        
        Action:
            1.  If the destination's occupant is friendly, send a BlockingReport. Otherwise,
                call _enemy_destination_analyzer to get either an AttackApproval or KingAttackApproval.
        Args:
            itinerary: Itinerary,
        Returns:
            AnalysisResult[ItineraryReport]
        Raises:
        """
        method = f"{cls.__name__}._occupied_destination_analyzer"
        
        destination_occupant = itinerary.destination.occupant
        # --- If the occupant is a friend send a BlockingReport. ---#
        if itinerary.token.is_friend(destination_occupant):
            return AnalysisResult.completed(
                BlockingReport(
                    id=itinerary.id,
                    recipient=itinerary.token,
                    origin=itinerary.source,
                    blocked_destination=itinerary.destination,
                    friendly=destination_occupant,
                )
            )
        # --- Otherwise, get the attack approvals. ---#
        return cls._enemy_destination_analyzer(itinerary=itinerary)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _enemy_destination_analyzer(
            cls,
            itinerary: Itinerary
    ) -> AnalysisResult[ItineraryReport]:
        """
        Generate an itinerary report for an enemy destination.
        Action:
            1.  If the enemy is an EnemyCombatant send an AttackApproval.
                Otherwise, send a KingAttackApproval.
        Args:
            itinerary: Itinerary,
        Returns:
            AnalysisResult[AttackApproval|KingAttackApproval]
        Raises:
        """
        method = f"{cls.__name__}._enemy_destination_analyzer"
        enemy = itinerary.destination.occupant
        
        # --- If the enemy is a combatant the work product is an AttackApproval. ---#
        if isinstance(enemy, CombatantToken):
            return AnalysisResult.completed(
                AttackApproval(
                    id=itinerary.id,
                    recipient=itinerary.token,
                    origin=itinerary.source,
                    target_square=itinerary.destination,
                    enemy_combatant=cast(CombatantToken, enemy),
                )
            )
        # --- Otherwise, a KingAttackApproval ---#
        return AnalysisResult.completed(
            KingAttackApproval(
                id=itinerary.id,
                recipient=itinerary.token,
                origin=itinerary.source,
                target_square=itinerary.destination,
                enemy_king=cast(KingToken, enemy),
            )
        )
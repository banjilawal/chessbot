# src/analyzer/friend/analyzer.py

"""
Module: analyzer.friend.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import Analyzer, EnemyCombatantStatusDetector, EnemyKingStatusDetector
from err import FriendshipAnalyzerException
from model import CombatantToken, KingToken, Token
from report import FriendshipReport, FriendshipStatus
from result import AnalysisResult
from util import LoggingLevelRouter
from validator import TokenValidator


class FriendshipAnalyzer(Analyzer):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner
        
    Responsibilities:
        1.  Token deployment exception owner.
        2.  Preserve original and updated data for rollbacks.
        3.  Ensure the token's integrity and consistency are maintained during the transaction.
    
    Attributes:
    
    Provides:
        -   def execute(
                    cls,
                    hunter: Token,
                    target: Token,
                    token_validator: TokenValidator,
                    king_status_detector: EnemyKingStatusDetector,
                    combatant_status_detector: EnemyCombatantStatusDetector,
            ) -> AnalysisResult[FriendshipReport
            
    Super Class:
        Analyzer
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            hunter: Token,
            target: Token,
            token_validator: TokenValidator | None = None,
            king_status_detector: EnemyKingStatusDetector | None = None,
            combatant_status_detector: EnemyCombatantStatusDetector | None = None,
    ) -> AnalysisResult[FriendshipReport]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send an exception chain in the AnalysisResult if any of the conditions occur.
                        -   The token fails a freedom check.
                        -   The opening square is not found in the token's board.
                        -   Searching the board is fails.
                        -   square has already been friended.
            2.  Otherwise, send the success result.
        Args:
            hunter: Token
            target: Token
            token_validator: TokenValidator
            king_status_detector: EnemyKingStatusDetector
            combatant_status_detector: EnemyCombatantStatusDetector
        Returns:
            AnalysisResult[FriendshipReport]
        Raises:
            FriendshipAnalyzerException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        if king_status_detector is None:
            king_status_detector = EnemyKingStatusDetector()
        if combatant_status_detector is None:
            combatant_status_detector = EnemyCombatantStatusDetector()
        
        # --- Perform analysis to see if the token is free. ---#
        for token in [hunter, target]:
            validation_result = token_validator.execute(candidate=token)
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return AnalysisResult.failure(
                    FriendshipAnalyzerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=FriendshipAnalyzerException.MSG,
                        err_code=FriendshipAnalyzerException.ERR_CODE,
                        ex=validation_result.exception,
                    )
                )
        if hunter.is_friend(target):
            return AnalysisResult.completed(
                FriendshipReport.friends(hunter=hunter, friend=target,)
            )
        
        if isinstance(target, KingToken):
            analysis_result = cls._process_enemy_king(
                hunter=hunter,
                king=cast(KingToken, target),
                king_status_detector=king_status_detector,
            )
            if analysis_result.is_failure:
                return AnalysisResult.failure(
                    FriendshipAnalyzerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=FriendshipAnalyzerException.MSG,
                        err_code=FriendshipAnalyzerException.ERR_CODE,
                        ex=analysis_result.exception,
                    )
                )
            return analysis_result
        
        analysis_result = cls._process_enemy_combatant(
            hunter=hunter,
            combatant=cast(CombatantToken, target),
            combatant_status_detector=combatant_status_detector,
        )
        if analysis_result.is_failure:
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=analysis_result.exception,
                )
            )
        # --- Send the work product ---#
        return analysis_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_enemy_king(
            cls,
            hunter: Token,
            king: KingToken,
            token_validator: TokenValidator,
            king_status_detector: EnemyKingStatusDetector,
    ) -> AnalysisResult[FriendshipReport]:
        method = f"{cls.__name__}._process_enemy_king"

        enemy_king_status_detection = king_status_detector.execute(
            king=king,
            token_validator=token_validator,
        )
        
        # Handle the case that, the king's friendship status cannot be detected.
        if enemy_king_status_detection.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=enemy_king_status_detection.exception,
                )
            )
        king_status = cast(FriendshipStatus, enemy_king_status_detection.payload)
        
        # Case: The enemy king is free.
        if king_status == FriendshipStatus.FREE_ENEMY_KING:
            return AnalysisResult.completed(
                FriendshipReport.free_enemy_king(
                    hunter=hunter,
                    enemy_king=king
                )
            )
        # Case: The enemy king is checkmated.
        if king_status == FriendshipStatus.CHECKMATED_ENEMY_KING:
            return AnalysisResult.completed(
                FriendshipReport.checkmated_enemy_king(
                    hunter=hunter,
                    enemy_king=king
                )
            )
        # Default Case: the king has not been deployed.
        return AnalysisResult.completed(
            FriendshipReport.undeployed_enemy_king(
                hunter=hunter,
                enemy_king=king
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _process_enemy_combatant(
            cls,
            hunter: Token,
            combatant: CombatantToken,
            token_validator: TokenValidator,
            combatant_status_detector: EnemyCombatantStatusDetector,
    ) -> AnalysisResult[FriendshipReport]:
        method = f"{cls.__name__}._process_enemy_combatant"
        
        enemy_combatant_status_detection = combatant_status_detector.execute(
            combatant=combatant,
            token_validator=token_validator,
        )
        
        # Handle the case that, the king's friendship status cannot be detected.
        if enemy_combatant_status_detection.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=enemy_combatant_status_detection.exception,
                )
            )
        combatant_status = cast(FriendshipStatus, enemy_combatant_status_detection.payload)
        
        # Case: The enemy king is free.
        if combatant_status == FriendshipStatus.FREE_ENEMY_COMBATANT:
            return AnalysisResult.completed(
                FriendshipReport.free_enemy_combatant(
                    hunter=hunter,
                    enemy_combatant=combatant
                )
            )
        # Case: The enemy combatant has been captured.
        if combatant_status == FriendshipStatus.ENEMY_PRISONER:
            return AnalysisResult.completed(
                FriendshipReport.enemy_prisoner(
                    hunter=hunter,
                    enemy_prisoner=combatant
                )
            )
        # Default Case: the combatant has not been deployed.
        return AnalysisResult.completed(
            FriendshipReport.undeployed_enemy_combatant(
                hunter=hunter,
                enemy_combatant=combatant
            )
        )
        
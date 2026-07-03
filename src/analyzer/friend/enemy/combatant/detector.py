# src/analyzer/friend/combatant/detector.py

"""
Module: analyzer.friend.combatant.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from err import EnemyCombatantAnalyzerException, TokenNullException
from model import CombatantToken
from report import FriendshipStatus
from result import Result
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validation import TokenValidator


class EnemyCombatantStatusDetector(Analyzer):
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
        -   execute(
                    token: Token,
                    token_validator: TokenFreedomAnalyzer,
            ) -> Result[FriendshipReport]
            
    Super Class:
        Analyzer
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            combatant: CombatantToken,
            toolkit: TokenToolkit | None = None,
            token_validator: TokenValidator | None = None,
    ) -> Result[FriendshipStatus]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send an exception chain in the Result if any of the conditions occur.
                        -   The token fails a freedom check.
                        -   The opening square is not found in the token's board.
                        -   Searching the board is fails.
                        -   square has already been friended.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            token_validator: TokenFreedomAnalyzer
        Returns:
            Result[FriendshipReport]
        Raises:
            EnemyCombatantAnalyzerException
            DuplicateTokenDeploymentException
            SquareNotFoundSearchException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        
        validation_result = token_validator.validate(
                candidate=combatant,
                toolkit=toolkit,
                null_exception=TokenNullException(),
            )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                EnemyCombatantAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=EnemyCombatantAnalyzerException.MSG,
                    err_code=EnemyCombatantAnalyzerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        if not isinstance(combatant, CombatantToken):
            # Send the exception chain on failure.
            return Result.failure(
                EnemyCombatantAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=EnemyCombatantAnalyzerException.MSG,
                    err_code=EnemyCombatantAnalyzerException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {CombatantToken} got {type(combatant).__class__.__name__} instead."
                    ),
                )
            )
        if combatant.is_active:
            return Result.success(FriendshipStatus.FREE_ENEMY_COMBATANT)
        if combatant.captor is not None:
            return Result.success(FriendshipStatus.ENEMY_PRISONERT)
        
        return Result.success(FriendshipStatus.UNDEPLOYED_ENEMY_COMBATANT)

        
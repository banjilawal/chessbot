# src/analyzer/friend/king/detector.py

"""
Module: analyzer.friend.king.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer
from err import EnemyKingAnalyzerException, TokenNullException
from model import KingToken
from report import FriendshipStatus
from result import Result
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validation import TokenValidator


class EnemyKingStatusDetector(Analyzer):
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
            king: KingToken,
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
            EnemyKingAnalyzerException
            DuplicateTokenDeploymentException
            SquareNotFoundSearchException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        
        validation_result = token_validator.validate(
                candidate=king,
                toolkit=toolkit,
                null_exception=TokenNullException(),
            )
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                EnemyKingAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=EnemyKingAnalyzerException.MSG,
                    err_code=EnemyKingAnalyzerException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        if not isinstance(king, KingToken):
            # Send the exception chain on failure.
            return Result.failure(
                EnemyKingAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=EnemyKingAnalyzerException.MSG,
                    err_code=EnemyKingAnalyzerException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {KingToken} got {type(king).__class__.__name__} instead."
                    ),
                )
            )
        if king.is_active or king.is_in_check:
            return Result.success(FriendshipStatus.FREE_ENEMY_KING)
        if king.is_checkmated:
            return Result.success(FriendshipStatus.CHECKMATED_ENEMY_KING)
        
        return Result.success(FriendshipStatus.UNDEPLOYED_ENEMY_KING)

        
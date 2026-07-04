# src/detection/home/detector.py

"""
Module: detection.home.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import HomeSquareDetectorException
from model import HomeSquare, SquareContext, Token
from result import Result
from util import LoggingLevelRouter
from validation import TokenValidator


class HomeSquareDetector:
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
            ) -> Result[HomeSquareClaimReport]
            
    Super Class:
        Analyzer
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_validator: TokenValidator | None = None,
    ) -> Result[HomeSquare]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send an exception chain in the Result if any of the conditions occur.
                        -   The token fails a freedom check.
                        -   The opening square is not found in the token's board.
                        -   Searching the board is fails.
                        -   square has already been claimed.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            token_validator: TokenFreedomAnalyzer
        Returns:
            Result[HomeSquareClaimReport]
        Raises:
            HomeSquareDetectorException
            DuplicateTokenDeploymentException
            SquareNotFoundSearchException
        """
        method = f"{cls.__class__.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        
        # --- Perform analysis to see if the token is free. ---#
        token_validator_result = token_validator.validate(token)
        
        # Handle the case that, the analysis is not completed.
        if token_validator_result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                HomeSquareDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareDetectorException.MSG,
                    err_code=HomeSquareDetectorException.ERR_CODE,
                    ex=token_validator_result.exception,
                )
            )
        # --- Search for the token's opening square. ---#
        board = token.team.board
        home_search_result = board.squares.search(
            context=SquareContext(id=token.home_square.id)
        )
        # Handle the case that, searching for the opening square is not completed.
        if home_search_result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                HomeSquareDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareDetectorException.MSG,
                    err_code=HomeSquareDetectorException.ERR_CODE,
                    ex=home_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if home_search_result.is_empty:
            # Send the exception chain on failure.
            return Result.failure(
                HomeSquareDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareDetectorException.MSG,
                    err_code=HomeSquareDetectorException.ERR_CODE,
                    ex=SquareNotFoundSearchException(
                        msg=SquareNotFoundSearchException.MSG,
                        err_code=SquareNotFoundSearchException.ERR_CODE,
                        var=f"opening_square:{token.home_square.name}",
                        val=token.home_square,
                    ),
                )
            )
        # --- Send the work product ---#
        return Result.success(cast(HomeSquare, home_search_result.payload[0]))
        
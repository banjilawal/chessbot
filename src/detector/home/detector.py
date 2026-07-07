# src/detector/home/detector.py

"""
Module: detector.home.detector
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from bootstrapper import HomeDetectorBootstrapper
from context import TokenHomeContext
from err import HomeSquareDetectorException
from model import HomeSquare
from result import Result
from util import LoggingLevelRouter


class TokenHomeDetector:
    """
    Role:
        - Transaction Worker
        - Search
        
    Responsibilities:
        1.  Find a token's home square.
    
    Attributes:
    
    Provides:
        -   execute(
                    token: Token,
                    token_validator: TokenFreedomAnalyzer,
            ) -> Result[HomeSquareClaimReport]
            
    Super Class:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            context: TokenHomeContext,
            bootstrapper: HomeDetectorBootstrapper | None = None,
    ) -> Result[HomeSquare]:
        """
        Find the HomeSquare from the context.
        
        Action:
            1.  If
        Args:
            context: TokenHomeContext,
            bootstrapper: HomeDetectorBootstrapper
        Returns:
            Result[HomeSquare]
        Raises:
            HomeSquareDetectorException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if bootstrapper is None:
            bootstrapper = HomeDetectorBootstrapper()
            
        result = bootstrapper.execute(context=context)
        # Handle the case that, the opening square is not found.
        if result.is_failure:
            # Send the exception chain on failure.
            return Result.failure(
                HomeSquareDetectorException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareDetectorException.MSG,
                    err_code=HomeSquareDetectorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product ---#
        return Result.success(cast(HomeSquare, result.payload[0]))
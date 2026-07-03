# src/analyzer/friend/analyzer.py

"""
Module: analyzer.friend.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import Analyzer, TokenReadinessAnalyzer
from err import (
    HomeSquareAlreadyFriendedException, FriendshipAnalyzerException, SquareNotFoundSearchException,
    TokenNullException
)
from model import OpeningSquare, SquareContext, Token
from report import FriendshipReport, TokenReadinessReport
from result import AnalysisResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validation import TokenValidator


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
        -   execute(
                    token: Token,
                    token_freedom_analyzer: TokenFreedomAnalyzer,
            ) -> AnalysisResult[FriendshipReport]
            
    Super Class:
        Analyzer
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            a: Token,
            b: Token,
            toolkit: TokenToolkit | None = None,
            token_validator: TokenValidator | None = None,
            token_freedom_analyzer: TokenReadinessAnalyzer | None = None,
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
            token: Token
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            AnalysisResult[FriendshipReport]
        Raises:
            FriendshipAnalyzerException
            DuplicateTokenDeploymentException
            SquareNotFoundSearchException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenReadinessAnalyzer()
        
        # --- Perform analysis to see if the token is free. ---#
        freedom_analysis_result = token_freedom_analyzer.analyze(token)
        
        for token in [a, b]:
            validation_result = token_validator.validate(
                candidate=token,
                toolkit=toolkit,
                null_exception=TokenNullException(),
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return AnalysisResult.failure(
                    FriendshipAnalyzerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=FriendshipAnalyzerException.MSG,
                        err_code=FriendshipAnalyzerException.ERR_CODE,
                        ex=freedom_analysis_result.exception,
                    )
                )
        if a.is_friend(b):
            
        
        # Handle the case that, the analysis is not completed.
        if freedom_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=freedom_analysis_result.exception,
                )
            )
        # Handle the case that, the token has already been deployed.
        report = cast(TokenReadinessReport, freedom_analysis_result.payload)
        if report.token_is_deployed:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=HomeSquareAlreadyFriendedException(
                        msg=HomeSquareAlreadyFriendedException.MSG,
                        err_code=HomeSquareAlreadyFriendedException.ERR_CODE,
                    ),
                )
            )
        # --- Start opening_square tests from the token's board. ---#
        board = token.team.board
        square_search_result = board.squares.search(
            context=SquareContext(id=token.opening_square.id)
        )
        # Handle the case that, searching for the opening square is not completed.
        if square_search_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=SquareNotFoundSearchException(
                        msg=SquareNotFoundSearchException.MSG,
                        err_code=SquareNotFoundSearchException.ERR_CODE,
                        var=f"opening_square:{token.opening_square.name}",
                        val=token.opening_square,
                    ),
                )
            )
        # Handle the case that, the opening square has already been friended as home by a token.
        home_square = cast(OpeningSquare, square_search_result.payload[0])
        if home_square.is_friended:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                FriendshipAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=FriendshipAnalyzerException.MSG,
                    err_code=FriendshipAnalyzerException.ERR_CODE,
                    ex=HomeSquareAlreadyFriendedException(
                        msg=HomeSquareAlreadyFriendedException.MSG,
                        err_code=HomeSquareAlreadyFriendedException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product ---#
        return AnalysisResult.completed(FriendshipReport(friendant=token, home_square=home_square))
        
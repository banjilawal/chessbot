# src/logic/token/service/operation/deployment/deployer.py

"""
Module: logic.token.service.operation.deployment.deployer
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations

from typing import cast

from analyzer import Analyzer, TokenFreedomAnalyzer
from err import HomeSquareAlreadyClaimedException, HomeSquareClaimAnalyzerException, SquareNotFoundSearchException
from model import OpeningSquare, SquareContext, Token
from report import HomeSquareClaimReport, TokenFreedomReport
from result import AnalysisResult, MethodResultType
from util import LoggingLevelRouter


class HomeSquareClaimAnalyzer(Analyzer[HomeSquareClaimReport]):
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
                    token_validator: TokenValidator,
            ) -> UpdateResult[Token]
            
        - _run_opening_square_tests(token: Token) -> SearchResult[List[Square]]
        
        - _square_visitation_process_work(
                    token: Token,
                    pre_update_token: Token,
                    opening_square: Square,
            ) -> UpdateResult[Token]
            
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_freedom_analyzer: TokenFreedomAnalyzer | None = None,
    ) -> AnalysisResult[HomeSquareClaimReport]:
        """
        Executes the deployment transaction.
        
        Action:
            1.  Send an exception chain in the AnalysisResult if any of the conditions occur.
                        -   The token fails a freedom check.
                        -   The opening square is not found in the token's board.
                        -   Searching the board is fails.
                        -   square has already been claimed.
            2.  Otherwise, send the success result.
        # Args:
            token: Token
            token_freedom_analyzer: TokenFreedomAnalyzer
        Returns:
            AnalysisResult[HomeSquareClaimReport]
        Raises:
            HomeSquareClaimAnalyzerException
            DuplicateTokenDeploymentException
            SquareNotFoundSearchException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if token_freedom_analyzer is None:
            token_freedom_analyzer = TokenFreedomAnalyzer()
        
        # --- Perform analysis to see if the token is free. ---#
        freedom_analysis_result = token_freedom_analyzer.analyze(token)
        
        # Handle the case that, the analysis is not completed.
        if freedom_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                HomeSquareClaimAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareClaimAnalyzerException.MSG,
                    err_code=HomeSquareClaimAnalyzerException.ERR_CODE,
                    ex=freedom_analysis_result.exception,
                )
            )
        # Handle the case that, the token has already been deployed.
        report = cast (TokenFreedomReport, freedom_analysis_result.payload)
        if report.token_is_deployed:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                HomeSquareClaimAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareClaimAnalyzerException.MSG,
                    err_code=HomeSquareClaimAnalyzerException.ERR_CODE,
                    ex=HomeSquareAlreadyClaimedException(
                        msg=HomeSquareAlreadyClaimedException.MSG,
                        err_code=HomeSquareAlreadyClaimedException.ERR_CODE,
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
                HomeSquareClaimAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareClaimAnalyzerException.MSG,
                    err_code=HomeSquareClaimAnalyzerException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                HomeSquareClaimAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareClaimAnalyzerException.MSG,
                    err_code=HomeSquareClaimAnalyzerException.ERR_CODE,
                    ex=SquareNotFoundSearchException(
                        msg=SquareNotFoundSearchException.MSG,
                        err_code=SquareNotFoundSearchException.ERR_CODE,
                        var=f"opening_square:{token.opening_square.name}",
                        val=token.opening_square,
                    ),
                )
            )
        # Handle the case that, the opening square has already been claimed as home by a token.
        opening_square = cast(OpeningSquare, square_search_result.payload[0])
        if opening_square.is_claimed:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                HomeSquareClaimAnalyzerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=HomeSquareClaimAnalyzerException.MSG,
                    err_code=HomeSquareClaimAnalyzerException.ERR_CODE,
                    ex=HomeSquareAlreadyClaimedException(
                        msg=HomeSquareAlreadyClaimedException.MSG,
                        err_code=HomeSquareAlreadyClaimedException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product ---#
        return AnalysisResult.success(
            HomeSquareClaimReport(claimant=token, opening_square=opening_square)
        )
        
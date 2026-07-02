# src/search/origin/searcher.py

"""
Module: search.origin/searcher
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import TokenReadinessAnalyzer
from err import (
    DisabledTokenException, TokenOriginSearcherException, TokenSearchHitConflictException,
    TokenSearchResultEmptyException
)
from model import SquareContext, Token
from report import TokenReadinessReport
from result import MethodResultType, SearchResult
from util import LoggingLevelRouter


class TokenOriginSearcher:
    """
    Role:
        - Search Worker
        - Integrity Maintenance

    Responsibilities:
        1.  Find the square a Token occupies on a Board.
        2.  Provides a token's origin for maneuver operations.
        3.  Provide debugging information for error cases which can occur during the search.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    readiness_analyzer: TokenReadinessAnalyzer,
            ) -> SearchResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            readiness_analyzer: TokenReadinessAnalyzer | None = None,
    ) -> SearchResult:
        """
        Find the source square a Token can move from.
        
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The token's readiness analysis is not completed.
                    -   The square search is not completed.
                    -   The token is disabled.
                    -   The token is not found on the board.
                    -   The search result indicates the token occupies more than one square.
            2.  Otherwise, send the success result.
        Args:
            token: Token,
            readiness_analyzer: TokenReadinessAnalyzer
        Returns:
            SearchResult
        Raises:
            DisabledTokenException
            TokenOriginSearcherException
            TokenSearchHitConflictException
            TokenSearchResultEmptyException
        """
        method =  f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if readiness_analyzer is None:
            readiness_analyzer = TokenReadinessAnalyzer()
        
        # --- Before doing anything else make sure the token can be used. ---#
        readiness_analysis_result = readiness_analyzer.analyze(token)
        
        # Handle the case that, the freedom
        if readiness_analysis_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                    ex=readiness_analysis_result.exception,
                )
            )
        # Handle the case that, the token is not ready for use.
        report = cast(TokenReadinessReport, readiness_analysis_result.payload)
        if report.token_is_not_ready:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                    ex=DisabledTokenException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=DisabledTokenException.MSG,
                        err_code=DisabledTokenException.ERR_CODE,
                    ),
                )
            )
        # --- After confirming the token is available find the square it occupies. ---#
        origin_search_result = token.team.board.squares.search(
            context=SquareContext(occupant=token)
        )
        
        # Handle the case that, the search is not completed.
        if origin_search_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                    ex=origin_search_result.exception,
                )
            )
        # Handle the case that, the token is not on the board.
        if origin_search_result.is_empty:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                    ex=TokenSearchResultEmptyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenSearchResultEmptyException.MSG,
                        err_code=TokenSearchResultEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the search contains more than one hit.
        if len(origin_search_result.payload) > 1:
            # Return the exception chain on failure
            return SearchResult.failure(
                exception=TokenOriginSearcherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginSearcherException.MSG,
                    err_code=TokenOriginSearcherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                    ex=TokenSearchHitConflictException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenSearchHitConflictException.MSG,
                        err_code=TokenSearchHitConflictException.ERR_CODE,
                    ),
                )
            )
        # --- Last possible case, Token's square has been found. Forward the work product. ---#
        return origin_search_result

    
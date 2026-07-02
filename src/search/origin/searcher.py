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
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a deletion.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
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
        Find the square a Token occupies on a Board.
        
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a deletion denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            item_id: int
            stack: TokenStackService
            square_validator: SquareValidator
            readiness_analyzer: TokenFreedomAnalyzer
        Returns:
            SearchResult
        Raises:
            TokenDeletePermitterException
            TokenStackFullException
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
        # --- After the token is available find where its on the board. ---#
        
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
        # --- Last possible case, Token's square has been found. Forward success result---#
        return origin_search_result

    
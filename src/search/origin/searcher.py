# src/search/origin/searcher.py

"""
Module: search.origin.searcher
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrap import OriginSearcherBootstrapper
from err import TokenOriginSearcherException
from model import Token
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
                    bootstrapper: OriginSearcherBootstrapper,
            ) -> SearchResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            target: Token,
            bootstrapper: OriginSearcherBootstrapper | None = None,
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
            target: Token,
            bootstrapper: OriginSearcherBootstrapper
        Returns:
            SearchResult
        Raises:
            DisabledTokenException
        """
        method =  f"{cls.__name__}.execute"
    
        # --- Supply any missing dependencies. ---#
        if bootstrapper is None:
            bootstrapper = OriginSearcherBootstrapper()
            
        search_result = bootstrapper.execute(target=target)
        if search_result.is_failure:
            # Handle the case that, the freedom
            if search_result.is_failure:
                # Return the exception chain on failure
                return SearchResult.failure(
                    exception=TokenOriginSearcherException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginSearcherException.MSG,
                        err_code=TokenOriginSearcherException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.SEARCH_RESULT,
                        ex=search_result.exception,
                    )
                )
        return search_result

    
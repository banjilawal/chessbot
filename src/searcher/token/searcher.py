# src/searcher/token/searcher.py

"""
Module: searcher.token.search
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenSearcherException
from permitter import TokenSearchPermitter
from request import SearchRequest
from result import SearchResult
from route import TokenSearchRouter
from util import LoggingLevelRouter


class TokenSearcher:
    _permitter: TokenSearchPermitter
    _router: TokenSearchRouter
    
    def __init__(
            self,
            permitter: TokenSearchPermitter | None = TokenSearchPermitter(),
            router: TokenSearchRouter | None = TokenSearchRouter(),
    ):
        self._permitter = permitter
        self._router = router
        
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchRequest) -> SearchResult:
        method = f"{self.__class__.__name__}.execute"


        permission = self._permitter.run(request=request)
        if permission.is_denied:
            return SearchResult.failure(
                TokenSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearcherException.MSG,
                    err_code=TokenSearcherException.ERR_CODE,
                    ex=permission.exception,
                )
            )
        search_result = self._router.route(request)
        if search_result.is_failure:
            return SearchResult.failure(
                TokenSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearcherException.MSG,
                    err_code=TokenSearcherException.ERR_CODE,
                    ex=search_result.exception,
                )
            )
        return search_result
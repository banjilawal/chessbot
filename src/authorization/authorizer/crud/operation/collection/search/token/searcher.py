# src/operation/collection/search/token/searcher.py

"""
Module: operation.collection.search.token.search
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from err import TokenSearcherException
from authorization.authorizer import TokenSearchAuthorizer
from client.exchange import SearchPermissionRequest
from artifcat import SearchResult
from transit.router import TokenSearchRouter
from util import LoggingLevelRouter


class TokenSearcher:
    _authorizer: TokenSearchAuthorizer
    _router: TokenSearchRouter
    
    def __init__(
            self,
            authorizer: TokenSearchAuthorizer | None = TokenSearchAuthorizer(),
            router: TokenSearchRouter | None = TokenSearchRouter(),
    ):
        self._authorizer = authorizer
        self._router = router
        
    @LoggingLevelRouter.monitor
    def execute(self, request: SearchPermissionRequest) -> SearchResult:
        method = f"{self.__class__.__name__}.execute"


        permission = self._authorizer.execute(request=request)
        if permission.is_denial:
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
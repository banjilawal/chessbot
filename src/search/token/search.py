# src/search/token/search.py

"""
Module: search.token.search
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from encodings import search_function
from typing import List

from database.coord.database import search
from err import TokenSearcherException
from model import Token, TokenQuery
from result import SearchResult
from route import TokenSearchRouter
from util import LoggingLevelRouter
from validation.query.validator import QueryValidator


class TokenSearcher:
    _query_validator: QueryValidator
    _search_router: TokenSearchRouter
    
    def __init__(
            self,
            query_validator: QueryValidator | None = None,
            search_router: TokenSearchRouter | None = None,
    ):
        self._query_validator = query_validator or QueryValidator()
        self._search_router = search_router or TokenSearchRouter()
        
    @LoggingLevelRouter.monitor
    def execute(self, query: TokenQuery) -> SearchResult[List[Token]]:
        method = f"{self.__class__.__name__}.search"
        query_validation_result = self._query_validator.validate(query)
        
        if query_validation_result.is_failure:
            return SearchResult.failure(
                TokenSearcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearcherException.MSG,
                    err_code=TokenSearcherException.ERR_CODE,
                    ex=query_validation_result.exception,
                )
            )
        search_result = self._search_router.route(query)
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
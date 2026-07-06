# src/logic/token/database/searcher/service/service.py

"""
Module: logic.token.database.searcher.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from system import LoggingLevelRouter, SearchMicroservice, SearchResult
from model.state.token import (
    Token, TokenContextService, TokenQuery, TokenQueryService, TokenSearchResourceHost,
    TokenSearchRouter, TokenSearchServiceException
)


class TokenSearchService(SearchMicroservice[Token]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Operations Provider

    Responsibilities:
        1.  Baremetal microservice for querying Tokens.

    Args:
        id: int
        name: str
        resource_host: TokenSearchResourceHost

    Provides:
        -  def search(context: TokenQuery) -> SearchResult[List[Token]]

    Super Class:
        SearchMicroservice
    """
    SERVICE_NAME = "TokenSearchService"
    _resource_host: TokenSearchResourceHost

    def __init__(
            self,
            name: str = SERVICE_NAME,
            resource_host: TokenSearchResourceHost = TokenSearchResourceHost(),
    ):
        """
        Args:
            id: int
            name: str
            resource_host: TokenSearchResourceHost
        """
        super().__init__(id=id, name=name)
        self._resource_host = resource_host
    
    @property
    def router(self) ->TokenSearchRouter:
        return self._resource_host.search_router
    
    @property
    def query_service(self) -> TokenQueryService:
        return self._resource_host.query_service
    
    @property
    def context_service(self) -> TokenContextService:
        return self._resource_host.context_service
    
    @LoggingLevelRouter.monitor
    def search(self, query: TokenQuery) -> SearchResult[List[Token]]:
        """
        Action:
            If the request is not completed send the exception in the SearchResult.
            Otherwise, send the success result.
        Args:
            query: TokenQuery
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenSearchServiceException
        """
        method = f"{self.__class__.__name__}.context"
        
        # --- Forward the request to the search_router. ---#
        search_result = self._resource_host.search_router.route(
            query=query,
            query_validator=self._resource_host.query_service.execute
        )
        # Handle the case that, the request was not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                TokenSearchServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenSearchServiceException.MSG,
                    err_code=TokenSearchServiceException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return search_result
    
    
# src/logic/token/database/search/service/microservice.py

"""
Module: logic.token.database.search.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.system import QueryService, IdFactory, LoggingLevelRouter, SearchResult
from logic.token import (
    Token, TokenContext, TokenContextService, TokenQueryServiceException, TokenSearchRouter
)

class TokenQueryService(QueryService[Token]):
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
        router: SearchRouter[T]
        context_service: IntegrityMicroService[Context[T]]

    Provides:
        -  query(data_set: List[Token], context: TokenContext) -> SearchResult[List[Token]]

    Super Class:
        QueryService
    """
    SERVICE_NAME = "TokenQueryService"
    _router: TokenSearchRouter
    _context_service: TokenContextService

    def __init__(
            self,
            name: str = SERVICE_NAME,
            router: TokenSearchRouter = TokenSearchRouter(),
            id: int = IdFactory.next_id(class_name="TokenQueryService"),
            context_service: TokenContextService =TokenContextService(),
    ):
        """
        Args:
            id: int
            name: str
            router: TokenSearchRouter
            context_service: TokenContextService
        """
        super().__init__(id=id, name=name)
        self._router = router
        self._context_service = context_service
    
    @property
    def router(self) ->TokenSearchRouter:
        return self._router
    
    @property
    def context_service(self) -> TokenContextService:
        return self._context_service
    
    @LoggingLevelRouter.monitor
    def query(self, data_set: List[Token], context: TokenContext) -> SearchResult[List[Token]]:
        """
        Action:
            If the request is not completed send the exception in the SearchResult.
            Otherwise, send the success result.
        Args:
            data_set: List[Token]
            context: TokenContext
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenQueryServiceException
        """
        method = f"{self.__class__.__name__}.query"
        
        # --- Forward the request to the search_router. ---#
        search_result = self._router.route(dataset=data_set, context=context)
        
        # Handle the case that, the request was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenQueryServiceException.MSG,
                    err_code=TokenQueryServiceException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return search_result
    
    
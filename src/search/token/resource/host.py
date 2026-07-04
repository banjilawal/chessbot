# src/logic/token/database/search/operation/controller.py

"""
Module: logic.token.database.search.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from model.state.token import TokenContextService, TokenQueryService, TokenSearchRouter


class TokenSearchResourceHost:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations TokenSearchService supports.
        
    Attributes:
        query_service: TokenQueryService
        search_router: TokenSearchRouter
        context_service: TokenContextService

    Provides:
    
    Super Class:
    """
    _query_service: TokenQueryService
    _search_router: TokenSearchRouter
    _context_service: TokenContextService
    
    def __init__(
            self,
            query_service: TokenQueryService = TokenQueryService(),
            search_router: TokenSearchRouter = TokenSearchRouter(),
            context_service: TokenContextService = TokenContextService(),
    ):
        """
        Args:
            query_service: TokenQueryService
            search_router: TokenSearchRouter
            context_service: TokenContextService
        """
        self._query_service = query_service
        self._search_router = search_router
        self._context_service = context_service
    
    @property
    def query_service(self) -> TokenQueryService:
        return self._query_service
    
    @property
    def search_router(self) -> TokenSearchRouter:
        return self._search_router
    
    @property
    def context_service(self) -> TokenContextService:
        return self._context_service
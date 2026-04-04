# src/logic/schema/database/search/operation/controller.py

"""
Module: logic.schema.database.search.operation.controller
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from catalog.schema import SchemaContextService, SchemaQueryService, SchemaSearchRouter


class SchemaSearchResourceHost:
    """
    Role:
        - Controller
        
    Responsibilities:
        1.  Provide a single entry point for operations SchemaLookupService supports.
        
    Attributes:
        query_service: SchemaQueryService
        search_router: SchemaSearchRouter
        context_service: SchemaContextService

    Provides:
    
    Super Class:
    """
    _query_service: SchemaQueryService
    _search_router: SchemaSearchRouter
    _context_service: SchemaContextService
    
    def __init__(
            self,
            query_service: SchemaQueryService = SchemaQueryService(),
            search_router: SchemaSearchRouter = SchemaSearchRouter(),
            context_service: SchemaContextService = SchemaContextService(),
    ):
        """
        Args:
            query_service: SchemaQueryService
            search_router: SchemaSearchRouter
            context_service: SchemaContextService
        """
        self._query_service = query_service
        self._search_router = search_router
        self._context_service = context_service
    
    @property
    def query_service(self) -> SchemaQueryService:
        return self._query_service
    
    @property
    def search_router(self) -> SchemaSearchRouter:
        return self._search_router
    
    @property
    def context_service(self) -> SchemaContextService:
        return self._context_service
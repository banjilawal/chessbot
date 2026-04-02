# src/logic/schema/database/search/service/microservice.py

"""
Module: logic.schema.database.search.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.system import LoggingLevelRouter, SearchMicroservice, SearchResult
from logic.schema import (
    Schema, SchemaContextService, SchemaQuery, SchemaQueryService, SchemaSearchResourceHost,
    SchemaSearchRouter, SchemaSearchServiceException
)


class SchemaSearchService(SearchMicroservice[Schema]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Operations Provider

    Responsibilities:
        1.  Baremetal microservice for querying Schemas.

    Args:
        id: int
        name: str
        resource_host: SchemaSearchResourceHost

    Provides:
        -  def search(context: SchemaQuery) -> SearchResult[List[Schema]]

    Super Class:
        SearchMicroservice
    """
    SERVICE_NAME = "SchemaSearchService"
    _resource_host: SchemaSearchResourceHost

    def __init__(
            self,
            name: str = SERVICE_NAME,
            resource_host: SchemaSearchResourceHost = SchemaSearchResourceHost(),
    ):
        """
        Args:
            id: int
            name: str
            resource_host: SchemaSearchResourceHost
        """
        super().__init__(id=id, name=name)
        self._resource_host = resource_host
    
    @property
    def router(self) ->SchemaSearchRouter:
        return self._resource_host.search_router
    
    @property
    def query_service(self) -> SchemaQueryService:
        return self._resource_host.query_service
    
    @property
    def context_service(self) -> SchemaContextService:
        return self._resource_host.context_service
    
    @LoggingLevelRouter.monitor
    def search(self, query: SchemaQuery) -> SearchResult[List[Schema]]:
        """
        Action:
            If the request is not completed send the exception in the SearchResult.
            Otherwise, send the success result.
        Args:
            query: SchemaQuery
        Returns:
            SearchResult[List[Schema]]
        Raises:
            SchemaSearchServiceException
        """
        method = f"{self.__class__.__name__}.context"
        
        # --- Forward the request to the search_router. ---#
        search_result = self._resource_host.search_router.route(
            query=query,
            query_validator=self._resource_host.query_service.validator
        )
        # Handle the case that, the request was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SchemaSearchServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SchemaSearchServiceException.MSG,
                    err_code=SchemaSearchServiceException.ERR_CODE,
                    ex=search_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return search_result
    
    
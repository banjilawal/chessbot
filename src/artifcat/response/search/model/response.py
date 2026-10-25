# src/artifact/response/search/model/response.py

"""
Module: artifact.response.search.model.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, SearchResponse, SearchResult
from exchange import ModelSearchRequest, Request
from domain import Model, ModelBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelSearchResponse(SearchResponse[T], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Model's search request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: SearchResult
        request: SearchRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[T]
        -   def valid_blueprint() -> Optional[ModelBlueprint[T]]

        -   def success(
                    request: Request,
                    result: SearchResult[T],
            ) -> SearchResponse[T]

        -   def failure(
                    request: Request,
                    result: SearchResult[T],
                    exception: Exception,
            ) -> SearchResponse[T]

    Super Class:
        SearchResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: ModelSearchRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: ModelSearchRequest[T],
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> SearchResult:
        return cast(SearchResult, super().result)
        
    @property
    def request(self) -> ModelSearchRequest[T]:
        return cast(ModelSearchRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ModelBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> ModelSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            ModelSearchRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=search_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: SearchResult,
            exception: Exception,
    ) -> ModelSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            ModelSearchRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )

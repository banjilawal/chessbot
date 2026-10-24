# src/artifact/response/search/struct/binder/response.py

"""
Module: artifact.response.search.struct.binder.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, SearchResponse, SearchResult
from domain import Binder, BinderBlueprint
from exchange import BinderSearchRequest, Request

T = TypeVar("T", bound="Binder")

class BinderSearchResponse(SearchResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Binder's search request-response cycle's data and state.

    Attributes:
        request: SearchRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_binder() -> Optional[T]
        -   def valid_blueprint() -> Optional[BinderBlueprint[T]]

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
            request: BinderSearchRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: BinderSearchRequest[T]
            exception:Optional[Exception]
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
    def request(self) -> BinderSearchRequest[T]:
        return cast(BinderSearchRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[BinderBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> BinderSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            BinderSearchRequest[T],
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
    ) -> BinderSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            BinderSearchRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )

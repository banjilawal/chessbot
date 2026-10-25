# src/artifact/response/search/response.py

"""
Module: artifact.response.search.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, SearchResult
from domain import Blueprint
from exchange import Request, SearchRequest

T = TypeVar("T",)

class SearchResponse(Response[SearchResult], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a search request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: SearchResult
        request: SearchRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

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
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: SearchRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult
            request: SearchRequest[T]
            exception: Optional[Exception]
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
    def request(self) -> SearchRequest[T]:
        return cast(SearchRequest[T], super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            (
                self.valid_model is not None or
                self.valid_blueprint is not None
            )
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[Blueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> SearchResponse[T]:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            SearchRequest[T],
            request,
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
    ) -> SearchResponse[T]:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            SearchRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )
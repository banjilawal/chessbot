# src/artifact/response/search/struct/register/response.py

"""
Module: artifact.response.search.struct.register.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, SearchResponse, SearchResult
from domain import Register, RegisterBlueprint
from exchange import RegisterSearchRequest, Request

T = TypeVar("T", bound="Register")

class RegisterSearchResponse(SearchResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Register's search request-response cycle's data and state.

    Attributes:
        request: SearchRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_register() -> Optional[T]
        -   def valid_blueprint() -> Optional[RegisterBlueprint[T]]

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
            request: RegisterSearchRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: RegisterSearchRequest[T]
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
    def request(self) -> RegisterSearchRequest[T]:
        return cast(RegisterSearchRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[RegisterBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> RegisterSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            RegisterSearchRequest[T],
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
    ) -> RegisterSearchResponse:
        # Downcast the request into a SearchRequest.
        search_request = cast(
            RegisterSearchRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )

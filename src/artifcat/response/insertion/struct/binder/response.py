# src/artifact/response/insertion/struct/binder/response.py

"""
Module: artifact.response.insertion.struct.binder.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, InsertionResponse, InsertionResult
from domain import Binder, BinderBlueprint
from exchange import BinderInsertionRequest, Request

T = TypeVar("T", bound="Binder")

class BinderInsertionResponse(InsertionResponse[T], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Binder's insertion request-response cycle's data and state.

    Attributes:
        request: InsertionRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_binder() -> Optional[T]
        -   def valid_blueprint() -> Optional[BinderBlueprint[T]]

        -   def success(
                    request: Request,
                    result: InsertionResult[T],
            ) -> InsertionResponse[T]

        -   def failure(
                    request: Request,
                    result: InsertionResult[T],
                    exception: Exception,
            ) -> InsertionResponse[T]

    Super Class:
        InsertionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: BinderInsertionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: BinderInsertionRequest[T]
            exception:Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> InsertionResult:
        return cast(InsertionResult, super().result)
        
    @property
    def request(self) -> BinderInsertionRequest[T]:
        return cast(BinderInsertionRequest[T], super().request)
    
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
            result: InsertionResult,
    ) -> BinderInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            BinderInsertionRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=insertion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: InsertionResult,
            exception: Exception,
    ) -> BinderInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            BinderInsertionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )

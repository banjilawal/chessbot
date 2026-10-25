# src/artifact/response/deletion/response.py

"""
Module: artifact.response.deletion.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, DeletionResult
from domain import Blueprint

T = TypeVar("T")

class DeletionResponse(Response[T], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a deletion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: DeletionResult
        request: DeletionRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(
                    request: Request,
                    result: DeletionResult[T],
            ) -> DeletionResponse[T]

        -   def failure(
                    request: Request,
                    result: DeletionResult[T],
                    exception: Exception,
            ) -> DeletionResponse[T]

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult[T],
            request: DeletionRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult
            request: DeletionRequest[T]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> DeletionResult[T]:
        return cast(DeletionResult, super().result)
        
    @property
    def request(self) -> DeletionRequest[T]:
        return cast(DeletionRequest[T], super().request)
    
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
            result: DeletionResult,
    ) -> DeletionResponse[T]:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            DeletionRequest[T],
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> DeletionResponse[T]:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            DeletionRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )
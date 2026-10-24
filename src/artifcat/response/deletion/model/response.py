# src/artifact/response/deletion/model/response.py

"""
Module: artifact.response.deletion.model.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, DeletionResponse, DeletionResult
from exchange import ModelDeletionRequest, Request
from domain import Model, ModelBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelDeletionResponse(DeletionResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Model's deletion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: DeletionResult
        request: DeletionRequest[T]
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
                    result: DeletionResult[T],
            ) -> DeletionResponse[T]

        -   def failure(
                    request: Request,
                    result: DeletionResult[T],
                    exception: Exception,
            ) -> DeletionResponse[T]

    Super Class:
        DeletionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: ModelDeletionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: ModelDeletionRequest[T],
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> DeletionResult:
        return cast(DeletionResult, super().result)
        
    @property
    def request(self) -> ModelDeletionRequest[T]:
        return cast(ModelDeletionRequest[T], super().request)
    
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
            result: DeletionResult,
    ) -> ModelDeletionResponse:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            ModelDeletionRequest[T],
            request
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
    ) -> ModelDeletionResponse:
        # Downcast the request into a DeletionRequest.
        deletion_request = cast(
            ModelDeletionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )

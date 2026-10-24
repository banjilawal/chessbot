# src/artifact/response/insertion/model/response.py

"""
Module: artifact.response.insertion.model.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, InsertionResponse, InsertionResult
from exchange import ModelInsertionRequest, Request
from domain import Model, ModelBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelInsertionResponse(InsertionResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Model's insertion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: InsertionResult
        request: InsertionRequest[T]
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
            request: ModelInsertionRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: ModelInsertionRequest[T],
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
    def request(self) -> ModelInsertionRequest[T]:
        return cast(ModelInsertionRequest[T], super().request)
    
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
            result: InsertionResult,
    ) -> ModelInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            ModelInsertionRequest[T],
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
    ) -> ModelInsertionResponse:
        # Downcast the request into a InsertionRequest.
        insertion_request = cast(
            ModelInsertionRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )

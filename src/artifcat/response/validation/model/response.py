# src/artifact/response/validation/model/response.py

"""
Module: artifact.response.validation.model.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from exchange import ModelValidationRequest
from domain import Model, ModelBlueprint


T = TypeVar("T", bound="ModelValidationRequest")

class ModelValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Model's validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult
        request: ValidationRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_model() -> Optional[T]
        -   def valid_blueprint() -> Optional[ModelBlueprint[T]]

        -   def success(request: T, result: ValidationResult[T]) -> ValidationResponse[T]

        -   def failure(request: T, exception: Exception) -> ValidationResponse[T]

    Super Class:
        ValidationResponse
    """
    
    def __init__(
            self,
            request: T,
            state: ResponseState,
            result: Optional[ValidationResult] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: ModelValidationRequest[T],
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[ValidationResult]:
        return cast(ValidationResult, super().result)
        
    @property
    def request(self) -> T:
        return cast(T, super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[Model]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ModelBlueprint]:
        pass
        
    @classmethod
    def success(cls, result: ValidationResult, request: T) -> ModelValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: T, exception: Exception) -> ModelValidationResponse:
        # Send a failure Response using the cast.
        return cls(
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )

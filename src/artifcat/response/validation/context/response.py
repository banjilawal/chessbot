# src/artifact/response/validation/context/response.py

"""
Module: artifact.response.validation.context.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from exchange import Request, ContextValidationRequest
from domain import Context, ContextBlueprint
from transit import ContextCarrier

T = TypeVar("T", bound="ContextValidationRequest")

class ContextValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a ContextValidation transaction.

    Attributes:
        request: T
        state: ResponseState
        result: Optional[ValidationResult]
        exception: Optional[Exception]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: ValidationResult, request: T) -> ContextValidationResponse[T]:
        -   def failure(request: T, exception: Exception) -> ContextValidationResponse[T]

    Super Class:
        ContextValidationResponse
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
            request: T,
            state: ResponseState
            result: ValidationResult,
            request: ContextValidationRequest[T],
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
    def valid_model(self) -> Optional[Context]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ContextBlueprint]:
        pass
    
    @property
    @abstractmethod
    def carrier(self) -> Optional[ContextCarrier]:
        pass
        
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> ContextValidationResponse:
        # Send a success Response using the cast.
        req = cast(T, request)
        return cls(
            result=result,
            request=req,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ContextValidationResponse:
        # Send a failure Response using the cast.
        req = cast(T, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )

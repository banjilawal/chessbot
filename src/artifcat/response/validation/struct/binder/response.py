# src/artifact/response/validation/struct/binder/response.py

"""
Module: artifact.response.validation.struct.binder.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from exchange import BinderValidationRequest, Request
from domain import ArchetypeBinder, BinderBlueprint
from transit import BinderCarrier

T = TypeVar("T", bound="BinderValidationRequest")

class BinderValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a BinderValidation transaction.

    Attributes:
        request: T
        state: ResponseState
        result: Optional[ValidationResult]
        exception: Optional[Exception]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: ValidationResult, request: Request) -> ValidationResponse[T]:
        -   def failure(request: Request, exception: Exception) -> ValidationResponse[T]

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
            request: T,
            state: ResponseState
            result: ValidationResult,
            request: BinderValidationRequest[T],
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
    def valid_model(self) -> Optional[ArchetypeBinder]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[BinderBlueprint]:
        pass
    
    @property
    @abstractmethod
    def carrier(self) -> Optional[BinderCarrier]:
        pass
        
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> BinderValidationResponse:
        # Send a success Response using the cast.
        req = cast(T, request)
        return cls(
            result=result,
            request=req,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> BinderValidationResponse:
        # Send a failure Response using the cast.
        req = cast(T, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )

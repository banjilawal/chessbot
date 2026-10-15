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
from domain import Binder, BinderBlueprint
from exchange import BinderValidationRequest, Request

T = TypeVar("T", bound="Binder")

class BinderValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Binder's validation request-response cycle's data and state.

    Attributes:
        request: ValidationRequest[T]
        exception: Optional[Exception]

    Provides:
        -   def valid_binder() -> Optional[T]
        -   def valid_blueprint() -> Optional[BinderBlueprint[T]]

        -   def success(
                    request: Request,
                    result: ValidationResult[T],
            ) -> ValidationResponse[T]

        -   def failure(
                    request: Request,
                    result: ValidationResult[T],
                    exception: Exception,
            ) -> ValidationResponse[T]

    Super Class:
        ValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: BinderValidationRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: BinderValidationRequest[T]
            exception:Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> ValidationResult:
        return cast(ValidationResult, super().result)
        
    @property
    def request(self) -> BinderValidationRequest[T]:
        return cast(BinderValidationRequest[T], super().request)
    
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
            result: ValidationResult,
    ) -> BinderValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            BinderValidationRequest[T],
            request
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=validation_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: ValidationResult,
            exception: Exception,
    ) -> BinderValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            BinderValidationRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )

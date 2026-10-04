# src/artifact/response/validation/structure/register/response.py

"""
Module: artifact.response.validation.register.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from domain import Register, RegisterBlueprint
from exchange import RegisterValidationRequest, Request
from transit import RegisterCarrier

T = TypeVar("T", bound="Register")

class RegisterValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Register's validation request-response cycle's data and state.

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
        
        -   def valid_register() -> Optional[T]
        -   def valid_blueprint() -> Optional[RegisterBlueprint[T]]

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
    _carrier: Optional[RegisterCarrier[T]]
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: RegisterValidationRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: RegisterValidationRequest[T]
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
    def request(self) -> RegisterValidationRequest[T]:
        return cast(RegisterValidationRequest[T], super().request)
    
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
            result: ValidationResult,
    ) -> RegisterValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            RegisterValidationRequest[T],
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
    ) -> RegisterValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            RegisterValidationRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )

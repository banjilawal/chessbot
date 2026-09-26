# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, ValidationResult
from client import Request, ValidationRequest

T = TypeVar("T",)

class ValidationResponse(Response[ValidationResult], ABC, Generic[T]):
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: ValidationRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult
            request: ValidationRequest[T]
            exception: Optional[Exception]
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
    def request(self) -> ValidationRequest[T]:
        return cast(ValidationRequest[T], super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            self.result.is_success and
            self._state == ResponseState.SUCCESS
        )

    @property
    def is_failure(self) -> bool:
        return (
            self._result.is_failure and
            self._state == ResponseState.FAILURE
        )
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> ValidationResponse[T]:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            ValidationRequest[T],
            request,
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
    ) -> ValidationResponse[T]:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            ValidationRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )
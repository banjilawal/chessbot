# src/artifact/response/validation/response.py

"""
Module: artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, ValidationResult
from domain import Blueprint
from exchange import Request, ValidationRequest
from transit import EntityCarrier

T = TypeVar("T", bound="ValidationRequest",)

class ValidationResponse(Response[ValidationResult], ABC, Generic[T]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a Validation transaction.

    Attributes:
        request: T
        state: ResponseState
        result: Optional[ValidationResult]
        exception: Optional[Exception]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: ValidationResult, request: T) -> ValidationResponse
        -   def failure(request: T, exception: Exception) -> ValidationResponse[

    Super Class:
        Response
    """
    def __init__(
            self,
            request: T,
            state: ResponseState,
            exception: Optional[Exception],
            result: Optional[ValidationResult],
    ):
        """
        Args:
            request: T
            state: ResponseState
            result: ValidationResult
            exception: Optional[Exception]
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
    def valid_model(self) -> Optional[Any]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[Blueprint]:
        pass
    
    @property
    @abstractmethod
    def carrier(self) -> Optional[EntityCarrier]:
        pass
        
    @classmethod
    def success(cls, result: ValidationResult, request: Request) -> ValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ValidationResponse:
        return cls(
            request=request,
            exception=exception,
            state=ResponseState.FAILURE,
        )
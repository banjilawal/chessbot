# src/artifact/response/validation/response.py

"""
Module: artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from domain import Structure, StructureBlueprint
from exchange import Request, StructureValidationRequest
from transit import StructureCarrier

T = TypeVar("T", bound="Structure")

class StructureValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Structure's validation request-response cycle's data and state.

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
        -   def valid_blueprint() -> Optional[StructureBlueprint[T]]

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
            request: StructureValidationRequest[T],
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult
            request: StructureValidationRequest[T]
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
    def request(self) -> StructureValidationRequest[T]:
        return cast(StructureValidationRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[Structure[T]]:
        pass
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[StructureBlueprint[T]]:
        pass
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> StructureValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            StructureValidationRequest[T],
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
    ) -> StructureValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            StructureValidationRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )

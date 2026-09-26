# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ResponseState, ValidationResponse, ValidationResult
from client import ModelValidationRequest, Request
from domain import Model, ModelBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelValidationResponse(ValidationResponse[T], ABC, Generic[T]):
    _carrier: Optional[ModelCarrier[T]]
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: ModelValidationRequest[T],
            exception:Optional[Exception],
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
    def result(self) -> ValidationResult:
        return cast(ValidationResult, super().result)
        
    @property
    def request(self) -> ModelValidationRequest[T]:
        return cast(ModelValidationRequest[T], super().request)
    
    @property
    @abstractmethod
    def valid_blueprint(self) -> Optional[ModelBlueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def valid_model(self) -> Optional[T]:
        pass
    
    @property
    def state(self) -> ResponseState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
            self.result.is_success and
            self._state == ResponseState.SUCCESS
        )

    @property
    def is_consistent(self) -> bool:
        if self.is_failure:
            return False
        if (
                self.valid_model is None and
                self.valid_blueprint is None
        ):
            return False
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.is_consistent

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
    ) -> ModelValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            ModelValidationRequest[T],
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
    ) -> ModelValidationResponse:
        # Downcast the request into a ValidationRequest.
        validation_request = cast(
            ModelValidationRequest[T],
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )

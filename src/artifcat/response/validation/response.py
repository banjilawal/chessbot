# src/client/artifact/response/validation/response.py

"""
Module: client.artifact.response.validation.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from artifcat import Response, ResponseState, ValidationResult
from client.request import ValidationRequest

T = TypeVar("T",)

class ValidationResponse(Response[ValidationResult], ABC, Generic[T]):
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: ValidationRequest[T],
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult,
            request: ValidationRequest[T],
        """
        super().__init__(state=state, result=result, request=request)
        
    @property
    def result(self) -> ValidationResult:
        return cast(ValidationResult, super().result)
        
    @property
    def request(self) -> ValidationRequest[T]:
        return cast(ValidationRequest[T], super().request)
    
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
    def is_failure(self) -> bool:
        return (
            self._result.is_failure and
            self._state == ResponseState.FAILURE
        )
        
    @classmethod
    def success(
            cls, 
            result: ValidationResult, 
            request: ValidationRequest[T],
    ) -> ValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls, 
            result: ValidationResult, 
            request: ValidationRequest[T],
    ) -> ValidationResponse:
        return cls(
            result=result,
            request=request,
            state=ResponseState.FAILURE,
        )
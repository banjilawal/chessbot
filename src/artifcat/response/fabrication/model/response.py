# src/artifact/response/fabrication/model/response.py

"""
Module: artifact.response.fabrication.model.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from artifcat import BuildResponse, BuildResult, ResponseState
from exchange import ModelBuildRequest, Request
from transit import ModelCarrier

T = TypeVar("T", bound="ModelBuildRequest",)

class ModelBuildResponse(BuildResponse[T], ABC, Generic[T]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a Build transaction.

    Attributes:
        request: T
        model: Optional[Model]
        carrier: Optional[ModelCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> BuildResponse
        -   def failure(request: Request, exception: Exception) -> BuildResponse

    Super Class:
        BuildResponse
    """
    def __init__(
            self,
            request: T,
            state: ResponseState,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            request: T
            state: ResponseState
            result: BuildResult
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[BuildResult]:
        return cast(BuildResult, super().result)
        
    @property
    def request(self) -> T:
        return cast(T, super().request)
    
    @property
    def is_success(self) -> bool:
        return super().is_success
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    @abstractmethod
    def model(self) -> Optional[Any]:
        pass
    
    @property
    @abstractmethod
    def carrier(self) -> Optional[ModelCarrier]:
        pass
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> BuildResponse:
        req = cast(T, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> BuildResponse:
        req = cast(T, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
# src/artifact/response/fabrication/response.py

"""
Module: artifact.response.fabrication.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, BuildResult
from exchange import Request, BuildRequest
from transit import EntityCarrier

T = TypeVar("T", bound="BuildRequest",)

class BuildResponse(Response[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a Build transaction.

    Attributes:
        request: T
        model: Optional[Any]
        carrier: Optional[EntityCarrier]
        is_success: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> BuildResponse
        -   def failure(request: Request, exception: Exception) -> BuildResponse

    Super Class:
        Response
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
        return (
                super().is_success and
                isinstance(self.result, BuildResult) and
                self.model is not None
        )

    @property
    @abstractmethod
    def model(self) -> Optional[Any]:
        pass
    
    @property
    @abstractmethod
    def carrier(self) -> Optional[EntityCarrier]:
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
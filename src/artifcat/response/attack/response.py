# src/artifact/response/attack/response.py

"""
Module: artifact.response.attack.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, AttackResult
from exchange import Request, AttackRequest

T = TypeVar("T", bound="AttackRequest")

class AttackResponse(Response[AttackResult], ABC, Generic[T]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a attack request-response cycle's data and state.

    Attributes:
        request: AttackRequest
        result: AttackResult

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: AttackResult, request: Request) -> AttackResponse
        -   def success(request: Request, exception: Exception) -> AttackResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            request: T,
            state: ResponseState,
            result: Optional[AttackResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            request: T
            state: ResponseState
            result: Optional[AttackResult]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[AttackResult]:
        return cast(AttackResult, super().result)
        
    @property
    def request(self) -> T:
        return cast(T, super().request)
    
    @property
    def is_success(self) -> bool:
        return super().is_success
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
        
    @classmethod
    def success(cls, result: AttackResult, request: Request) -> AttackResponse:
        # Send a success Response using the cast.
        req = cast(AttackRequest[T], request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> AttackResponse:
        # Downcast the request into a AttackRequest.
        req = cast(T, request)
        # Send a failure Response using the cast.
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
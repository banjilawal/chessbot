# src/artifact/response/attack/stalemate/response.py

"""
Module: artifact.response.attack.stalemate.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResponse, AttackResult, ResponseState
from domain import StalemateEncounter
from exchange import StalemateRequest, Request


class StalemateResponse(AttackResponse[StalemateRequest]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Stalemate's attack request-response cycle's data and state.

    Attributes:
        result: AttackResult
        request: StalemateRequest

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(result: AttackResult, request: Request) -> AttackResponse
        -   def failure(request:Request,  exception:Exception) -> AttackResponse

    Super Class:
        AttackResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: StalemateRequest,
            result: Optional[AttackResult] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: StalemateRequest
            result: Optional[AttackResult]
            exception:Optional[Exception]
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
    def request(self) -> StalemateRequest:
        return cast(StalemateRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return super().is_success and isinstance(self.request, StalemateRequest)
    
    @property
    def encounter(self) -> Optional[StalemateEncounter]:
        result = self.result
        if (
            result is None or
            result.is_failure or
            not isinstance(result, AttackResult)
        ):
            return None
        encounter = cast(StalemateEncounter, result.payload)
        return encounter
        
    @classmethod
    def success(cls, result: AttackResult, request: Request) -> StalemateResponse:
        # Send a success Response using the cast.
        req = cast(StalemateRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls,request: Request, exception: Exception) -> StalemateResponse:
        # Downcast the request
        req = cast(StalemateRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )

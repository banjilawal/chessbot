# src/artifact/response/attack/checkmate/response.py

"""
Module: artifact.response.attack.checkmate.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResponse, AttackResult, ResponseState
from domain import CheckmateEncounter
from exchange import CheckmateRequest, Request


class CheckmateResponse(AttackResponse[CheckmateRequest]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Checkmate's attack request-response cycle's data and state.

    Attributes:
        result: AttackResult
        request: CheckmateRequest

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
            request: CheckmateRequest,
            result: Optional[AttackResult] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: CheckmateRequest
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
    def request(self) -> CheckmateRequest:
        return cast(CheckmateRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return super().is_success and isinstance(self.request, CheckmateRequest)
    
    @property
    def encounter(self) -> Optional[CheckmateEncounter]:
        result = self.result
        if (
            result is None or
            result.is_failure or
            not isinstance(result, AttackResult)
        ):
            return None
        encounter = cast(CheckmateEncounter, result.payload)
        return encounter
        
    @classmethod
    def success(cls, result: AttackResult, request: Request) -> CheckmateResponse:
        # Send a success Response using the cast.
        req = cast(CheckmateRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls,request: Request, exception: Exception) -> CheckmateResponse:
        # Downcast the request.
        req = cast(CheckmateRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )

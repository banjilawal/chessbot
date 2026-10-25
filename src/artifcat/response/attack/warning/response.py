# src/artifact/response/attack/warning/response.py

"""
Module: artifact.response.attack.warning.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResponse, AttackResult, ResponseState
from domain import EncounterWarning
from exchange import WarningRequest, Request


class WarningResponse(AttackResponse[WarningRequest]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Warning's attack request-response cycle's data and state.

    Attributes:
        result: AttackResult
        request: WarningRequest

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
            request: WarningRequest,
            result: Optional[AttackResult] | None = None,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: WarningRequest
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
    def request(self) -> WarningRequest:
        return cast(WarningRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return super().is_success and isinstance(self.request, WarningRequest)
    
    @property
    def encounter(self) -> Optional[EncounterWarning]:
        result = self.result
        if (
            result is None or
            result.is_failure or
            not isinstance(result, AttackResult)
        ):
            return None
        encounter = cast(EncounterWarning, result.payload)
        return encounter
        
    @classmethod
    def success(cls, result: AttackResult, request: Request) -> WarningResponse:
        # Send a success Response using the cast.
        req = cast(WarningRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls,request: Request, exception: Exception) -> WarningResponse:
        # Downcast the request.
        req = cast(WarningRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )

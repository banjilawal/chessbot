# src/artifact/response/maneuver/response.py

"""
Module: artifact.response.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverResult, Response, ResponseState
from domain import Maneuver, PawnToken, Rank
from exchange import ManeuverRequest, Request


class ManeuverResponse(Response[ManeuverResult]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a Maneuver transaction.

    Attributes:
        request: ManeuverRequest
        result: Optional[ManeuverResult]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: ManeuverResult, request: Request) -> ManeuverResponse
        -   def failure(request: Request, exception: Exception) -> ManeuverResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            request: ManeuverRequest,
            exception: Optional[Exception] | None = None,
            result: Optional[ManeuverResult] | None = None,
    ):
        """
        Args:
            state: ResponseState
            request: ManeuverRequest
            exception: Optional[Exception]
            result: Optional[ManeuverResult]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[ManeuverResult]:
        return cast(ManeuverResult, super().result)
        
    @property
    def request(self) -> ManeuverRequest:
        return cast(ManeuverRequest, super().request)
    
    @property
    def successful_maneuver(self) -> Optional[Maneuver]:
        result = self.result
        if (
            result is None or
            result.is_failure or
            not isinstance(result, ManeuverResult)
        ):
            return None
        maneuver = cast(Maneuver, result.payload)
        return maneuver
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            isinstance(self.request, ManeuverRequest) and
            isinstance(self.result, ManeuverResult)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
        
    @classmethod
    def success(cls, result: ManeuverResult, request: Request) -> ManeuverResponse:
        req = cast(ManeuverRequest, request)
        return cls(
            result=result,
            request=req,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> ManeuverResponse:
        req = cast(ManeuverRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )
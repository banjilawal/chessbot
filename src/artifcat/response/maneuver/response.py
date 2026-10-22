# src/artifact/response/maneuver/response.py

"""
Module: artifact.response.maneuver.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Response, ResponseState, ManeuverResult
from domain import Token, Path
from exchange import Request, ManeuverRequest

class ManeuverResponse(Response[ManeuverResult]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a maneuver request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ManeuverResult
        request: ManeuverRequest
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(
                    request: Request,
                    result: ManeuverResult,
            ) -> ManeuverResponse

        -   def failure(
                    request: Request,
                    result: ManeuverResult,
                    exception: Exception,
            ) -> ManeuverResponse

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: ManeuverResult,
            request: ManeuverRequest,
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: ManeuverResult
            request: ManeuverRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> ManeuverResult:
        return cast(ManeuverResult, super().result)
        
    @property
    def request(self) -> ManeuverRequest:
        return cast(ManeuverRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            self.traveler is not None and
            self.path is not None
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def traveler(self) -> Optional[Token]:
        if self.is_failure:
            return None
        request = self.request
        return request.traveler
    
    @property
    def path(self) -> Optional[Path]:
        if self.is_failure:
            return None
        request = self.request
        return request.path
        
    @classmethod
    def success(
            cls,
            request: Request,
            result: ManeuverResult,
    ) -> ManeuverResponse:
        # Downcast the request into a ManeuverRequest.
        maneuver_request = cast(
            ManeuverRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=maneuver_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: ManeuverResult,
            exception: Exception,
    ) -> ManeuverResponse:
        # Downcast the request into a ManeuverRequest.
        maneuver_request = cast(
            ManeuverRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=maneuver_request,
            state=ResponseState.FAILURE,
        )
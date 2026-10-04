# src/artifact/response/fabrication/response.py

"""
Module: artifact.response.fabrication.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import Response, ResponseState, BuildResult
from exchange import Request, BuildRequest

T = TypeVar("T",)

class BuildResponse(Response[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a build request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: BuildResult
        request: BuildRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(
                    request: Request,
                    result: BuildResult[T],
            ) -> BuildResponse[T]

        -   def failure(
                    request: Request,
                    result: BuildResult[T],
                    exception: Exception,
            ) -> BuildResponse[T]

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: BuildResult,
            request: BuildRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: BuildRequest[T]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> BuildResult:
        return cast(BuildResult, super().result)
        
    @property
    def request(self) -> BuildRequest[T]:
        return cast(BuildRequest[T], super().request)
    
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
            request: Request,
            result: BuildResult,
    ) -> BuildResponse[T]:
        # Downcast the request into a BuildRequest.
        fabrication_request = cast(
            BuildRequest[T],
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=fabrication_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: BuildResult,
            exception: Exception,
    ) -> BuildResponse[T]:
        # Downcast the request into a BuildRequest.
        fabrication_request = cast(
            BuildRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=fabrication_request,
            state=ResponseState.FAILURE,
        )
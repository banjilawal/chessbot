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
from domain import Encounter
from exchange import Request, AttackRequest

T = TypeVar("T", bound="Encounter")

class AttackResponse(Response[T], ABC, Generic[T]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a attack request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: AttackResult
        request: AttackRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool

        -   def success(
                    request: Request,
                    result: AttackResult[T],
            ) -> AttackResponse[T]

        -   def failure(
                    request: Request,
                    result: AttackResult[T],
                    exception: Exception,
            ) -> AttackResponse[T]

    Super Class:
        Response
    """
    def __init__(
            self,
            state: ResponseState,
            result: AttackResult[T],
            request: AttackRequest[T],
            exception: Optional[Exception],
    ):
        """
        Args:
            state: ResponseState
            result: AttackResult
            request: AttackRequest[T]
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> AttackResult:
        return cast(AttackResult, super().result)
        
    @property
    def request(self) -> AttackRequest[T]:
        return cast(AttackRequest[T], super().request)
    
    @property
    def is_success(self) -> bool:
        return (
            super().is_success and
            (
                self.valid_model is not None or
                self.valid_blueprint is not None
            )
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
        
    @classmethod
    def success(
            cls,
            request: Request[T],
            result: AttackResult[T],
    ) -> AttackResponse:
        # Send a success Response using the cast.
        return cls(
            result=result[T],
            request=request[T],
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request[T],
            result: AttackResult[T],
            exception: Exception,
    ) -> AttackResponse[T]:
        # Downcast the request into a AttackRequest.
        attack_request = cast(
            AttackRequest[T],
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=attack_request,
            state=ResponseState.FAILURE,
        )
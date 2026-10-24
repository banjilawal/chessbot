# src/artifact/response/attack/kill/response.py

"""
Module: artifact.response.attack.kill.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackResponse, KillResult, ResponseState
from domain import KillEncounter
from exchange import KillRequest


class KillResponse(AttackResponse[KillEncounter]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Kill's attack request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: KillAttack
        request: AttackRequest[T]
        exception: Optional[Exception]

    Provides:
        -   is_success: bool
        -   is_failure: bool
        -   is_consistent: bool
        -   is_not_consistent: bool
        
        -   def valid_kill() -> Optional[T]
        -   def valid_blueprint() -> Optional[KillBlueprint[T]]

        -   def success(
                    request: Request,
                    result: KillAttack[T],
            ) -> AttackResponse[T]

        -   def failure(
                    request: Request,
                    result: KillAttack[T],
                    exception: Exception,
            ) -> AttackResponse[T]

    Super Class:
        AttackResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: KillResult,
            request: KillRequest,
            exception:Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: KillAttack,
            request: KillAttackRequest,
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> KillResult:
        return cast(KillResult, super().result)
        
    @property
    def request(self) -> KillRequest:
        return cast(KillRequest, super().request)
        
    @classmethod
    def success(
            request: KillRequest,
            result: KillResult,
    ) -> KillResponse:
        # Send a success Response using the cast.
        return cls(
            request=request,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: KillRequest,
            result: KillAttack,
            exception: Exception,
    ) -> KillResponse:
        # Downcast the request into a AttackRequest.
        attack_request = cast(
            KillAttackRequest,
            request
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=attack_request,
            state=ResponseState.FAILURE,
        )

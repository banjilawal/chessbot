# src/artifact/result/authorizable/promotion/result.py

"""
Module: artfifact.result.authorizable.promotion.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizableResult, ResultState
from domain import PawnToken


class PromotionResult(AuthorizableResult[PawnToken]):
    """
    Role:
        - Data Transport
        - Error Transport

    Responsibilities:
        1.  Contains details of a Promotion transaction.

    Attributes:
        exception: Optional[Exception]
        payload: Optional[PawnToken]
        state: resultState
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: PawnToken) -> PromotionResult
        -   def failure(exception: Exception) -> PromotionResult
        -   def timed_out(cls, exception: Exception) -> PromotionResult:

    Super Class:
        AuthorizableResult
    """
    _state: ResultState
    
    def __init__(
            self,
            state: ResultState,
            payload: Optional[PawnToken] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: resultState
            payload: Optional[PawnToken]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use promotion methods instead of direct constructor."""
        self._state = state
    
    @property
    def payload(self) -> Optional[PawnToken]:
        return cast(PawnToken, super().payload)
    
    @property
    def is_success(self) -> bool:
        return (
            self.payload is not None and
            self.exception is None and
            self.state == ResultState.SUCCESS and
            isinstance(self.payload, PawnToken)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.success
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: PawnToken) -> PromotionResult:
        return cls(
            payload=payload,
            state=ResultState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> PromotionResult:
        return cls(
            exception=exception,
            state=ResultState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> PromotionResult:
        return cls(
            exception=exception,
            state=ResultState.TIMED_OUT,
        )
# src/artifact/result/authorizable/promotion/result.py

"""
Module: artfifact.result.authorizable.promotion.result
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import Authorizable, ResultState, Result
from domain import Model, PawnToken


T = TypeVar("T", bound="Model")

class AuthorizableResult(Result[T], Authorizable, ABC, Generic[T]):
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
        Result
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
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use promotion methods instead of direct constructor."""
        self._state = state
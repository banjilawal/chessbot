# src/result/build/result.py

"""
Module: result.build.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from result import Result

T = TypeVar("T")


class BuildResult(Result[T], Generic[T]):
    """
    Role:
        -   Data Transport
        -   Error Transport

    Responsibilities:
        1.  Contains the outcome of a build transaction.

    Attributes:
        exception: Optional[Exception]
        state: buildState
        payload: Optional[T]
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> Result[T]
        -   def failure(exception: Exception) -> Result[T]

    Super Class:
        Result
    """
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use build methods instead of direct constructor."""
    
    @classmethod
    def success(cls, payload: T) -> BuildResult[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> BuildResult[T]:
        return cls(exception=exception)
# src/result/build/result.py

"""
Module: result.build.result
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from result import BuildState, Result


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
        payload: Optional[T]
        state: buildState
        is_timed_out: bool
        is_success: bool
        is_failure: bool

    Provides:
        -   def success(payload: T) -> BuildResult
        -   def failure(exception: Exception) -> BuildResult
        -   def timed_out(cls, exception: Exception) -> BuildResult:

    Super Class:
        Result
    """
    _state: BuildState
    
    def __init__(
            self,
            state: BuildState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
    ):
        """
        Args:
            state: buildState
            payload: Optional[T]
            exception: Optional[Exception]
        """
        super().__init__(
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state
    
    @property
    def state(self) -> BuildState:
        return self._state
        
    @property
    def is_success(self) -> bool:
        return not self.is_failure
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == BuildState.FAILURE or
                self._state == BuildState.TIMED_OUT
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == BuildState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> BuildResult:
        return cls(
            payload=payload,
            state=BuildState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> BuildResult:
        return cls(
            exception=exception,
            state=BuildState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> BuildResult:
        return cls(
            exception=exception,
            state=BuildState.TIMED_OUT,
        )
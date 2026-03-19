# src/logic/system/computation/result.py

"""
Module: logic.system.computation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from logic.system import ComputationState, Result

T = TypeVar("T")

class ComputationResult(Result[T], Generic[T]):
    """
    Role:Messanger, Data Transport Object, Error Transport Object.

    Responsibilities:
    1.  Send the outcome of a calculation to the caller.
    2.  Enforcing mutual exclusion. A ComputationResult can either carry payload or exception. Not both.

    Super Class:
        *   DataResult

    Provides:

    # LOCAL ATTRIBUTES:
        *   state (ComputationState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _state: ComputationState
    
    def __init__(
            self,
            state: ComputationState,
            exception: Optional[Exception] = None,
            payload: Optional[T] = None,
    ):
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use build methods instead of direct constructor."""
        self._state = state

    @property
    def is_success(self) -> bool:
        return (
                self.payload is not None and
                self.exception is None and
                self._state == ComputationState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ComputationState.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.payload is None and
                self.exception is not None and
                self._state == ComputationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> ComputationResult[T]:
        return cls(
            payload=payload,
            exception=None,
            state=ComputationState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, exception: Exception) -> ComputationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationState.FAILURE,
        )
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ComputationResult[T]:
        return cls(
            payload=None,
            exception=exception,
            state=ComputationState.TIMED_OUT,
        )

    

    




# src/chess/square/occupation/result.py

"""
Module: chess.square.occupation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system import Result, OccupationResult, OccupationState
from chess.token.model import Token

T = TypeVar("T")


class OccupationResult(Result[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a occupation to the caller.
    2.  Enforcing mutual exclusion. A OccupationResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (OccupationState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _state: OccupationState
    _occupier: Optional[Token]
    
    def __init__(self, state: OccupationState, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.result"
        self._state = state
    
    @property
    def state(self) -> OccupationState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self.exception is None and
                self.payload is not None and
                self._state == OccupationState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == OccupationState.FAILURE
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == OccupationState.EMPTY
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == OccupationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> OccupationResult:
        return cls(state=OccupationState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> OccupationResult:
        return cls(state=OccupationState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> OccupationResult:
        return cls(state=OccupationState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> OccupationResult:
        return cls(state=OccupationState.EMPTY)
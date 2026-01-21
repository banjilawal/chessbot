# src/chess/system/data/result/deletion/result.py

"""
Module: chess.system.data.result.deletion.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system import DataResult, DeletionResult, DeletionState, DataResultState

T = TypeVar("T")


class DeletionResult(DataResult[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a deletion to the caller.
    2.  Enforcing mutual exclusion. A DeletionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (DeletionState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    def __init__(
            self,
            state: DataResultState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None
    ):
        super().__init__(
            state=state,
            payload=payload,
            exception=exception
        )
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.result"
    
    @property
    def is_success(self) -> bool:
        return (
                self.exception is None and
                self.payload is not None and
                self._state == DeletionState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == DeletionState.FAILURE
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == DeletionState.EMPTY
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == DeletionState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> DeletionResult:
        return cls(state=DeletionState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> DeletionResult:
        return cls(state=DeletionState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> DeletionResult:
        return cls(state=DeletionState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> DeletionResult:
        return cls(state=DeletionState.EMPTY)


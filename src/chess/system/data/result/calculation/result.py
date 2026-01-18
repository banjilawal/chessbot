# src/chess/system/data/result/calculation/result.py

"""
Module: chess.system.data.result.calculation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar, cast

from chess.system import (
    DataResult, CalculationResult, CalculationState, EmptyDataResultException, NotImplementedException
)

T = TypeVar("T")

class CalculationResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a calculation to the caller.
    2.  Enforcing mutual exclusion. A CalculationResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (CalculationState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    _state: CalculationState
    
    def __init__(
            self,
            state: CalculationState,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=payload, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.result"
        self._state = state
    
    @property
    def state(self) -> CalculationState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self.exception is None and
                self.payload is not None and
                self._state == CalculationState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == CalculationState.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                self._state == CalculationState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: int|bool) -> CalculationResult:
        return cls(state=CalculationState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> CalculationResult:
        return cls(state=CalculationState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> CalculationResult:
        return cls(state=CalculationState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> CalculationResult:
        method = "CalculationResult.empty"
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )

    

    




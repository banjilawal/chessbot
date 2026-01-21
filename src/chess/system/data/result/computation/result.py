# src/chess/system/data/result/calculation/result.py

"""
Module: chess.system.data.result.calculation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar, cast

from chess.system import (
    DataResult, ComputationResult, CalculationState, EmptyDataResultException, NotImplementedException,
    UnsupportedEmptyComputationResultException
)

T = TypeVar("T")

class ComputationResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a calculation to the caller.
    2.  Enforcing mutual exclusion. A ComputationResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (CalculationState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    
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
    def success(cls, payload: T) -> ComputationResult[T]:
        return cls(state=CalculationState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> ComputationResult[T]:
        return cls(state=CalculationState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> ComputationResult[T]:
        return cls(state=CalculationState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> ComputationResult[T]:
        method = "ComputationResult.empty"
        return cls(
            UnsupportedEmptyComputationResultException(
                f"{method}: {UnsupportedEmptyComputationResultException.DEFAULT_MESSAGE}"
            )
        )

    

    




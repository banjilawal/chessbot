# src/chess/system/data/result/insertion/result.py

"""
Module: chess.system.data.result.insertion.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar, cast

from chess.system import DataResult, InsertionResult, EmptyDataResultException, NotImplementedException, ResultState

T = TypeVar("T")


class InsertionResult(DataResult[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a insertion to the caller.
    2.  Enforcing mutual exclusion. A InsertionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   state (InsertionState)

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    def __init__(
            self,
            state: ResultState,
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
                ResultState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                ResultState.FAILURE
        )
    
    @property
    def is_timed_out(self) -> bool:
        return (
                self.exception is not None and
                self.payload is None and
                ResultState.TIMED_OUT
        )
    
    @classmethod
    def success(cls, payload: T) -> InsertionResult:
        return cls(state=ResultState.SUCCESS, payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> InsertionResult:
        return cls(state=ResultState.FAILURE, exception=exception)
    
    @classmethod
    def timed_out(cls, exception: Exception) -> InsertionResult:
        return cls(state=ResultState.TIMED_OUT, exception=exception)
    
    @classmethod
    def empty(cls) -> InsertionResult:
        method = "InsertionResult.empty"
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )




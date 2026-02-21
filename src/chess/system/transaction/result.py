# src/chess/system/transaction/result.py

"""
Module: chess.system.transaction.result
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0
"""

from typing import Optional, cast

from chess.system import (
    Event, MethodNotImplementedException, Result, RollbackException, TransactionState, TransactionResult
)


class TransactionResult(Result[Event]):
    """"""
    _checkpoint: Event
    _state: TransactionState
    _exception: Optional[Exception]
    
    def __init__(
            self,
            checkpoint: Event,
            state: TransactionState,
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=checkpoint, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._state = state
    
    @property
    def checkpoint(self) -> Event:
        return cast(Event, self.payload)
    
    @property
    def state(self) -> TransactionState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self.exception is None and self._state == TransactionState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self._state == TransactionState.FAILURE or self._state == TransactionState.ROLLED_BACK
        )
    
    @property
    def is_rolled_back(self) -> bool:
        return self.exception is not None and self._state == TransactionState.ROLLED_BACK
    
    @property
    def is_timed_out(self) -> bool:
        return self.exception is not None and self._state == TransactionState.TIMED_OUT
    
    @classmethod
    def success(cls, checkpoint) -> TransactionResult:
        return cls(checkpoint, TransactionState.SUCCESS)
    
    @classmethod
    def errored(cls, checkpoint: Event, exception: Exception) -> TransactionResult:
        return cls(checkpoint, TransactionState.FAILURE, exception)
    
    @classmethod
    def rolled_back(cls, checkpoint: Event, rollback_exception: RollbackException) -> TransactionResult:
        return cls(checkpoint, TransactionState.ROLLED_BACK, rollback_exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "TransactionResult.empty"
        return Result(
            exception=MethodNotImplementedException(
                f"{method}: {MethodNotImplementedException.DEFAULT_MESSAGE}. TransactionResult must "
                f"always have an event in the payload. It cannot be empty."
            )
        )

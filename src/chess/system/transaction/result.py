# src/chess/system/transaction/result.py

"""
Module: `chess.system.transaction.result`
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0
"""

from typing import Optional, cast

from chess.system import (
    Event, NotImplementedException, Result, RollbackException, TransactionState, TransactionResult
)


class TransactionResult(Result[Event]):
    """"""
    _event_update: Event
    _transaction_state: TransactionState
    _exception: Optional[Exception]
    
    def __init__(
            self,
            event_update: Event,
            transaction_state: TransactionState,
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=event_update, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.__init__"
        self._transaction_state = transaction_state
    
    @property
    def event_update(self) -> Event:
        return cast(Event, self.payload)
    
    @property
    def transaction_state(self) -> Optional[TransactionState]:
        return self._transaction_state
    
    def is_success(self) -> bool:
        return (
                self.exception is None and self.payload is not None and
                self._transaction_state == TransactionState.SUCCESS
        )
    
    def is_failure(self) -> bool:
        return (
                self.exception is not None and
                self._transaction_state == TransactionState.FAILURE or
                self._transaction_state == TransactionState.ROLLED_BACK
        )
    
    def is_rolled_back(self) -> bool:
        return self.exception is not None and self._transaction_state == TransactionState.ROLLED_BACK
    
    def is_timed_out(self) -> bool:
        return self.exception is not None and self._transaction_state == TransactionState.TIMED_OUT
    
    @classmethod
    def success(cls, event_update) -> TransactionResult:
        return cls(event_update, TransactionState.SUCCESS)
    
    @classmethod
    def errored(cls, event_update: Event, exception: Exception) -> TransactionResult:
        return cls(event_update, TransactionState.FAILURE, exception)
    
    @classmethod
    def rolled_back(cls, event_update: Event, rollback_exception: RollbackException) -> TransactionResult:
        return cls(event_update, TransactionState.ROLLED_BACK, rollback_exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "TransactionResult.empty"
        return Result(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. TransactionResult must "
                f"always have an event in the payload. It cannot be empty."
            )
        )

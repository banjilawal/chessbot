# src/chess/system/transfer/result.py

"""
Module: chess.system.transfer.result
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system.transfer import TransferResultState

S = TypeVar("S")
R = TypeVar("R")


class TransferResult(Generic[R, S]):
    """
    
    """
    _sender: S
    _recipient: Optional[R]
    _state: TransferResultState
    _exception: Optional[Exception]
    
    def result(
            self,
            checkpoint: Event,
            state: TransactionState,
            exception: Optional[Exception] = None
    ):
        super().result(payload=checkpoint, exception=exception)
        """INTERNAL: Use factory methods instead of direct constructor."""
        method = "TransactionResult.result"
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
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. TransactionResult must "
                f"always have an event in the payload. It cannot be empty."
            )
        )

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
    
    def __init__(
            self,
            sender: S,
            state: TransferResultState,
            recipient: Optional[R] = None,
            exception: Optional[Exception] = None
    ):
        method = "TransferResult.__init__"
        self._state = state
        self._sender = sender
        self._recipient = recipient
        self._exception = exception
    
    @property
    def sender(self) -> S:
        return self._sender
    
    @property
    def recipient(self) -> R:
        return self._recipient
    
    @property
    def state(self) -> TransferResultState:
        return self._state
    
    @property
    def is_success(self) -> bool:
        return (
                self._sender is not None and
                self._recipient is not None and
                self._exception is None and
                self._state == TransferResultState.SUCCESS
        )
    
    @property
    def is_failure(self) -> bool:
        return (
                self._sender is not None and
                self._recipient is None and
                self._exception is not None and
                self._state != TransferResultState.SUCCESS
        )
    
    @property
    def is_rolled_back(self) -> bool:
        return (
                self._sender is not None and
                self._recipient is not None and
                self._exception is not None and
                self._state != TransferResultState.ROLLED_BACK
        )
    
    @classmethod
    def success(cls, sender: S, recipient: R) -> TransferResult[S, R]:
        return cls(
            sender=sender,
            recipient=recipient,
            state=TransferResultState.SUCCESS
        )
    
    @classmethod
    def failure(cls, sender: S, exception: Exception) -> TransferResult[S, R]:
        return cls(
            sender=sender,
            exception=exception,
            state=TransferResultState.FAILURE
        )
    
    @classmethod
    def rollback(cls, sender: S, recipient: R, exception: Exception) -> TransferResult[S, R]:
        return cls(
            sender=sender,
            recipient=recipient,
            exception=exception,
            state=TransferResultState.ROLLED_BACK
        )
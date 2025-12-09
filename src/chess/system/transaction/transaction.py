# src/chess/system/transaction/transaction.py

"""
Module: chess.system.transaction.transaction
Author: Banji Lawal
Created: 2025-08-11
"""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod
from chess.system import LoggingLevelRouter, TransactionResult, TransactionState

V = TypeVar("V", bound="Event")


class Transaction(ABC, Generic[V]):
    """"""
    _event: V
    _state: TransactionState
    
    @LoggingLevelRouter.monitor
    def __init__(self, event: V):
        self._event = event
        self._state = TransactionState.RUNNING
    
    @property
    def event(self) -> V:
        return self._event
    
    @property
    def state(self) -> TransactionState:
        return self._state
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self) -> TransactionResult:
        """
        # ACTION:
        Fire a process from the event.
    
        # PARAMETERS:
        None
        
        # RETURNS:
        TransactionResult
    
    
        # RAISES:
            * TransactionException
        """
        pass

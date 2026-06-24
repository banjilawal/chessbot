# src/model/transaction/model.py

"""
Module: model.transaction.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from event import Event
from model import TransactionState
from report import Report


class Transaction:
    """
    Role:
        -   Model
        -   Addressing
        -   Stateful Data Holder

    Responsibilities:
        1.  Maps a Coord to a approvalable, occupyable checkpoint location.
        2.  Space on Checkpoint a Token can occupy.
        3.  Metadata about a reference on the Checkpoint.
    
    Attributes:
        id: int
        approval: Report
        checkpoint: Event
        state: TransactionState
        
    Provides:

    Super Class:
    """
    _id: int
    _approval: Report
    _checkpoint: Event
    _state: TransactionState
    
    def __init__(self, id: int, approval: Report, checkpoint: Event):
        """
        Args:
            id: int
            approval: Report
            checkpoint: Event
        """
        self._id = id
        self._approval = approval
        self._checkpoint = checkpoint
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def approval(self) -> Report:
        return self._approval
    
    @property
    def checkpoint(self) -> Event:
        return self._checkpoint
    
    @property
    def state(self) -> TransactionState:
        return self._state
    
    @state.setter
    def state(self, state: TransactionState):
        self._state = state
   
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Transaction):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)

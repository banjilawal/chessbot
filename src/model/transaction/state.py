# src/model/transaction/state.py

"""
Module: model.transaction.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class TransactionState(Enum):
    """
    Role:
        -   State Descriptor

    Responsibilities:
        1.  Indicates if the transaction can be visited.
        
    Provides

    Super Class:
        Enum
    """
    RUNNING = auto(),
    SUCCESS = auto(),
    FAILURE = auto(),
    TIMED_OUT = auto(),
    ROLLED_BACK = auto()
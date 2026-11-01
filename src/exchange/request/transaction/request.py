# src/exchange/request/transaction/request.py

"""
Module: exchange.request.transaction.equest
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import TransactionResult

R = TypeVar("R", bound="TransactionResult")


class TransactionRequest(ABC, Generic[R]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides information an Authorizer needs to execute a client's job.

     Attributes:
        id: int
        candidate: T

     Provides:
     
     Super Class:
     """
    _id: int
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        self._id = id
        
    @property
    def id(self) -> int:
        return self._id
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TransactionRequest):
            return self.id == other.id
        return False
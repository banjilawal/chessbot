# src/request/transaction/computation/request.py

"""
Module: request.transaction.computation.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import ComputationResult
from exchange import TransactionRequest

R = TypeVar("R", bound="ComputationResult")
T = TypeVar("T")

class ComputationRequest(TransactionRequest[R], ABC, Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
         id: int

     Provides:

     Super Class:
        TransactionRequest
     """
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        super().__init__(id)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ComputationRequest):
            return self.id == other.id
        return False
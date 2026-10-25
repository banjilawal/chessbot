# src/exchange/request/transaction//crud/insertion/request.py

"""
Module: exchange.request.transaction.crud.insertion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import InsertionResult
from exchange import CrudRequest

T = TypeVar("T")

class InsertionRequest(CrudRequest[InsertionResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide insertion job details.

     Attributes:
         id: int

     Provides:

     Super Class:
        CrudRequest
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
        if isinstance(other, InsertionRequest):
            return self.id == other.id
        return False
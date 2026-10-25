# src/exchange/request/crud/request.py

"""
Module: exchange.request.crud.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import CrudResult
from exchange import Request

T = TypeVar("T", bound="CrudResult")

class CrudRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a CrudWorker details about a job.

     Attributes:
         id: int

     Provides:

     Super Class:
        Request
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
        if isinstance(other, CrudRequest):
            return self.id == other.id
        return False
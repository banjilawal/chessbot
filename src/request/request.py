# src/request/request.py

"""
Module: request.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T", bound="Operation")


class Request(ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the Operation lifecycle.

     Attributes:
         id: int

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
        if isinstance(other, Request):
            return self._id == other.id
        return False
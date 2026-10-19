# src/exchange/request/request.py

"""
Module: exchange.request.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import Result
from exchange import Request

T = TypeVar("T", bound="Result")


class AuthorizationRequest(Request[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a job.

     Attributes:

     Provides:
     
     Super Class:
        Request
     """
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        super().__init__(id=id)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationRequest):
            return self._id == other.id
        return False
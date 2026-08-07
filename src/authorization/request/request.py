# src/authorization/request/request.py

"""
Module: authorization.request.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC


class Request(ABC):
    """
     Role:
         -  Request

     Responsibilities:
         1. Provide information to get permission to run an operation.

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
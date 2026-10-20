# src/authorization/form/form.py

"""
Module: authorization.form.form
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from exchange import Request

T = TypeVar("T", bound="Request")


class AuthorizationForm(ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about a job.

     Attributes:
         id: int
         request: T

     Provides:
     
     Super Class:
     """
    _id: int
    _applicant: T
    
    def __init__(self, id: int, operation: T):
        """
        Args:
            id: int
            operation: T
        """
        self._id = id
        self._operation = operation
        
    @property
    def id(self) -> int:
        return self.id
    
    @property
    def operation(self) -> T:
        return self._operation
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AuthorizationForm):
            return self._id == other.id
        return False
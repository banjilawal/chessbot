# src/exchange/request/permission/request.py

"""
Module: exchange.request.permission.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from exchange import TransactionRequest

T = TypeVar("T", bound="TransactionRequest")


class PermissionRequest(ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a CrudAuthorizer with job details.

     Attributes:
         id: int
         authorization_applicant: T

     Provides:

     Super Class:
     """
    _id: int
    _authorization_applicant: T
    
    def __init__(self, id: int, authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: T
        """
        self._id = id
        self._authorization_applicant = authorization_applicant
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def authorization_applicant(self) -> T:
        return self._authorization_applicant
    
    @abstractmethod
    def __eq__(self, other) -> bool:
        pass
    
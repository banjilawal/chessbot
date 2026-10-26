# src/exchange/permissionRequest/permission/crud/insertion/push/request.py

"""
Module: exchange.request.permission.crud.insertion.push.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from exchange import InsertionPermissionRequest

T = TypeVar("T")


class PushPermissionRequest(
    InsertionPermissionRequest[T], ABC, Generic[T]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a PushAuthorizer with job details.

     Attributes:
         id: int
         candidate: : T

     Provides:

     Super Class:
        InsertionPermissionRequest
     """
    
    def __init__(self, id: int, candidate: T):
        """
        Args:
            id: int
            candidate: T
        """
        super().__init__(id, candidate=candidate)
    
    @property
    def payload(self) -> T:
        return cast(T, super().payload)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PushPermissionRequest):
            return self.id == other.id
        return False
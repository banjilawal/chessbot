# src/exchange/permissionRequest/permission/crud/request.py

"""
Module: exchange.request.permission.crud.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from exchange import CrudRequest, PermissionRequest

T = TypeVar("T", bound="CrudRequest")


class CrudPermissionRequest(
    PermissionRequest[T], ABC, Generic[T]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a CrudAuthorizer with job details.

     Attributes:
         id: int
         candidate: : T

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int, candidate: T):
        """
        Args:
            id: int
            candidate: T
        """
        super().__init__(id, candidate=candidate)
    
    @property
    def candidate(self) -> T:
        return cast(T, super().candidate)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CrudPermissionRequest):
            return self.id == other.id
        return False
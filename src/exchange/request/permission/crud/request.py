# src/exchange/permissionRequest/permission/crud/request.py

"""
Module: exchange.request.permission.crud.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T", bound="CrudRequest")

class CrudPermissionRequest(PermissionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a CrudWorker details about a job.

     Attributes:
         id: int

     Provides:

     Super Class:
        PermissionRequest
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
        if isinstance(other, CrudPermissionRequest):
            return self.id == other.id
        return False
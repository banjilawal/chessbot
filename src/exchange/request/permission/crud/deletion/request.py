# src/exchange/permissionRequest/permission/crud/delete/request.py

"""
Module: exchange.request.permission.crud.delete.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import ExchangeObjectCollection
from exchange import CrudPermissionRequest, ExchangeDataObject
from artifcat import DeletionRequest


T = TypeVar("T", bound="ExchangeDataObject")


class DeletePermissionRequest(CrudPermissionRequest[DeletionRequest], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a collection and details about the item a Deleter needs to run a job.

     Attributes:
         id: int
         collection: ExchangeObjectCollection[T]

     Provides:
     
     Super Class:
        CrudPermissionRequest
     """
    
    def __init__(self, id: int, collection: ExchangeObjectCollection[T]):
        """
        Args:
            id: int
            collection: ExchangeObjectCollection[T]
        """
        super().__init__(id, collection=collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeletePermissionRequest):
            permissionRequest = cast(DeletePermissionRequest, other)
            return self.id == permissionRequest.id
        return False
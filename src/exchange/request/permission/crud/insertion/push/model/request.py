# src/exchange/permissionRequest/permission/crud/insertion/push/model/request.py

"""
Module: exchange.request.permission.crud.insertion.push.model.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from exchange import PushPermissionRequest

T = TypeVar("T", bound="ModelPushPermissionRequest")


class ModelPushPermissionRequest(
    PushPermissionRequest[T], ABC, Generic[T]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a ModelPushAuthorizer with job details.

     Attributes:
         id: int
         candidate: : T

     Provides:

     Super Class:
        PushPermissionRequest
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
        if isinstance(other, ModelPushPermissionRequest):
            return self.id == other.id
        return False
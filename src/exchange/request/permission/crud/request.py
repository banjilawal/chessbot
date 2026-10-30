# src/exchange/request/permission/crud/request.py

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
         authorization_applicant: : T

     Provides:

     Super Class:
        PermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: T
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> T:
        return cast(T, super().authorization_applicant)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CrudPermissionRequest):
            return self.id == other.id
        return False
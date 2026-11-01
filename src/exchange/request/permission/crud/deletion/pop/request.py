# src/exchange/request/permission/crud/deletion/pop/request.py

"""
Module: exchange.request.permission.crud.deletion.pop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from exchange import DeletionPermissionRequest, PopRequest

T = TypeVar("T", bound="PopRequest")


class PopPermissionRequest(
    DeletionPermissionRequest[T], ABC, Generic[T]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides a PopPermitter with job details.

     Attributes:
         id: int
         authorization_applicant: : T

     Provides:

     Super Class:
        DeletionPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: T):
        """
        Args:
            id: int
            authorization_applicant: T
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
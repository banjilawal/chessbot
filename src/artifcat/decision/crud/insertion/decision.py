# src/artifact/decision/crud/insertion/decision.py

"""
Module: artfifact.decision.crud.insertion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Self, TypeVar, cast

from artifcat import CrudDecision, Permission
from request import InsertionPermissionRequest, InsertionRequest

P = TypeVar("P", bound="InsertionPermissionRequest")
T = TypeVar("T", bound="InsertionRequest")


class InsertionDecision(CrudDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an Insertion transaction is permitted.

    Attributes:
    
    Provides:
        -   def do_nothing() -> InsertionDecision
        
    Super Class:
        CrudDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[P] | None = None,
            transaction_request: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[P]
            transaction_request: Optional[T]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
        
    @classmethod
    def do_nothing(cls) -> Self:
        return cls(permission=Permission.DO_NOTHING)

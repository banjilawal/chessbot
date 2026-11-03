# src/authorization/checker/checker.py

"""
Module: authorization.checker.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from exchange import PermissionRequest, TransactionRequest
from util import LoggingLevelRouter

D = TypeVar("D", bound="Decision")
P = TypeVar("P")
R = TypeVar("R")


class RoleChecker(ABC, Generic[D, P, R]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for implementing a check on an Actor's eligibility to perform a Maneuver.

    Attributes:
        role: R
        principal: P
        transaction_request: TransactionRequest
        permission_request: PermissionRequest

    Provides:
        -   def execute(request: P) -> Decision

    Super Class:
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            role: R,
            principal: P,
            transaction_request: TransactionRequest,
            permission_request: PermissionRequest,
    ) -> D:
        """
        Check if a transaction permission requirement is satisfied.
        Args:
            role: R
            principal: P
            transaction_request: TransactionRequest
            permission_request: PermissionRequest
        Returns:
            D
        Raises:
            CheckerException
        """
        pass

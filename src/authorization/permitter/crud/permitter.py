# src/authorization/permitter/crud/permitter.py

"""
Module: authorization.permitter.crud.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import CrudDecision
from authorization import Permitter
from bootstrap import CrudAuthorizationLoader
from exchange import CrudPermissionRequest
from exchange.service import ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudPermissionRequest")

class CrudPermitter(Permitter[T], ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about a CrudPermissionRequest.

    Attributes:
        loader: CrudAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> CrudDecision

    Super Class:
        Permitter
    """

    def __init__(self, loader: CrudAuthorizationLoader[T]):
        """
        Args:
            loader: CrudAuthorizationLoader[T]
        """
        super().__init__(loader=loader)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> CrudDecision:
        """
        Grant permission for a CRUD activity.
        Args:
            candidate: Any
        Returns:
           CrudDecision
        Raises:
            CrudPermitterException
        """
        
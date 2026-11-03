# src/authorization/permitter/permitterr.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Decision
from bootstrap import AuthorizationLoader
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class Permitter(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant permission to perform an activity.

    Attributes:
        loader: AuthorizationLoader[T]
        
    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
    """
    
    _loader: AuthorizationLoader[T]

    def __init__(self, loader: AuthorizationLoader[T]):
        """
        Args:
            loader: AuthorizationLoader[T]
        """
        self._loader = loader
    
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Grant permission for an activity.
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
            PermitterException
        """
        
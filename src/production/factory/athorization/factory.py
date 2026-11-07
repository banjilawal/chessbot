# src/production/factory/authorization/factory.py

"""
Module: production.factory.authorization.factory
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import Decision
from bootstrap import AuthorizationLoader
from exchange import PushPermissionRequest
from production import CollisionManager
from util import LoggingLevelRouter

T = TypeVar("T", bound="PushPermissionRequest")

class PermissionFactory(ABC, ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable authorization module.

    Attributes:
        manager: CollisionManager[T]

    Provides:
        -   def execute(candidate: Any) -> Decision[Blueprint[T]|T]:
    Super
    """
    
    _manager: CollisionManager[T]
    _loader: AuthorizationLoader[T]


    
    def __init__(
            self,
            manager: CollisionManager[T],
            loader: AuthorizationLoader[T],
    ):
        """
        Args:
            manager: CollisionManager[T]
            loader: AuthorizationLoader[T]
        """
        self._manager = manager
        self._loader = loader
        
    @property
    def loader(self) -> AuthorizationLoader:
        return self._loader
     
    @property
    def manager(self) -> CollisionManager[T]:
        return self._manager
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> Decision:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           Decision[T]
        Raises:
            ValidatorException
        """
        pass
    
    

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
from production import CollisionManagery
from util import LoggingLevelRouter

T = TypeVar("T")

class AuthorizationFactory(ABC, ABC, Generic[T]):
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
    
    def __init__(self, manager: CollisionManager[T]):
        """
        Args:
            manager: CollisionManager[T]
        """
        self._manager = manager
     
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
    
    

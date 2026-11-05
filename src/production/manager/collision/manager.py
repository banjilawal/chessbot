# src/production/manager/collision/manager.py

"""
Module: production.manager.collision.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CollisionReport
from collection import Stack
from environment import CollisionDetector
from util import LoggingLevelRouter

T = TypeVar("T")


class CollisionManager(ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable collision module.

    Attributes:
        detector: CollisionDetector[T]

    Provides:
        -   def execute(item: T, collection: Stack[T]) -> CollisionReport
        
    Super Class:
    """

    _detector: CollisionDetector[T]
    
    def __init__(self, detector: CollisionDetector[T]):
        """
        Args:
            detector: CollisionDetector[T]
        """
        self._detector = detector

    @property
    def detector(self) -> CollisionDetector[T]:
        return self._detector
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: T, collection: Stack[T]) -> CollisionReport:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: T
            collection: Stack[T]
        Returns:
           CollisionReport
        Raises:
            CollisionManagerException
        """
        pass
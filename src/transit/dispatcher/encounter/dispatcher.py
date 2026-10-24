# src/transit/dispatcher/encounter/dispatcher.py

"""
Module: transit.dispatcher.encounter.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from artifcat import Decision
from exchange import EncounterRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="EncounterRequest")

class EncounterDispatcher(ABC, Generic[T]):
    """
    Role
        -   Permission Encounter Manager

    Responsibilities:
        1.  Grant

    Attributes:
        authorizer: Authorizer[T]

    Provides:
        -   def  execute(self, request: T) -> Decision[T]

    Super Class:
        Dispatcher
    """
    
    _authorizer: Authorizer[T]
    
    def __init__(self, authorizer: Authorizer[T]):
        """
        Args:
            authorizer: Authorizer[T]
        """
        self._authorizer = authorizer
        
    @property
    def authorizer(self) -> Authorizer[T]:
        return self._authorizer
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Decide if an activity can be performed.
        Args:
            request: T
        Returns:
            Decision[T]
        Raises:
            EncounterDispatcherException
        """
        pass
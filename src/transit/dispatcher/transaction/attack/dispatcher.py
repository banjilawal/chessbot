# src/transit/dispatcher/Attack/dispatcher.py

"""
Module: transit.dispatcher.Attack.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import AttackResponse, AttackResult
from domain import Encounter
from exchange import AttackRequest
from transit import Dispatcher
from util import LoggingLevelRouter


T = TypeVar("T", bound="Encounter")

class AttackDispatcher(Dispatcher[AttackResult], ABC, Generic[T]):
    """
    Role
        -   Permission Attack Manager

    Responsibilities:
        1.  Grant

    Attributes:
        attacker: Attacker[T]

    Provides:
        -   def  execute(self, request: AttackRequest) -> AttackResponse

    Super Class:
        Dispatcher
    """
    
    _attacker: Attacker
    
    def __init__(self, attacker: Attacker[T] | None = None):
        """
        Args:
            Attacker: Optional[Attacker]
        """
        self._attacker = attacker
    
    @property
    def attacker(self) -> Attacker[T]:
        return self._attacker
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackResponse:
        """
        Decide if an activity can be performed.
        Args:
            request: T
        Returns:
            AttackResponse
        Raises:
            AttackDispatcherException
        """
        pass
# src/transit/dispatcher/attack/domain/dispatcher.py

"""
Module: transit.dispatcher.attack.domain.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import AttackResult
from domain import AttackRequest
from fabrication import Attack
from transit import AttackDispatcher
from util import LoggingLevelRouter

T = TypeVar("T")


class DomainObjectAttackDispatcher(AttackDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner
    
    Responsibilities:
        1.  Ensure a new T instance is born safe and reliable.
    
    Attributes:
        attack_toolkit: AttackToolkit[T]
    
    Provides:
        -   def execute(self, blueprint: Blueprint[T]) -> AttackResult[T]
    
    Super Class:
    """
    _attack: DomainObjectAttack[T]
    
    def __init__(self, assembler: Attack[T]):
        """
        Args:
           assembler: AttackToolkit[T]
        """
        self._assembler = assembler
    
    @property
    def assembler(self) -> Attack[T]:
        return self._assembler

    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest[T]) -> AttackResult[T]:
        pass
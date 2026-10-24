# src/transit/dispatcher/attack/dispatcher/attack/toggle/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.toggle.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast


from domain.metadata.blueprint.struct.toggle import ToggleBlueprint
from transit.dispatcher.attack import AttackDispatcher
from artifcat import AttackResult
from operation.toolkit import AttackToolkit, ToggleAttackToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Toggle")


class ToggleAttackDispatcher(AttackDispatcher, Generic[T]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Toggle instance is born safe and reliable.

    Attributes:
            attack_toolkit: [ToggleAttackToolkit[T]]

    Provides:
        -   def execute(self, blueprint: ToggleBlueprint[T]) -> AttackResult[T]

     Super Class:
         Attack
     """
    def __init__(self, attack_toolkit: ToggleAttackToolkit[T]):
        """
        Args:
            attack_toolkit: ToggleAttackToolkit[T]
        """
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> AttackToolkit[T]:
        return cast(ToggleAttackToolkit[T], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ToggleBlueprint[T]) -> AttackResult[T]:
        pass
        
        

# src/space/dispatcher/attack/struct/register/__init__.py

"""
Module: space.attack.register.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.blueprint import RegisterBlueprint
from transit.dispatcher.attack import AttackDispatcher
from artifcat import AttackResult
from operation.toolkit import RegisterAttackToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Register")


class RegisterAttackDispatcher(AttackDispatcher, Generic[T]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Register instance is born safe and reliable.

    Attributes:
            attack_toolkit: [RegisterAttackToolkit[T]]

    Provides:
        -   def execute(self, blueprint: RegisterBlueprint[T]) -> AttackResult[Register]

     Super Class:
         Attack
     """
    
    def __init__(self, attack_toolkit: [RegisterAttackToolkit[T]]):
        """
        Args:
            attack_toolkit: [RegisterAttackToolkit[T]]
        """
        super().__init__(attack_toolkit=attack_toolkit)
        
    @property
    def attack_toolkit(self) -> RegisterAttackToolkit[T]:
        return cast([RegisterAttackToolkit[T]], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RegisterBlueprint[T]) -> AttackResult[T]:
        pass
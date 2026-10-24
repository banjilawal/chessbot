# src/transit/dispatcher/attack/model/dispatcher/attack/model/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.model.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from domain import Model
from fabrication import Attack

T = TypeVar("T", bound="Model")


class ModelAttackDispatcher(Attack[T], ABC, Generic[T]):
    """
    Role
        - Attack Pipeline
        - Integrity Management
        - Consistency Assurance
        - Workflow Owner

   Responsibilities:
        1.  Ensure a new Model instance is born safe and reliable.

    Attributes:
            attack_toolkit: ModelAttackToolkit[T]

    Provides:
        -   def execute(self, blueprint: ModelBlueprint[T]) -> AttackResult[T]

     Super Class:
         Attack
     """
    def __init__(self, assembler: [ModelAttackToolkit[T]]):
        """
        Args:
            assembler: [ModelAttackToolkit[T]]
        """
        super().__init__(assembler=assembler)
    
    @property
    def assembler(self) -> ModelAttackToolkit[T]:
        return cast(ModelAttackToolkit[T], super().assembler)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ModelBlueprint[T]) -> AttackResult[T]:
        pass
        
        

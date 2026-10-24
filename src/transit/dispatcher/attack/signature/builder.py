# src/transit/dispatcher/attack/pattern/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.pattern.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast


T = TypeVar("T", bound="Signature")

class SignatureAttack(Attack, ABC, Generic[T]):
    
    def __init__(self, attack_toolkit: SignatureAttackToolkit[T]):
        super().__init__(attack_toolkit=attack_toolkit)
    
    @property
    def attack_toolkit(self) -> SignatureAttackToolkit[T]:
        return cast(T, super().attack_toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SignatureBlueprint[T]) -> AttackResult[T]:
        pass
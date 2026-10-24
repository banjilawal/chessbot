# src/transit/dispatcher/attack/space/quadrant/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.quadrant.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.metadata.blueprint import Blueprint
from transit.dispatcher.attack import SpaceAttackDispatcher
from artifcat import AttackResult
from operation.toolkit import QuadrantAttackToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="QuadrantSpace")


class QuadrantAttack(SpaceAttackDispatcher, Generic[T]):

    
    def __init__(self, attack_toolkit: QuadrantAttackToolkit[T]):
        super().__init__(attack_toolkit=attack_toolkit)
        
    @property
    def attack_toolkit(self) -> QuadrantAttackToolkit:
        return cast(QuadrantAttackToolkit[T], super().assembler)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: Blueprint[T]) -> AttackResult[T]:
        pass
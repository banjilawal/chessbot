# src/transit/dispatcher/attack/space/axis/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.axis.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar, cast

from domain.blueprint import AxisBlueprint
from transit.dispatcher.attack import SpaceAttackDispatcher
from artifcat import AttackResult
from operation.toolkit import AxisAttackToolkit
from util import LoggingLevelRouter

T = TypeVar("T", bound="Axis")


class AxisAttack(SpaceAttackDispatcher, Generic[T]):

    
    def __init__(self, attack_toolkit: AxisAttackToolkit[T]):
        super().__init__(attack_toolkit=attack_toolkit)
        
    @property
    def attack_toolkit(self) -> AxisAttackToolkit:
        return cast(AxisAttackToolkit[T], super().assembler)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisBlueprint[T]) -> AttackResult[T]:
        pass
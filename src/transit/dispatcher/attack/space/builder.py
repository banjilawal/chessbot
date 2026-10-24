# src/transit/dispatcher/attack/space/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.space.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, Optional, TypeVar, cast

from transit.dispatcher.attack import AttackDispatcher
from domain.model import Vector

from artifcat import AttackResult
from operation.toolkit import MathToolkit, SpaceAttackToolkit
from util import LoggingLevelRouter


T = TypeVar("T", bound="Space")

class SpaceAttackDispatcher(AttackDispatcher, Generic[T]):
    _math_toolkit: MathToolkit
    
    def __init__(
            self,
            attack_toolkit: Optional[SpaceAttackToolkit] | None = None,
            math_toolkit: Optional[MathToolkit] | None = None,
    ):
        """
        Args:
            attack_toolkit: Optional[SpaceAttackToolkit]
            math_toolkit: Optional[MathToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit or SpaceAttackToolkit())
        self._math_toolkit = math_toolkit or MathToolkit()
        
    @property
    def attack_toolkit(self) -> SpaceAttackToolkit:
        return cast(SpaceAttackToolkit, super().assembler)
        
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, origin: Vector) -> AttackResult[T]:
        pass

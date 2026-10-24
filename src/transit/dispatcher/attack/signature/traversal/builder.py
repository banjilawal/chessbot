# src/transit/dispatcher/attack/pattern/traversal/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.pattern.traversal.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from transit.dispatcher.attack import SignatureAttack
from util import LoggingLevelRouter

T = TypeVar("T", bound="TraversalSignature")

class TraversalAttack(SignatureAttack, ABC, Generic[T]):
    """
    Role:
        - Iteration


    Responsibilities:
        1.  Stepping function which gives the next vector in a series.

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:

    Super Class:
    """
    
    def __init__(self, attack_toolkit: TraversalAttackToolkit[T]):
        super().__init__(attack_toolkit=attack_toolkit)
        
    @property
    def attack_toolkit(self) -> TraversalAttackToolkit[T]:
        return cast(TraversalAttackToolkit[T], super().attack_toolkit)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, attack: TraversalAttack[T]) -> AttackResult[T]:
        pass
# src/transit/dispatcher/attack/pattern/offset/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.pattern.offset.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from transit.dispatcher.attack import SignatureAttack
from util import LoggingLevelRouter

T = TypeVar("T", bound="OffsetSignature")

class OffsetAttack(SignatureAttack, Generic[T]):
    
    def __init__(self, attack_toolkit: OffsetAttackToolkit[T]):
        super().__init__(attack_toolkit=attack_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, attack: OffsetSignatureAttack[T]) -> AttackResult[OffsetSignature[T]]:
        pass

    
    
    
# src/transit/dispatcher/attack/pattern/offset/knight/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.pattern.offset.knight.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from transit.dispatcher.attack import OffsetAttack
from surface.topology import KnightSignature
from artifcat import AttackResult
from util import LoggingLevelRouter


class KnightOffsetAttack(OffsetAttack[KnightSignature]):
    
    def __init__(self, attack_toolkit: Optional[KnightSignatureAttackToolkit]):
        """
        Args:
            attack_toolkit: Optional[KnightSignatureAttackToolkit]
        """
        super().__init__(attack_toolkit=attack_toolkit or KnightSignatureAttackToolkit())
        
        
    @property
    def attack_toolkit(self) -> KnightSignatureAttackToolkit:
        return cast(KnightSignatureAttackToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, attack:KnightSignatureAttack) -> AttackResult[KnightSignature]:
        method = f"{self.__class__.__name__}"
    

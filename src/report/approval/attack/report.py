# src/report/approval/attack/report.py

"""
Module: report.approval.attack.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import CombatantToken, KingToken, Square, Token
from report import OperationApprovalReport, Permission


class AttackApprovalReport(OperationApprovalReport):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Provides details about the outcome of a promote approval request.
        
    Attributes:
        token: T
        origin: Origin
        exception: Optional[Exception]
        permission: Permission
        
    Provides:
        -   def approve(token: T, origin: Origin) -> OperationApprovalReport
        -   def deny(exception: Exception) -> OperationApprovalReport:
        
    Super Class:
        OperationApprovalReport
    """
    _attacker: Optional[Token]
    _enemy_king: Optional[KingToken]
    _enemy_combatant: Optional[CombatantToken]
    _enemy_square: Optional[Square]
    _benefit: Optional[int]
    
    def __init__(
            self,
            permission: Permission,
            attacker: Optional[Token] | None = None,
            enemy_king: Optional[KingToken] | None = None,
            enemy_combatant: Optional[CombatantToken] | None = None,
            enemy_square: Optional[Square] | None = None,
            exception: Optional[Exception] | None = None,
            benefit: Optional[int] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._attacker = attacker
        self._enemy_king = enemy_king
        self._enemy_combatant = enemy_combatant
        self._enemy_square = enemy_square
        self._benefit = benefit
    
    @property
    def attacker(self) -> Optional[Token]:
        return self._attacker
    
    @property
    def enemy_king(self) -> Optional[KingToken]:
        return self._enemy_king
    
    @property
    def enemy_combatant(self) -> Optional[CombatantToken]:
        return self._enemy_combatant
    
    @property
    def enemy_square(self) -> Optional[Square]:
        return self._enemy_square
    
    @property
    def benefit(self) -> Optional[int]:
        return self._benefit
    
    @property
    def king_attack_is_granted(self) -> bool:
        return (
                self._attacker is not None and
                self._enemy_king is not None and
                self._enemy_square is not None and
                self.enemy_king.current_position == self._enemy_square.coord and
                self._enemy_combatant is None and
                self.exception is None and
                super().is_granted
        )
    
    @property
    def combatant_attack_is_granted(self) -> bool:
        return (
                self._attacker is not None and
                self._enemy_combatant is not None and
                self._enemy_square is not None and
                self.enemy_combatant.current_position == self._enemy_square.coord and
                self._enemy_king is None and
                self.exception is None and
                super().is_granted
        )
    
    @property
    def is_granted(self) -> bool:
        return self.king_attack_is_granted or self.combatant_attack_is_granted
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def approve_king_attack(
            cls,
            attacker: Token,
            enemy_king: KingToken,
            enemy_square: Square,
            benefit: Optional[int] | None = None,
    ) -> AttackApprovalReport:
        return cls(
            attacker=attacker,
            enemy_king=enemy_king,
            enemy_square=enemy_square,
            permission=Permission.GRANTED,
            benefit=benefit,
        )
    
    @classmethod
    def approve_combatant_attack(
            cls,
            attacker: Token,
            enemy_combatant: CombatantToken,
            enemy_square: Square,
            benefit: Optional[int] | None = None,
    ) -> AttackApprovalReport:
        return cls(
            attacker=attacker,
            enemy_combatant=enemy_combatant,
            enemy_square=enemy_square,
            permission=Permission.GRANTED,
            benefit=benefit,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> AttackApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )

    
    

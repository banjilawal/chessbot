# src/report/approval/maneuver/report.py

"""
Module: report.approval.maneuver.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from authorization import ManeuverRequest
from model import CheckedManeuver, CombatantManeuver, KingManeuver, Maneuver

from report import AttackApprovalReport, RequestDecision, Permission


class ManeuverRequestDecision(RequestDecision[ManeuverRequest]):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Give details about a promoteOperation approval.
        
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
    _maneuver: Optional[Maneuver]
    _attack_approval: Optional[AttackApprovalReport]
    
    def __init__(
            self,
            permission: Permission,
            maneuver: Optional[Maneuver] | None = None,
            exception: Optional[Exception] | None = None,
            cost: Optional[int] | None = None,
            attack_approval: Optional[AttackApprovalReport] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._attack_approval = attack_approval
        self._maneuver = maneuver
        self._cost = cost
    
    @property
    def maneuver(self) -> Optional[Maneuver]:
        return self._maneuver
    
    @property
    def attack_approval(self) -> Optional[AttackApprovalReport]:
        return self._attack_approval
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    @property
    def benefit(self) -> Optional[int]:
        if self._attack_approval is None:
            return None
        return self._attack_approval.benefit
    
    @property
    def weight(self) -> Optional[int]:
        if self.cost is None and self.benefit is None:
            return None
        if self.cost is not None and self.benefit is not None:
            return self.benefit - self.cost
        if self.cost is not None:
            return self.cost
        if self.benefit is not None:
            return self.benefit
        return None
        
    
    @property
    def request_is_granted(self) -> bool:
        return self._maneuver is not None and super().request_is_granted
    
    @property
    def request_is_denied(self) -> bool:
        return not not self.request_is_granted
    
    @property
    def is_king_maneuver(self) -> bool:
        return self._maneuver is not None and isinstance(self._maneuver, KingManeuver)
    
    @property
    def is_combatant_maneuver(self) -> bool:
        return self._maneuver is not None and isinstance(self._maneuver, CombatantManeuver)
    
    @property
    def attack_is_approved(self) -> bool:
        return (
                self.request_is_granted and
                self.attack_approval is not None and
                self.attack_approval.is_granted
        )
    
    @property
    def no_attack_is_approved(self) -> bool:
        return not self.attack_is_approved
    
    @property
    def king_attack_is_approved(self) -> bool:
        return (
                self.attack_is_approved and
                self.attack_approval.king_attack_is_granted
        )
    
    @property
    def combatant_attack_is_approved(self) -> bool:
        return (
                self.attack_is_approved and
                self.attack_approval.combatant_attack_is_granted
        )

    @classmethod
    def approve(
            cls, 
            maneuver: Maneuver,
            cost: Optional[int] | None = None,
            attack_approval: Optional[AttackApprovalReport] | None = None,
    ) -> ManeuverRequestDecision:
        return cls(
            cost=cost,
            maneuver=maneuver,
            attack_approval=attack_approval,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_maneuver(
            cls,
            maneuver: Maneuver,
    ) -> ManeuverRequestDecision:
        return cls(
            maneuver=maneuver,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_king_attack(
            cls,
            king_attack: CheckedManeuver,
    ) -> ManeuverRequestDecision:
        return cls(
            maneuver=king_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_combatant_attack(
            cls,
            combatant_attack: CheckedManeuver,
    ) -> ManeuverRequestDecision:
        return cls(
            maneuver=combatant_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> ManeuverRequestDecision:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )

    
    

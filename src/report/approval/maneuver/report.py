# src/report/approval/promote/report.py

"""
Module: report.approval.promote.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import CombatantManeuver, KingManeuver, Maneuver
from model.state.maneuver.checked.model import CheckedManeuver
from report import OperationApprovalReport, Permission


class ManeuverApprovalReport(OperationApprovalReport):
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
    _maneuver: Optional[Maneuver]
    
    def __init__(
            self,
            permission: Permission,
            maneuver: Optional[Maneuver] | None = None,
            exception: Optional[Exception] | None = None,
            cost: Optional[int] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._maneuver = maneuver
        self._cost = cost
    
    @property
    def maneuver(self) -> Optional[Maneuver]:
        return self._maneuver
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    @property
    def is_granted(self) -> bool:
        return self._maneuver is not None and super().is_granted
    
    @property
    def is_denied(self) -> bool:
        return not not self.is_granted
    
    @property
    def is_king_maneuver(self) -> bool:
        return self._maneuver is not None and isinstance(self._maneuver, KingManeuver)
    
    @property
    def is_combatant_maneuver(self) -> bool:
        return self._maneuver is not None and isinstance(self._maneuver, CombatantManeuver)

    
    @classmethod
    def approve(
            cls, 
            maneuver: Maneuver,
            cost: Optional[int] | None = None,
    ) -> ManeuverApprovalReport:
        return cls(
            cost=cost,
            maneuver=maneuver,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_maneuver(
            cls,
            maneuver: Maneuver,
    ) -> ManeuverApprovalReport:
        return cls(
            maneuver=maneuver,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_king_attack(
            cls,
            king_attack: CheckedManeuver,
    ) -> ManeuverApprovalReport:
        return cls(
            maneuver=king_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_combatant_attack(
            cls,
            combatant_attack: CheckedManeuver,
    ) -> ManeuverApprovalReport:
        return cls(
            maneuver=combatant_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> ManeuverApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )

    
    

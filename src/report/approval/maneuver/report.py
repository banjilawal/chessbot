# src/report/approval/promote/report.py

"""
Module: report.approval.promote.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import CheckedPath, Path, Token, Path
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
    _path: Optional[Path]
    
    def __init__(
            self,
            permission: Permission,
            path: Optional[Path] | None = None,
            exception: Optional[Exception] | None = None,
            cost: Optional[int] | None = None,
    ):
        super().__init__(exception=exception, permission=permission)
        self._path = path
        self._cost = cost
    
    @property
    def path(self) -> Optional[Path]:
        return self._path
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    @property
    def is_granted(self) -> bool:
        return self._path is not None and super().is_granted
    
    @property
    def is_denied(self) -> bool:
        return not not self.is_granted

    
    @classmethod
    def approve(
            cls, 
            path: Path,
            cost: Optional[int] | None = None,
    ) -> ManeuverApprovalReport:
        return cls(
            cost=cost,
            path=path,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_maneuver(
            cls,
            maneuver: Path,
    ) -> ManeuverApprovalReport:
        return cls(
            path=maneuver,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_king_attack(
            cls,
            king_attack: CheckedPath,
    ) -> ManeuverApprovalReport:
        return cls(
            path=king_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def approve_combatant_attack(
            cls,
            combatant_attack: CheckedPath,
    ) -> ManeuverApprovalReport:
        return cls(
            path=combatant_attack,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def deny(cls, exception: Exception) -> ManeuverApprovalReport:
        return cls(
            exception=exception,
            permission=Permission.DENIED,
        )

    
    

# src/model/dossier/model.py

"""
Module: model.dossier.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional


from model import Square
from report import ManeuverApprovalReport, Report


class SquareDossier:
    """]
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  A Node's payload.

    Attributes:
        square: Square
        report: Optional[Report]

    Provides:

    Super Class:
    """
    _square: Square
    _report: Optional[ManeuverApprovalReport]
    
    def __init__(self, square: Square, report: Optional[ManeuverApprovalReport] | None = None):
        """
        Args:
            square: Square
            report: Optional[Report]
        """
        self._square = square
        self._report = report
        
    @property
    def square(self) -> Square:
        return self._square
    
    @property
    def report(self) -> Optional[ManeuverApprovalReport]:
        return self._report
    
    @property
    def has_king_attack_approval(self) -> bool:
        return self._report is not None and self._report.king_attack_is_approved
    
    @property
    def has_combatant_approval(self) -> bool:
        return self._report is not None and self._report.combatant_attack_is_approved
    
    @report.setter
    def report(self, other: ManeuverApprovalReport):
        self._report = other

        

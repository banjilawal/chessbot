# src/model/dossier/model.py

"""
Module: model.dossier.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from os import times
from sndhdr import tests
from typing import Optional, cast

from model import Square
from report import ManeuverRequestDecision, Report


class Dossier:
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
    _timestamp: int
    _report: Optional[ManeuverRequestDecision]
    
    def __init__(
            self,
            square: Square,
            timestamp: int,
            report: Optional[ManeuverRequestDecision] | None = None
    ):
        """
        Args:
            square: Square
            timestamp: int
            report: Optional[Report]
        """
        self._square = square
        self._report = report
        self._timestamp = timestamp
        
    @property
    def square(self) -> Square:
        return self._square
    
    @property
    def timestamp(self) -> int:
        return self._timestamp
    
    @property
    def report(self) -> Optional[ManeuverRequestDecision]:
        return self._report
    
    @property
    def has_king_attack_approval(self) -> bool:
        return self._report is not None and self._report.king_attack_is_approved
    
    @property
    def has_combatant_approval(self) -> bool:
        return self._report is not None and self._report.combatant_attack_is_approved
    
    @report.setter
    def report(self, other: ManeuverRequestDecision):
        self._report = other
        
    def is_fresher_than_other(self, other: Dossier) -> bool:
        return self.timestamp > other.timestamp
    
    def is_not_fresher_than_other(self, other: Dossier) -> bool:
        return self.timestamp <= other.timestamp
        
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Dossier):
            dossier = cast(Dossier, other)
            return  (
                    self.square == dossier.square and
                    self._timestamp == dossier.timestamp
            )
        return False
    
    def __hash__(self) -> int:
        return hash(self.timestamp)
        

        

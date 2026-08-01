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
from report import Report


class SquareDossier:
    """
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
    _report: Optional[Report]
    
    def __init__(self, square: Square, report: Optional[Report] | None = None):
        """
        Args:
            square: Square
            report: Optional[Report]
        """
        self._hunter = square
        self._report = report
        
    @property
    def square(self) -> Square:
        return self._square
    
    @property
    def report(self) -> Optional[Report]:
        return self._report
    
    @report.setter
    def report(self, other: Report):
        self._report = other

        

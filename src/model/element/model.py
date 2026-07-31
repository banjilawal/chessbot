# src/model/element/model.py

"""
Module: model.element.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional


from model import Square
from report import Report


class Element:
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
    
    @property
    def has(self) -> bool:
        return not self.hunter_elementing_itself
    
    @property
    def element_count(self) -> int:
        return self._group.size
    
    @property
    def elements_are_null(self) -> bool:
        return self._group is None
    
    @property
    def has_elements(self) -> bool:
        return self._group.is_not_empty
    
    @property
    def has_no_elements(self) -> bool:
        return not self.has_elements
    
    def remove_hunter_from_elements(self) -> Element:
        if self.hunter_not_elementing_itself:
            return self
        temp = []
        for element in self._group.to_list:
            if element != self.hunter:
                temp.append(element)
        return Element(
            hunter=self._hunter,
            group=VectorSet(tuple(temp))
        )
        

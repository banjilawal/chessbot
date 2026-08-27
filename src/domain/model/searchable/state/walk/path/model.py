# src/domain/model/searchable/walk/path/model.py

"""
Module: domain.model.searchable.walk.path.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional

from domain import SearchableModel, SquareRegister



class Path(SearchableModel):
    """
    Role:
        - Model
        -  Searchableful Data Holder

    Responsibilities:
        1.  Adds a label and cost to a SquareRegister.
        2.  Used in path optimization problems.

    Attributes:
        endpoints: SquareRegister
        id: Optional[int]

    Provides:

    Super Class:
        SearchableModel
    """
    _endpoints: SquareRegister
    _label: Optional[int]
    
    def __init__(
            self,
            endpoints: SquareRegister,
            label: Optional[int] | None = None,
    ):
        """
        Attributes:
            endpoints: SquareRegister
            label: Optional[int]
        """
        super().__init__()
        self._label = label
        self._endpoints = endpoints
        
        
    @property
    def endpoints(self) -> SquareRegister:
        return self._endpoints
    
    @property
    def label(self) -> Optional[int]:
        return self._label
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Path):
            return self.endpoints == other.endpoints
        return False
        
        

        
        
        
    
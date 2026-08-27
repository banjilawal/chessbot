# src/domain/model/searchable/state/walk/path/model.py

"""
Module: domain.model.searchable.state.walk.path.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional

from domain import StatefulModel, SquareRegister



class Path(StatefulModel):
    """
    Role:
        - Model
        -  Searchableful Data Holder

    Responsibilities:
        1.  Adds a label and cost to a SquareRegister.
        2.  Used in path optimization problems.

    Attributes:
        endpoints: SquareRegister
        cost: Optional[int]
        id: Optional[int]

    Provides:

    Super Class:
        Walk
    """
    _endpoints: SquareRegister
    _label: Optional[int]
    _cost: Optional[int]
    
    def __init__(
            self,
            endpoints: SquareRegister,
            label: Optional[int] | None = None,
            cost: Optional[int] | None = None,
    ):
        """
        Attributes:
            endpoints: SquareRegister
            cost: Optional[int]
            label: Optional[int]
        """
        super().__init__()
        self._label = label
        self._cost = cost
        self._endpoints = endpoints
        
        
    @property
    def endpoints(self) -> SquareRegister:
        return self._endpoints
    
    @property
    def label(self) -> Optional[int]:
        return self._label
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Path):
            return self.endpoints == other.endpoints
        return False
        
        

        
        
        
    
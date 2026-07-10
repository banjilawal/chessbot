# src/operand/state/binder/binder.py

"""
Module: operand.state.binder.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

from microservice import Microservice
from operand import Schema

P = TypeVar("P")
S = TypeVar("S")

class Binder(ABC, Generic[P, S]):
    """
    Role:
        -   Operand
        -   Stateless Data-Holder
        
    Responsibility:
        1.  Separates responsibilities of managing the satellites bound to a primary entity.
        2.  Adds utility functions, integrity and consistency management to a dictionary of
            the satellites.
        
    Attributes:
        id: int
        primary: P
        satellite_list: List[S]
        schema_list: List[Schema]
        white_satellite: Optional[S]
        black_satellite: Optional[S]
        satellite_table: Dict[Schema, S]
        satellite_service: Microservice[S]
        is_empty: bool
        is_full: bool
        is_white_slot_occupied: bool
        is_black_slot_occupied: bool

    Provides:

    Super Class:
    
    Binder Implementations:
        Must satisfy at least one of these requirements.
            -   Schemas are a natural, unique attribute of every satellite.
            -   The primary has only two satellites which ae both required for the primary's
                operations.
            -   If primary's satellites do not have an organic schema attribute. It has a transitive
                link to the Schema catalog through one its fields.
    """
    _id: int
    _primary: P
    _satellite_table: Dict[Schema, S]
    _satellite_service: Microservice[S]
    
    def __init__(
            self,
            id: int,
            primary: P,
            satellite_service: Microservice[S],
            satellite_table: Dict[Schema, S] | None = None,
    ):
        """
        Args:
            id: int
            primary: P
            satellite_table: Dict[schema, S]
            satellite_service: MicroService[S]
        """
        self._id = id
        self._primary = primary
        self._satellite_service = satellite_service
        self._satellite_table = satellite_table or {}
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def primary(self) -> P:
        return self._primary
    
    @property
    def satellite_table(self) -> Dict[Schema, S]:
        return self._satellite_table
    
    @property
    def satellite_service(self) -> Microservice[S]:
        return self._satellite_service
        
    @property
    def is_empty(self) -> bool:
        return len(self._satellite_table) == 0
    
    @property
    def is_full(self) -> bool:
        return not len(self._satellite_table) == len(Schema.value)
    
    @property
    def is_white_slot_occupied(self) -> bool:
        return self._satellite_table[Schema.WHITE] is not None
    
    @property
    def is_black_slot_is_occupied(self) -> bool:
        return self._satellite_table[Schema.BLACK] is not None
        
    @property
    def white_satellite(self) -> Optional[S]:
        if Schema.WHITE not in self._satellite_table.keys():
            return None
        return self._satellite_table[Schema.WHITE]
    
    @property
    def black_satellite(self) -> Optional[S]:
        if Schema.BLACK not in self._satellite_table.keys():
            return None
        return self._satellite_table[Schema.BLACK]
    
    @property
    def schema_list(self) -> List[Schema]:
        keys: List[Schema] = []
        for key in self._satellite_table.keys():
            keys.append(key)
        return keys
    
    @property
    def satellite_list(self) -> List[S]:
        satellites: List[S] = []
        for key in self._satellite_table.keys():
            satellites.append(self._satellite_table[key])
        return satellites
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Binder):
            return self.id == other.id
        
    def __hash__(self):
        return hash(self.id)

        
    
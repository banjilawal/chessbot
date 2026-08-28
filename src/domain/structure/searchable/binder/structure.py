# src/domain/structure/binder/binder.py

"""
Module: domain.structure.binder.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Iterator, Optional, TypeVar

from domain import Archetype, Structure
from microservice import Microservice

P = TypeVar("P")
S = TypeVar("S")

class ColorBinder(Structure, ABC, Generic[P, S]):
    """
    Role:
        - Model
        -  Stateless Data-Holder
        
    Responsibility:
        1.  Ensure the two satellites are correctly mapped to a GameColor when the Primary
            is created.
        2.  Simplify satellite selection without having to know any details other than
            the satellite's GameColor.
        3.  Guarantee consistency between:
                -   The primary and its satellites.
                -   Between the satellites.
        
    Attributes:
        id: int
        primary: P
        satellite_list: List[S]
        archetype_list: List[Archetype]
        white_satellite: Optional[S]
        black_satellite: Optional[S]
        satellite_table: Dict[Archetype, S]
        satellite_service: Microservice[S]
        is_empty: bool
        is_full: bool
        is_white_slot_occupied: bool
        is_black_slot_occupied: bool

    Provides:

    Super Class:
    
    Binder Implementations:
        Must satisfy at least one of these requirements.
            -  Archetypes are a natural, unique attribute of every satellite.
            -  The primary has only two satellites which ae both required for the primary's
                operations.
            -  If primary's satellites do not have an organic archetype attribute. It has a transitive
                link to the Archetype catalog through one its fields.
    """
    _id: int
    _primary: P
    _satellite_table: Dict[Archetype, S]
    _satellite_service: Microservice[S]
    
    def __init__(
            self,
            id: int,
            primary: P,
            satellite_service: Microservice[S],
            satellite_table: Dict[Archetype, S] | None = None,
    ):
        """
        Args:
            id: int
            primary: P
            satellite_table: Dict[archetype, S]
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
    def satellite_service(self) -> Microservice[S]:
        return self._satellite_service
        
    @property
    @abstractmethod
    def has_both_slots_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_both_slots_occupied(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_white_slot_occupied(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_black_slot_occupied(self) -> bool:
        pass
        
    @property
    @abstractmethod
    def white_satellite(self) -> Optional[S]:
        pass
    
    @property
    @abstractmethod
    def black_satellite(self) -> Optional[S]:
        pass
    
    @property
    @abstractmethod
    def archetype_iter(self) -> Iterator[Archetype]:
        pass
    
    @property
    @abstractmethod
    def satellite_iter(self) -> Iterator[S]:
        pass
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ColorBinder):
            return self.id == other.id
        
    def __hash__(self):
        return hash(self.id)

        
    
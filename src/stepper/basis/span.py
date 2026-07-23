# src/space/basis/basis/space.py

"""
Module: space.basis.basis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from math import BasisTargetVectorSpanner
from model import Vector
from result import ComputationResult
from space.basis import VectorSet
from util import LoggingLevelRouter

T = TypeVar("T", bound="Rank")

class BasisSpace(ABC, Generic[T]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors from an origin by adding it to each
            movement vector.

    Attributes:
        origin: Vector
        offsets: VectorSet[T]
        targeting_computer: Optional[DestinationSpanComputer]
        
        is_empty: bool
        is_not_empty: bool
        is_a_point: bool
        is_a_line: bool:
        is_an_area:  bool
        has_inconsistency: bool
        
    Provides:

    Super Class:
    """
    _origin: Vector
    _offsets: VectorSet[T]
    _targeting_computer: BasisTargetVectorSpanner
    
    def __init__(
            self,
            origin: Vector,
            offsets: VectorSet[T],
            targeting_computer: Optional[BasisTargetVectorSpanner] |
                                None = BasisTargetVectorSpanner(),
    ):
        """
        Args:
            origin: Vector
            offsets: VectorSet
            targeting_computer: Optional[DestinationSpanComputer]
        """
        self._origin = origin
        self._offsets = offsets
        self._targeting_computer = targeting_computer
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def offsets(self) -> VectorSet[T]:
        return self._offsets
    
    @property
    def targeting_computer(self) -> BasisTargetVectorSpanner:
        return self._targeting_computer
    
    @property
    def is_empty(self) -> bool:
        return self._offsets.is_empty and self._origin is None
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_a_point(self) -> bool:
        return self._origin is not None and self._offsets.is_empty
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def target_vectors(self) -> ComputationResult[TargetVectorSet]:
        pass
    
    @property
    def is_a_line(self) -> bool:
        return self.origin is not None and self._offsets.rule_count == 1
    
    @property
    def is_an_area(self) -> bool:
        return self._origin is not None and self._offsets.rule_count > 1
    
    @property
    def has_inconsistency(self) -> bool:
        return self.is_a_point or self.is_empty
    

        

# src/space/span/basis/span.py

"""
Module: space.span.basis.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar

from err import BasisNullException
from model import Vector
from space import ManeuverVectorSet, VectorTargetingComputer

T = TypeVar("T", bound="Basis")

class BasisBlueprint(SpaceBlueprint, Generic[T]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors from an origin by adding it to each
            movement vector.

    Attributes:
        origin: Vector
        maneuver_vectors: ManeuverVectorSet[T]
        targeting_computer: Optional[DestinationSpanComputer]
        
    Provides:

    Super Class:
        SpaceBlueprint
    """
    _origin: Vector
    _maneuver_vectors: ManeuverVectorSet[T]
    _targeting_computer: VectorTargetingComputer
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: ManeuverVectorSet[T],
            model_class: Type[T],
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
            null_exception: Optional[BasisNullException] | None = BasisNullException(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: ManeuverVectorSet
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._origin = origin
        self._maneuver_vectors = maneuver_vectors
        self._targeting_computer = targeting_computer
        
    @property
    def model_class(self) -> Type[T]:
        return cast(Type[T], self.model)
    
    @property
    def null_exception(self) -> BasisNullException:
        return cast(BasisNullException, self.null_exception)
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def maneuver_vectors(self) -> ManeuverVectorSet[T]:
        return self._maneuver_vectors
    
    @property
    def targeting_computer(self) -> VectorTargetingComputer:
        return self._targeting_computer
        

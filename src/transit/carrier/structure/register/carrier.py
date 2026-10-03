# src/transit/carrier/structure/register/carrier.py

"""
Module: transit.carrier.structure.register.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from domain import Register, RegisterBlueprint
from transit import StructureCarrier

T = TypeVar("T", bound="Register")


class RegisterCarrier(StructureCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Register its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[RegisterBlueprint[T]]
        entity: [T | RegisterBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[RegisterBlueprint[T]]

    Super Class:
        StructureCarrier
    """
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[RegisterBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[RegisterBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | RegisterBlueprint[T]]:
        if (
                self.is_empty or
                self.is_not_consistent
        ):
            return None
        if self.has_model:
            return cast(T, super().entity)
        return cast(RegisterBlueprint[T], super().entity)
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[RegisterBlueprint[T]]:
        pass


    
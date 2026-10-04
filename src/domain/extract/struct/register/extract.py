# src/domain/extract/struct/register/extract.py

"""
Module: domain.extract.struct.register.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Register, RegisterBlueprint
from transit import RegisterCarrier

T = TypeVar("T", bound="Register")

class RegisterPrimeExtract(StructPrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for RegisterValidator.

    Attributes:
        carrier: RegisterCarrier
        blueprint: Optional[RegisterBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: RegisterCarrier[T],
            blueprint: Optional[RegisterBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: RegisterCarrier[T]
            blueprint: Optional[RegisterBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> RegisterCarrier[T]:
        return cast(RegisterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[RegisterBlueprint[T]]:
        return cast(RegisterBlueprint, super().blueprint)
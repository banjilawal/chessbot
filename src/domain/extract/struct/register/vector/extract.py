# src/domain/extract/struct/register/vector.extract.py

"""
Module: domain.extract.struct.register.vector.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorRegister, VectorRegisterBlueprint, RegisterPrimeExtract
from transit import VectorRegisterCarrier


class VectorRegisterPrimeExtract(RegisterPrimeExtract[VectorRegister]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for VectorRegisterValidator.

    Attributes:
        carrier: VectorRegisterCarrier
        blueprint: Optional[VectorRegisterBlueprint]

    Provides:

    Super Class:
        RegisterPrimeExtract
    """

    def __init__(
            self,
            carrier: VectorRegisterCarrier,
            blueprint: Optional[VectorRegisterBlueprint] | None = None,
    ):
        """
        Args:
            carrier: VectorRegisterCarrier
            blueprint: Optional[VectorRegisterBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> VectorRegisterCarrier:
        return cast(VectorRegisterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[VectorRegisterBlueprint]:
        return cast(VectorRegisterBlueprint, super().blueprint)
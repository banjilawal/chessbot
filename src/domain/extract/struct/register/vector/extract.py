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
            reference: VectorRegisterCarrier,
            safe_blueprint: Optional[VectorRegisterBlueprint] | None = None,
    ):
        """
        Args:
            reference: VectorRegisterCarrier
            safe_blueprint: Optional[VectorRegisterBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> VectorRegisterCarrier:
        return cast(VectorRegisterCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[VectorRegisterBlueprint]:
        return cast(VectorRegisterBlueprint, super().blueprint)
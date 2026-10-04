# src/domain/extract/struct/register/square.extract.py

"""
Module: domain.extract.struct.register.square.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import SquareRegister, SquareRegisterBlueprint, RegisterPrimeExtract
from transit import SquareRegisterCarrier


class SquareRegisterPrimeExtract(RegisterPrimeExtract[SquareRegister]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for SquareRegisterValidator.

    Attributes:
        carrier: SquareRegisterCarrier
        blueprint: Optional[SquareRegisterBlueprint]

    Provides:

    Super Class:
        RegisterPrimeExtract
    """

    def __init__(
            self,
            carrier: SquareRegisterCarrier,
            blueprint: Optional[SquareRegisterBlueprint] | None = None,
    ):
        """
        Args:
            carrier: SquareRegisterCarrier
            blueprint: Optional[SquareRegisterBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> SquareRegisterCarrier:
        return cast(SquareRegisterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[SquareRegisterBlueprint]:
        return cast(SquareRegisterBlueprint, super().blueprint)
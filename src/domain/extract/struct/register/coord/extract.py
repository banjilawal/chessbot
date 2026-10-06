# src/domain/extract/struct/register/coord.extract.py

"""
Module: domain.extract.struct.register.coord.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordRegister, CoordRegisterBlueprint, RegisterPrimeExtract
from transit import CoordRegisterCarrier


class CoordRegisterPrimeExtract(RegisterPrimeExtract[CoordRegister]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CoordRegisterValidator.

    Attributes:
        carrier: CoordRegisterCarrier
        blueprint: Optional[CoordRegisterBlueprint]

    Provides:

    Super Class:
        RegisterPrimeExtract
    """

    def __init__(
            self,
            reference: CoordRegisterCarrier,
            safe_blueprint: Optional[CoordRegisterBlueprint] | None = None,
    ):
        """
        Args:
            reference: CoordRegisterCarrier
            safe_blueprint: Optional[CoordRegisterBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> CoordRegisterCarrier:
        return cast(CoordRegisterCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CoordRegisterBlueprint]:
        return cast(CoordRegisterBlueprint, super().blueprint)
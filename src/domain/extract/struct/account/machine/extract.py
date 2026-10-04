# src/domain/extract/struct/account/machine.extract.py

"""
Module: domain.extract.struct.account.machine.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import MachineAccount, MachineAccountBlueprint, AccountPrimeExtract
from transit import MachineAccountCarrier


class MachineAccountPrimeExtract(AccountPrimeExtract[MachineAccount]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for MachineAccountValidator.

    Attributes:
        carrier: MachineAccountCarrier
        blueprint: Optional[MachineAccountBlueprint]

    Provides:

    Super Class:
        AccountPrimeExtract
    """

    def __init__(
            self,
            carrier: MachineAccountCarrier,
            blueprint: Optional[MachineAccountBlueprint] | None = None,
    ):
        """
        Args:
            carrier: MachineAccountCarrier
            blueprint: Optional[MachineAccountBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> MachineAccountCarrier:
        return cast(MachineAccountCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[MachineAccountBlueprint]:
        return cast(MachineAccountBlueprint, super().blueprint)
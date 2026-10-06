# src/domain/extract/model/account/machine.extract.py

"""
Module: domain.extract.model.account.machine.extract
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
            reference: MachineAccountCarrier,
            blueprint: Optional[MachineAccountBlueprint] | None = None,
    ):
        """
        Args:
            reference: MachineAccountCarrier
            blueprint: Optional[MachineAccountBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> MachineAccountCarrier:
        return cast(MachineAccountCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[MachineAccountBlueprint]:
        return cast(MachineAccountBlueprint, super().blueprint)
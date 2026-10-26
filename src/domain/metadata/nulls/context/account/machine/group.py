# src/domain/metadata/nulls/context/account/machine/group.py

"""
Module: domain.metadata.nulls.context.account.machine.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import MachineAccount, AccountContextNullGroup
from err import (
    MachineContextBlueprintNullException, MachineContextCarrierNullException, MachineContextNullException
)


class MachineAccountContextNullGroup(AccountContextNullGroup[MachineAccountContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a MachineAccount's integrity cycle.

    Attributes:
        model: MachineContextNullException
        carrier: MachineContextCarrierNullException
        blueprint: MachineContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[MachineContextNullException] | None = None,
            carrier: Optional[MachineContextCarrierNullException] | None = None,
            blueprint: Optional[MachineContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[MachineContextNullException]
            carrier: Optional[MachineContextCarrierNullException]
            blueprint: Optional[MachineContextBlueprintNullException]
        """
        super().__init__(
            model=model or MachineContextNullException(),
            carrier=carrier or MachineContextCarrierNullException(),
            blueprint=blueprint or MachineContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> MachineContextNullException:
        return cast(MachineContextNullException, super().model)
    
    @property
    def carrier(self) -> MachineContextCarrierNullException:
        return cast(MachineContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> MachineContextBlueprintNullException:
        return cast(MachineContextBlueprintNullException, super().blueprint)
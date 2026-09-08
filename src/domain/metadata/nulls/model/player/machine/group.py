# src/domain/metadata/nulls/model/player/machine/group.py

"""
Module: domain.metadata.nulls.model.player.machine.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PlayerNullGroup
from err import MachineBlueprintNullException, MachineCarrierNullException, MachineNullException


class MachineNullGroup(PlayerNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a MachinePlayer's integrity cycle.

    Attributes:
        model: MachineNullException
        carrier: MachineCarrierNullException
        blueprint: MachineBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[MachineNullException] | None = None,
            carrier: Optional[MachineCarrierNullException] | None = None,
            blueprint: Optional[MachineBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[MachineNullException]
            carrier: Optional[MachineCarrierNullException]
            blueprint: Optional[MachineBlueprintNullException]
        """
        super().__init__(
            model = model or MachineNullException(),
            carrier = carrier or MachineCarrierNullException(),
            blueprint = blueprint or MachineBlueprintNullException(),
        )
        
    @property
    def model(self) -> MachineNullException:
        return cast(MachineNullException, super().model)
    
    @property
    def carrier(self) -> MachineCarrierNullException:
        return cast(MachineCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> MachineBlueprintNullException:
        return cast(MachineBlueprintNullException, super().blueprint)
# src/domain/extract/struct/node/warning.extract.py

"""
Module: domain.extract.struct.node.warning.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarningNode, WarningNodeBlueprint, NodePrimeExtract
from transit import WarningNodeCarrier


class EncounterWarningNodePrimeExtract(NodePrimeExtract[EncounterWarningNode]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for WarningNodeValidator.

    Attributes:
        carrier: WarningNodeCarrier
        blueprint: Optional[WarningNodeBlueprint]

    Provides:

    Super Class:
        NodePrimeExtract
    """

    def __init__(
            self,
            carrier: WarningNodeCarrier,
            blueprint: Optional[WarningNodeBlueprint] | None = None,
    ):
        """
        Args:
            carrier: WarningNodeCarrier
            blueprint: Optional[WarningNodeBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> WarningNodeCarrier:
        return cast(WarningNodeCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[WarningNodeBlueprint]:
        return cast(WarningNodeBlueprint, super().blueprint)
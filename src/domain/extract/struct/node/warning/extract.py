# src/domain/extract/struct/node/warning.extract.py

"""
Module: domain.extract.struct.node.warning.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarningNode, EncounterWarningNodeBlueprint, NodePrimeExtract
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
            reference: WarningNodeCarrier,
            blueprint: Optional[EncounterWarningNodeBlueprint] | None = None,
    ):
        """
        Args:
            reference: WarningNodeCarrier
            blueprint: Optional[WarningNodeBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> WarningNodeCarrier:
        return cast(WarningNodeCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[EncounterWarningNodeBlueprint]:
        return cast(EncounterWarningNodeBlueprint, super().blueprint)
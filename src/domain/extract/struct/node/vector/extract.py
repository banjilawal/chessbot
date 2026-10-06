# src/domain/extract/struct/node/vector.extract.py

"""
Module: domain.extract.struct.node.vector.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorNode, VectorNodeBlueprint, NodePrimeExtract
from transit import VectorNodeCarrier


class VectorNodePrimeExtract(NodePrimeExtract[VectorNode]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for VectorNodeValidator.

    Attributes:
        carrier: VectorNodeCarrier
        blueprint: Optional[VectorNodeBlueprint]

    Provides:

    Super Class:
        NodePrimeExtract
    """

    def __init__(
            self,
            reference: VectorNodeCarrier,
            blueprint: Optional[VectorNodeBlueprint] | None = None,
    ):
        """
        Args:
            reference: VectorNodeCarrier
            blueprint: Optional[VectorNodeBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> VectorNodeCarrier:
        return cast(VectorNodeCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[VectorNodeBlueprint]:
        return cast(VectorNodeBlueprint, super().blueprint)
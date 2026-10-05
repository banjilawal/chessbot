# src/domain/metadata/nulls/struct/node/vector/group.py

"""
Module: domain.metadata.nulls.struct.node.vector.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NodeNullGroup, VectorNode
from err import (
    VectorNodeBlueprintNullException, VectorNodeCarrierNullException,
    VectorNodeNullException
)


class VectorNodeNullGroup(NodeNullGroup[VectorNode]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a VectorNode's integrity cycle.

    Attributes:
        model: VectorNodeNullException
        carrier: VectorNodeCarrierNullException
        blueprint:VectorNodeBlueprintNullException

    Provides:

    Super Class:
        NodeNullGroup
    """

    
    def __init__(
            self,
            model: Optional[VectorNodeNullException] | None = None,
            carrier: Optional[VectorNodeCarrierNullException] | None = None,
            blueprint: Optional[VectorNodeBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[VectorNodeNullException]
            carrier: Optional[VectorNodeCarrierNullException]
            blueprint: Optional[VectorNodeBlueprintNullException]
        """
        super().__init__(
            model=model or VectorNodeNullException(),
            carrier=carrier or VectorNodeCarrierNullException(),
            blueprint=blueprint or VectorNodeBlueprintNullException(),
        )
        
    @property
    def struct(self) -> VectorNodeNullException:
        return cast(VectorNodeNullException, super().model)
    
    @property
    def model(self) -> VectorNodeNullException:
        return self.struct
    
    @property
    def carrier(self) -> VectorNodeCarrierNullException:
        return cast(VectorNodeCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> VectorNodeBlueprintNullException:
        return cast(VectorNodeBlueprintNullException, super().blueprint)
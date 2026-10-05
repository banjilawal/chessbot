# src/assurance/depend/toolkit/struct/node/vector/toolkit.py

"""
Module: assurance.depend.toolkit.struct.node.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import NodeValidatorToolkit, VectorNodeDependency
from domain import (
    VectorNode, VectorNodeManifest, VectorNodeNullGroup,
    VectorNodeTypeUnion
)


class VectorNodeValidatorToolkit(NodeValidatorToolkit[VectorNode]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: VectorNodeDependency
            metadata: VectorNodeManifest

    Provides:

    Super Class:
       NodeValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[VectorNodeDependency] | None = None,
            metadata: Optional[VectorNodeManifest] | None = None,
    ):
        """
            wrapper: Optional[VectorNodeDependency]
            metadata: Optional[VectorNodeManifest]
        """
        super().__init__(
            wrapper=wrapper or VectorNodeDependency(),
            metadata=metadata or VectorNodeManifest(),
        )
    
    @property
    def wrapper(self) -> VectorNodeDependency:
        return cast(VectorNodeDependency, super().wrapper)
    
    @property
    def metadata(self) -> VectorNodeManifest:
        return cast(VectorNodeManifest, super().metadata)
    
    @property
    def nulls(self) -> VectorNodeNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> VectorNodeTypeUnion:
        return self.metadata.types
# src/operation/toolkit/builder/space/quadrant/southwest/toolkit.py

"""
Module: operation.toolkit.builder.space.quadrant.southwest.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import SouthwestQuadrantAssembler
from assurance.checker import SouthwestQuadrantRootCertifier
from space import SouthwestQuadrant
from operation.toolkit.builder.space.quadrant.southwest.toolkit import QuadrantBuilderToolkit


class SouthwestQuadrantBuilderToolkit(
    QuadrantBuilderToolkit[SouthwestQuadrant]
):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SouthwestQuadrantBuilder dependencies.

    Attributes:
        assembler: Optional[SouthwestQuadrantAssembler]
        root_certifier: Optional[SouthwestQuadrantRootCertifier]
        
    Provides:
    
    Super Class:
        QuadrantBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[SouthwestQuadrantAssembler] |
                       None = SouthwestQuadrantAssembler(),
            root_certifier: Optional[SouthwestQuadrantRootCertifier] |
                            None = SouthwestQuadrantRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[SouthwestQuadrantAssembler]
            root_certifier: Optional[SouthwestQuadrantRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> SouthwestQuadrantAssembler:
        return cast(SouthwestQuadrantAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> SouthwestQuadrantRootCertifier:
        return cast(SouthwestQuadrantRootCertifier, super().integrity_checker)
# src/operation/toolkit/builder/space/quadrant/southeast/toolkit.py

"""
Module: operation.toolkit.builder.space.quadrant.southeast.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import SoutheastQuadrantAssembler
from assurance.validator import SoutheastQuadrantRootCertifier
from space import SoutheastQuadrant
from operation.toolkit.builder.space.quadrant.southeast.toolkit import QuadrantBuilderToolkit


class SoutheastQuadrantBuilderToolkit(QuadrantBuilderToolkit[SoutheastQuadrant]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SoutheastQuadrantBuilder dependencies.

    Attributes:
        assembler: Optional[SoutheastQuadrantAssembler]
        root_certifier: Optional[SoutheastQuadrantRootCertifier]
        
    Provides:
    
    Super Class:
        QuadrantBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[SoutheastQuadrantAssembler] | None = SoutheastQuadrantAssembler(),
            root_certifier: Optional[SoutheastQuadrantRootCertifier] |  None = SoutheastQuadrantRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[SoutheastQuadrantAssembler]
            root_certifier: Optional[SoutheastQuadrantRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> SoutheastQuadrantAssembler:
        return cast(SoutheastQuadrantAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> SoutheastQuadrantRootCertifier:
        return cast(SoutheastQuadrantRootCertifier, super().integrity_checker)
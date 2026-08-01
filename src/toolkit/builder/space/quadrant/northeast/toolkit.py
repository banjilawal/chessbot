# src/toolkit/builder/space/quadrant/northeast/toolkit.py

"""
Module: toolkit.builder.space.quadrant.northeast.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import NortheastQuadrantAssembler
from assurance.certifier import NortheastQuadrantRootCertifier
from geometry.space import NortheastQuadrant
from toolkit import QuadrantBuilderToolkit


class NortheastQuadrantBuilderToolkit(QuadrantBuilderToolkit[NortheastQuadrant]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles NortheastQuadrantBuilder dependencies.

    Attributes:
        assembler: Optional[NortheastQuadrantAssembler]
        root_certifier: Optional[NortheastQuadrantRootCertifier]
        
    Provides:
    
    Super Class:
        QuadrantBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[NortheastQuadrantAssembler] |
                       None = NortheastQuadrantAssembler(),
            root_certifier: Optional[NortheastQuadrantRootCertifier] |
                            None = NortheastQuadrantRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[NortheastQuadrantAssembler]
            root_certifier: Optional[NortheastQuadrantRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> NortheastQuadrantAssembler:
        return cast(NortheastQuadrantAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> NortheastQuadrantRootCertifier:
        return cast(NortheastQuadrantRootCertifier, super().root_certifier)
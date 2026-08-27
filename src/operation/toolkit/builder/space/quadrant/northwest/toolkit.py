# src/operation/toolkit/builder/space/quadrant/northwest/toolkit.py

"""
Module: operation.toolkit.builder.space.quadrant.northwest.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import NorthwestQuadrantAssembler
from assurance.validator import NorthwestQuadrantRootCertifier
from space import NorthwestQuadrant
from operation.toolkit.builder.space.quadrant.northwest.toolkit import QuadrantBuilderToolkit


class NorthwestQuadrantBuilderToolkit(QuadrantBuilderToolkit[NorthwestQuadrant]):
    """
    Role:
        - Dependency Management
        
    Responsibilities:
        1.  Bundles NorthwestQuadrantBuilder dependencies.

    Attributes:
        assembler: Optional[NorthwestQuadrantAssembler]
        root_certifier: Optional[NorthwestQuadrantRootCertifier]
        
    Provides:
    
    Super Class:
        QuadrantBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[NorthwestQuadrantAssembler] | None = NorthwestQuadrantAssembler(),
            root_certifier: Optional[NorthwestQuadrantRootCertifier] |  None = NorthwestQuadrantRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[NorthwestQuadrantAssembler]
            root_certifier: Optional[NorthwestQuadrantRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> NorthwestQuadrantAssembler:
        return cast(NorthwestQuadrantAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> NorthwestQuadrantRootCertifier:
        return cast(NorthwestQuadrantRootCertifier, super().integrity_checker)
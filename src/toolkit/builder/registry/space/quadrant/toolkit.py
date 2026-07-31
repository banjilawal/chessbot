# src/toolkit/builder/registry/space/quadrantReservoir/toolkit.py

"""
Module: toolkit.builder.registry.space.quadrantReservoir.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from assembler import QuadrantReservoirAssembler
from geometry.registry import QuadrantReservoir
from root import QuadrantReservoirRootCertifier
from toolkit import SpaceReservoirBuilderToolkit


class QuadrantReservoirBuilderToolkit(SpaceReservoirBuilderToolkit[QuadrantReservoir]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles QuadrantReservoirBuilder dependencies.

    Attributes:
        assembler: [QuadrantReservoirAssembler[T]],
        root_certifier: [QuadrantReservoirRootCertifier[T]]
        
    Provides:
    
    Super Class:
        SpaceReservoirBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: QuadrantReservoirAssembler,
            root_certifier: QuadrantReservoirRootCertifier,
    ):
        """
        Args:
            assembler: [QuadrantReservoirAssembler[T]],
            root_certifier: [QuadrantReservoirRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> QuadrantReservoirAssembler:
        return cast(QuadrantReservoirAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> QuadrantReservoirRootCertifier:
        return cast(QuadrantReservoirRootCertifier, super().root_certifier)
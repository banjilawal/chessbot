# src/toolkit/builder/registry/space/axisReservoir/toolkit.py

"""
Module: toolkit.builder.registry.space.axisReservoir.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from assembler import AxisReservoirAssembler
from geometry.registry import AxisReservoir
from core.certifier import AxisReservoirRootCertifier
from toolkit import SpaceReservoirBuilderToolkit


class AxisReservoirBuilderToolkit(SpaceReservoirBuilderToolkit[AxisReservoir]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles AxisReservoirBuilder dependencies.

    Attributes:
        assembler: [AxisReservoirAssembler[T]],
        root_certifier: [AxisReservoirRootCertifier[T]]
        
    Provides:
    
    Super Class:
        SpaceReservoirBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: AxisReservoirAssembler,
            root_certifier: AxisReservoirRootCertifier,
    ):
        """
        Args:
            assembler: [AxisReservoirAssembler[T]],
            root_certifier: [AxisReservoirRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> AxisReservoirAssembler:
        return cast(AxisReservoirAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> AxisReservoirRootCertifier:
        return cast(AxisReservoirRootCertifier, super().root_certifier)
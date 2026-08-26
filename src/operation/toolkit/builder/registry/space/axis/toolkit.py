# src/operation/toolkit/builder/registry/space/axisReservoir/toolkit.py

"""
Module: operation.toolkit.builder.registry.space.axisReservoir.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from fabrication.builder import AxisReservoirAssembler
from topology.registry import AxisReservoir
from assurance.validator import AxisReservoirRootCertifier
from operation.toolkit.builder.registry.space.axis.toolkit import SpaceReservoirBuilderToolkit


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
        return cast(AxisReservoirRootCertifier, super().integrity_checker)
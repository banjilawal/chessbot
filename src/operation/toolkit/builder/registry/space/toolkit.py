# src/operation/toolkit/builder/registry/space/toolkit.py

"""
Module: operation.toolkit.builder.registry.space.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.builder import SpaceReservoirBuilder
from assurance.checker import SpaceReservoirCertifier

from operation.toolkit.builder.registry.space.toolkit import BuilderToolkit


T = TypeVar("T", bound="SpaceReservoir")

class SpaceReservoirBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SpaceReservoirBuilder dependencies.

    Attributes:
        assembler: [SpaceReservoirAssembler[T]],
        root_certifier: [SpaceReservoirRootCertifier[T]]
        
    Provides:
    
    Super Class:
        BuilderToolkit
    """
    
    def __init__(
            self,
            assembler: SpaceReservoirBuilder[T],
            root_certifier: SpaceReservoirCertifier[T],
    ):
        """
        Args:
            assembler: [SpaceReservoirAssembler[T]],
            root_certifier: [SpaceReservoirRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> SpaceReservoirBuilder[T]:
        return cast(SpaceReservoirBuilder[T], super()._assembler)
        
    @property
    def root_certifier(self) -> SpaceReservoirCertifier[T]:
        return cast(SpaceReservoirCertifier[T], super().integrity_checker)
# src/toolkit/builder/registry/space/toolkit.py

"""
Module: toolkit.builder.registry.space.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.assembler import SpaceReservoirAssembler
from assurance.certifier import SpaceReservoirCertifier

from toolkit import BuilderToolkit


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
            assembler: SpaceReservoirAssembler[T],
            root_certifier: SpaceReservoirCertifier[T],
    ):
        """
        Args:
            assembler: [SpaceReservoirAssembler[T]],
            root_certifier: [SpaceReservoirRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> SpaceReservoirAssembler[T]:
        return cast(SpaceReservoirAssembler[T], super()._assembler)
        
    @property
    def root_certifier(self) -> SpaceReservoirCertifier[T]:
        return cast(SpaceReservoirCertifier[T], super()._root_certifier)
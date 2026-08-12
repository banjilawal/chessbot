# src/toolkit/builder/space/toolkit.py

"""
Module: toolkit.builder.space.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.assembler import SpaceAssembler
from assurance.certifier import SpaceCertifier
from toolkit.builder.space.toolkit import BuilderToolkit


T = TypeVar("T", bound="Space")

class SpaceBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SpaceBuilder dependencies.

    Attributes:
        assembler: [SpaceAssembler[T]],
        root_certifier: [SpaceRootCertifier[T]]
        
    Provides:
    
    Super Class:
        BuilderToolkit
    """
    
    def __init__(
            self,
            assembler: SpaceAssembler[T],
            root_certifier: SpaceCertifier[T],
    ):
        """
        Args:
            assembler: [SpaceAssembler[T]],
            root_certifier: [SpaceRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> SpaceAssembler[T]:
        return cast(SpaceAssembler[T], super()._assembler)
        
    @property
    def root_certifier(self) -> SpaceCertifier[T]:
        return cast(SpaceCertifier[T], super()._root_certifier)
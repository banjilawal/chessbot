# src/toolkit/builder/space/quadrant/toolkit.py

"""
Module: toolkit.builder.space.quadrant.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from assembler import QuadrantAssembler
from root import QuadrantRootCertifier
from toolkit import SpaceBuilderToolkit

T = TypeVar("T", bound="Quadrant")

class QuadrantBuilderToolkit(SpaceBuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles QuadrantBuilder dependencies.

    Attributes:
        assembler: [QuadrantAssembler[T]],
        root_certifier: [QuadrantRootCertifier[T]]
        
    Provides:
    
    Super Class:
        SpaceBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: QuadrantAssembler[T],
            root_certifier: QuadrantRootCertifier[T],
    ):
        """
        Args:
            assembler: [QuadrantAssembler[T]],
            root_certifier: [QuadrantRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> [QuadrantAssembler[T]]:
        return cast(QuadrantAssembler[T], super()._assembler)
        
    @property
    def root_certifier(self) -> QuadrantRootCertifier[T]:
        return cast(QuadrantRootCertifier[T], super()._root_certifier)
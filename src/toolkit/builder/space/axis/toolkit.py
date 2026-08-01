# src/toolkit/builder/space/axis/toolkit.py

"""
Module: toolkit.builder.space.axis.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.assembler import AxisAssembler
from assurance.certifier import AxisRootCertifier
from toolkit import SpaceBuilderToolkit

T = TypeVar("T", bound="Axis")

class AxisBuilderToolkit(SpaceBuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles AxisBuilder dependencies.

    Attributes:
        assembler: [AxisAssembler[T]],
        root_certifier: [AxisRootCertifier[T]]
        
    Provides:
    
    Super Class:
        SpaceBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: [AxisAssembler[T]],
            root_certifier: [AxisRootCertifier[T]],
    ):
        """
        Args:
            assembler: [AxisAssembler[T]],
            root_certifier: [AxisRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> [AxisAssembler[T]]:
        return cast([AxisAssembler[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [AxisRootCertifier[T]]:
        return cast([AxisRootCertifier[T]], super()._root_certifier)
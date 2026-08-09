# src/kit/toolkit/builder/space/axis/north/toolkit.py

"""
Module: kit.toolkit.builder.space.axis.north.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.assembler import NorthAxisAssembler
from assurance.certifier import NorthAxisRootCertifier
from space import NorthAxis
from kit.toolkit import AxisBuilderToolkit


class NorthAxisBuilderToolkit(AxisBuilderToolkit[NorthAxis]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles NorthAxisBuilder dependencies.

    Attributes:
        assembler: Optional[NorthAxisAssembler]
        root_certifier: Optional[NorthAxisRootCertifier]
        
    Provides:
    
    Super Class:
        AxisBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[NorthAxisAssembler] | None = NorthAxisAssembler(),
            root_certifier: Optional[NorthAxisRootCertifier] |  None = NorthAxisRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[NorthAxisAssembler]
            root_certifier: Optional[NorthAxisRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> NorthAxisAssembler:
        return cast(NorthAxisAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> NorthAxisRootCertifier:
        return cast(NorthAxisRootCertifier, super().root_certifier)
    
# src/kit/toolkit/builder/space/axis/south/toolkit.py

"""
Module: kit.toolkit.builder.space.axis.south.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.assembler import SouthAxisAssembler
from assurance.certifier import SouthAxisRootCertifier
from space import SouthAxis
from kit.toolkit import AxisBuilderToolkit


class SouthAxisBuilderToolkit(AxisBuilderToolkit[SouthAxis]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles SouthAxisBuilder dependencies.

    Attributes:
        assembler: Optional[SouthAxisAssembler]
        root_certifier: Optional[SouthAxisRootCertifier]
        
    Provides:
    
    Super Class:
        AxisBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[SouthAxisAssembler] | None = SouthAxisAssembler(),
            root_certifier: Optional[SouthAxisRootCertifier] |  None = SouthAxisRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[SouthAxisAssembler]
            root_certifier: Optional[SouthAxisRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> SouthAxisAssembler:
        return cast(SouthAxisAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> SouthAxisRootCertifier:
        return cast(SouthAxisRootCertifier, super().root_certifier)
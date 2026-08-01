# src/toolkit/builder/space/axis/west/toolkit.py

"""
Module: toolkit.builder.space.axis.west.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import WestAxisAssembler
from assurance.certifier import WestAxisRootCertifier
from geometry.space import WestAxis
from toolkit import AxisBuilderToolkit


class WestAxisBuilderToolkit(AxisBuilderToolkit[WestAxis]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles WestAxisBuilder dependencies.

    Attributes:
        assembler: Optional[WestAxisAssembler]
        root_certifier: Optional[WestAxisRootCertifier]
        
    Provides:
    
    Super Class:
        AxisBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[WestAxisAssembler] | None = WestAxisAssembler(),
            root_certifier: Optional[WestAxisRootCertifier] |  None = WestAxisRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[WestAxisAssembler]
            root_certifier: Optional[WestAxisRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> WestAxisAssembler:
        return cast(WestAxisAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> WestAxisRootCertifier:
        return cast(WestAxisRootCertifier, super().root_certifier)
# src/operation/toolkit/builder/space/axis/east/toolkit.py

"""
Module: operation.toolkit.builder.space.axis.east.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import EastAxisAssembler
from assurance.checker import EastAxisRootCertifier
from space import EastAxis
from operation.toolkit.builder.space.axis.east.toolkit import AxisBuilderToolkit


class EastAxisBuilderToolkit(AxisBuilderToolkit[EastAxis]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles EastAxisBuilder dependencies.

    Attributes:
        assembler: Optional[EastAxisAssembler]
        root_certifier: Optional[EastAxisRootCertifier]
        
    Provides:
    
    Super Class:
        AxisBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[EastAxisAssembler] | None = EastAxisAssembler(),
            root_certifier: Optional[EastAxisRootCertifier] |  None = EastAxisRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[EastAxisAssembler]
            root_certifier: Optional[EastAxisRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

    @property
    def assembler(self) -> EastAxisAssembler:
        return cast(EastAxisAssembler, super().assembler)
        
    @property
    def root_certifier(self) -> EastAxisRootCertifier:
        return cast(EastAxisRootCertifier, super().integrity_checker)
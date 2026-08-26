# src/operation/toolkit/builder/model/coord/toolkit.py

"""
Module: operation.toolkit.builder.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import CoordAssembler
from domain.model import Coord
from assurance.checker import CoordRootCertifier
from operation.toolkit.builder.model.coord.toolkit import ModelBuilderToolkit


class CoordBuilderToolkit(ModelBuilderToolkit[Coord]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles CoordBuilder dependencies.

    Attributes:
        assembler: Optional[CoordAssembler]
        root_certifier: Optional[CoordRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[CoordAssembler] | None = CoordAssembler(),
            root_certifier: Optional[CoordRootCertifier] |
                            None = CoordRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[CoordAssembler]
            root_certifier: Optional[CoordRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> CoordAssembler:
        return cast(CoordAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> CoordRootCertifier:
        return cast(CoordRootCertifier, super().integrity_checker)
    

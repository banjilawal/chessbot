# src/toolkit/builder/model/vector/toolkit.py

"""
Module: toolkit.builder.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import VectorAssembler
from model import Vector
from root import VectorRootCertifier
from toolkit import ModelBuilderToolkit


class VectorBuilderToolkit(ModelBuilderToolkit[Vector]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorBuilder dependencies.

    Attributes:
        assembler: Optional[VectorAssembler]
        root_certifier: Optional[VectorRootCertifier]
            
    Provides:

    Super Class:
        ModelBuildToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorAssembler] | None = VectorAssembler(),
            root_certifier: Optional[VectorRootCertifier] |
                            None = VectorRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorAssembler]
            root_certifier: Optional[VectorRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> VectorAssembler:
        return cast(VectorAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> VectorRootCertifier:
        return cast(VectorRootCertifier, super().root_certifier)
    

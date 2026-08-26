# src/operation/toolkit/builder/model/vector/toolkit.py

"""
Module: operation.toolkit.builder.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import VectorAssembler
from domain.model import Vector
from assurance.validator import VectorIntegrityValidator
from operation.toolkit.builder.model.vector.toolkit import ModelBuilderToolkit


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
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorAssembler] | None = VectorAssembler(),
            root_certifier: Optional[VectorIntegrityValidator] |
                            None = VectorIntegrityValidator(),
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
    def root_certifier(self) -> VectorIntegrityValidator:
        return cast(VectorIntegrityValidator, super().integrity_checker)
    

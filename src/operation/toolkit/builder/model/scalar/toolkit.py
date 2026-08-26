# src/operation/toolkit/builder/model/scalar/toolkit.py

"""
Module: operation.toolkit.builder.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import ScalarAssembler
from domain.model import Scalar
from assurance.checker import ScalarRootCertifier
from operation.toolkit.builder.model.scalar.toolkit import ModelBuilderToolkit


class ScalarBuilderToolkit(ModelBuilderToolkit[Scalar]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ScalarBuilder dependencies.

    Attributes:
        assembler: Optional[ScalarAssembler]
        root_certifier: Optional[ScalarRootCertifier]
            
    Provides:

    Super Class:
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[ScalarAssembler] | None = ScalarAssembler(),
            root_certifier: Optional[ScalarRootCertifier] |
                            None = ScalarRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[ScalarAssembler]
            root_certifier: Optional[ScalarRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> ScalarAssembler:
        return cast(ScalarAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> ScalarRootCertifier:
        return cast(ScalarRootCertifier, super().integrity_checker)
    

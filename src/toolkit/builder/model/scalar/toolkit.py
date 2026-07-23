# src/toolkit/builder/model/scalar/toolkit.py

"""
Module: toolkit.builder.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import ScalarAssembler
from model import Scalar
from root import ScalarRootCertifier
from toolkit import ModelBuilderToolkit


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
        ModelBuildToolkit
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
        return cast(ScalarRootCertifier, super().root_certifier)
    

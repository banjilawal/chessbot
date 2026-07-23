# src/toolkit/builder/toggle/vector/toolkit.py

"""
Module: toolkit.builder.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import  VectorToggleAssembler
from root import VectorToggleRootCertifier
from toggle import VectorToggle
from toolkit import ToggleBuilderToolkit


class VectorToggleBuilderToolkit(ToggleBuilderToolkit[VectorToggle]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorToggleBuilderToolkit dependencies.

    Attributes:
        assembler: Optional[VectorToggleAssembler]
        root_certifier: Optional[VectorToggleRootCertifier]
            
    Provides:

    Super Class:
        ToggleBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorToggleAssembler] | None = VectorToggleAssembler(),
            root_certifier: Optional[VectorToggleRootCertifier] |
                            None = VectorToggleRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorToggleAssembler]
            root_certifier: Optional[VectorToggleRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> VectorToggleAssembler:
        return cast(VectorToggleAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> VectorToggleRootCertifier:
        return cast(VectorToggleRootCertifier, super().root_certifier)
    

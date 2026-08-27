# src/operation/toolkit/builder/toggle/vector/toolkit.py

"""
Module: operation.toolkit.builder.toggle.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import  CartesianToggleAssembler
from assurance.validator import CartesianToggleRootCertifier
from domain.structure.toggle import CartesianToggle
from operation.toolkit.builder.toggle.vector.toolkit import ToggleBuilderToolkit


class CartesianToggleBuilderToolkit(ToggleBuilderToolkit[CartesianToggle]):
    """
    Role:
        - Dependency Management
        
    Responsibilities:
        1.  Bundles CartesianToggleBuilderToolkit dependencies.

    Attributes:
        assembler: Optional[CartesianToggleAssembler]
        root_certifier: Optional[CartesianToggleRootCertifier]
            
    Provides:

    Super Class:
        ToggleBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[CartesianToggleAssembler] | None = CartesianToggleAssembler(),
            root_certifier: Optional[CartesianToggleRootCertifier] |
                            None = CartesianToggleRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[CartesianToggleAssembler]
            root_certifier: Optional[CartesianToggleRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> CartesianToggleAssembler:
        return cast(CartesianToggleAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> CartesianToggleRootCertifier:
        return cast(CartesianToggleRootCertifier, super().integrity_checker)
    

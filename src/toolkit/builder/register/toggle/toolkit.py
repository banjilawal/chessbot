# src/toolkit/builder/register/toggle/toolkit.py

"""
Module: toolkit.builder.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.assembler import VectorToggleRegisterAssembler
from domain.structure.register import CartesianToggleRegister
from assurance.checker import VectorToggleRegisterCertifier
from toolkit.builder.register.toggle.toolkit import RegisterBuilderToolkit


class VectorToggleRegisterBuilderToolkit(RegisterBuilderToolkit[CartesianToggleRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorToggleRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[VectorToggleRegisterAssembler]
        root_certifier: Optional[VectorToggleRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorToggleRegisterAssembler] |
                       None = VectorToggleRegisterAssembler(),
            root_certifier: Optional[VectorToggleRegisterCertifier] |
                            None = VectorToggleRegisterCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorToggleRegisterAssembler]
            root_certifier: Optional[VectorToggleRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> VectorToggleRegisterAssembler:
        return cast(VectorToggleRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> VectorToggleRegisterCertifier:
        return cast(VectorToggleRegisterCertifier, super().integrity_checker)
    

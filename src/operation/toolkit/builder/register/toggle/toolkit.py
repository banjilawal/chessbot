# src/operation/toolkit/builder/register/toggle/toolkit.py

"""
Module: operation.toolkit.builder.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import CartesianToggleRegisterAssembler
from domain.structure.register import CartesianToggleRegister
from assurance.validator import CartesianToggleRegisterCertifier
from operation.toolkit.builder.register.toggle.toolkit import RegisterBuilderToolkit


class CartesianToggleRegisterBuilderToolkit(RegisterBuilderToolkit[CartesianToggleRegister]):
    """
    Role:
        - Dependency Management
        
    Responsibilities:
        1.  Bundles CartesianToggleRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[CartesianToggleRegisterAssembler]
        root_certifier: Optional[CartesianToggleRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[CartesianToggleRegisterAssembler] |
                       None = CartesianToggleRegisterAssembler(),
            root_certifier: Optional[CartesianToggleRegisterCertifier] |
                            None = CartesianToggleRegisterCertifier(),
    ):
        """
        Args:
            assembler: Optional[CartesianToggleRegisterAssembler]
            root_certifier: Optional[CartesianToggleRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> CartesianToggleRegisterAssembler:
        return cast(CartesianToggleRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> CartesianToggleRegisterCertifier:
        return cast(CartesianToggleRegisterCertifier, super().integrity_checker)
    

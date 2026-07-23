# src/toolkit/builder/register/toggle/toolkit.py

"""
Module: toolkit.builder.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import VectorToggleRegisterAssembler
from register import VectorToggleRegister
from root import VectorToggleRegisterCertifier
from toolkit import RegisterBuilderToolkit


class VectorToggleRegisterBuilderToolkit(RegisterBuilderToolkit[VectorToggleRegister]):
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
        return cast(VectorToggleRegisterCertifier, super().root_certifier)
    

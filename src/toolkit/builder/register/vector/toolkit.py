# src/toolkit/builder/register/vector/toolkit.py

"""
Module: toolkit.builder.register.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import VectorRegisterAssembler
from register import VectorRegister
from root import VectorRegisterRootCertifier
from toolkit import RegisterBuilderToolkit


class VectorRegisterBuilderToolkit(RegisterBuilderToolkit[VectorRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles VectorRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[VectorRegisterAssembler]
        root_certifier: Optional[VectorRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[VectorRegisterAssembler] |
                       None = VectorRegisterAssembler(),
            root_certifier: Optional[VectorRegisterRootCertifier] |
                            None = VectorRegisterRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[VectorRegisterAssembler]
            root_certifier: Optional[VectorRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> VectorRegisterAssembler:
        return cast(VectorRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> VectorRegisterRootCertifier:
        return cast(VectorRegisterRootCertifier, super().root_certifier)
    

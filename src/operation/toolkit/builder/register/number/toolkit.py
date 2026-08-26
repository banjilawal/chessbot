# src/operation/toolkit/builder/register/number/toolkit.py

"""
Module: operation.toolkit.builder.register.number.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.builder import NumberRegisterAssembler
from domain.structure.register import NumberRegister
from assurance.validator import NumberRegisterRootCertifier
from operation.toolkit.builder.register.number.toolkit import RegisterBuilderToolkit


class NumberRegisterBuilderToolkit(RegisterBuilderToolkit[NumberRegister]):
    """
    Role:
        -  Dependency Management
        
    Responsibilities:
        1.  Bundles NumberRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[NumberRegisterAssembler]
        root_certifier: Optional[NumberRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[NumberRegisterAssembler] |
                       None = NumberRegisterAssembler(),
            root_certifier: Optional[NumberRegisterRootCertifier] |
                            None = NumberRegisterRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[NumberRegisterAssembler]
            root_certifier: Optional[NumberRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> NumberRegisterAssembler:
        return cast(NumberRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> NumberRegisterRootCertifier:
        return cast(NumberRegisterRootCertifier, super().integrity_checker)
    

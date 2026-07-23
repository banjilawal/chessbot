# src/toolkit/builder/register/toggle/toolkit.py

"""
Module: toolkit.builder.register.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import ToggleRegisterAssembler
from register import ToggleRegister
from root import ToggleRegisterRootCertifier
from toolkit import RegisterBuildToolkit


class ToggleRegisterBuildToolkit(RegisterBuildToolkit[ToggleRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ToggleRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[ToggleRegisterAssembler]
        root_certifier: Optional[ToggleRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuildToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[ToggleRegisterAssembler] |
                       None = ToggleRegisterAssembler(),
            root_certifier: Optional[ToggleRegisterRootCertifier] |
                            None = ToggleRegisterRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[ToggleRegisterAssembler]
            root_certifier: Optional[ToggleRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> ToggleRegisterAssembler:
        return cast(ToggleRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> ToggleRegisterRootCertifier:
        return cast(ToggleRegisterRootCertifier, super().root_certifier)
    

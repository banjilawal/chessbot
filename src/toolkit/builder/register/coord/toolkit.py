# src/toolkit/builder/register/coord/toolkit.py

"""
Module: toolkit.builder.register.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import CoordRegisterAssembler
from register import CoordRegister
from root import CoordRegisterRootCertifier
from toolkit import RegisterBuilderToolkit


class CoordRegisterBuilderToolkit(RegisterBuilderToolkit[CoordRegister]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles CoordRegisterRegisterBuilder dependencies.

    Attributes:
        assembler: Optional[CoordRegisterAssembler]
        root_certifier: Optional[CoordRegisterRootCertifier]
            
    Provides:

    Super Class:
        RegisterBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[CoordRegisterAssembler] |
                       None = CoordRegisterAssembler(),
            root_certifier: Optional[CoordRegisterRootCertifier] |
                            None = CoordRegisterRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[CoordRegisterAssembler]
            root_certifier: Optional[CoordRegisterRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> CoordRegisterAssembler:
        return cast(CoordRegisterAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> CoordRegisterRootCertifier:
        return cast(CoordRegisterRootCertifier, super().root_certifier)
    

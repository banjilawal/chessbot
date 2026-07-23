# src/toolkit/builder/model/token/toolkit.py

"""
Module: toolkit.builder.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from assembler import TokenAssembler
from model import Token
from root import TokenRootCertifier
from toolkit import ModelBuilderToolkit


class TokenBuilderToolkit(ModelBuilderToolkit[Token]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles TokenBuilder dependencies.

    Attributes:
        assembler: Optional[TokenAssembler]
        root_certifier: Optional[TokenRootCertifier]
            
    Provides:

    Super Class:
        ModelBuildToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[TokenAssembler] | None = TokenAssembler(),
            root_certifier: Optional[TokenRootCertifier] |
                            None = TokenRootCertifier(),
    ):
        """
        Args:
            assembler: Optional[TokenAssembler]
            root_certifier: Optional[TokenRootCertifier]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)
        
    @property
    def assembler(self) -> TokenAssembler:
        return cast(TokenAssembler, super().assembler)
    
    @property
    def root_certifier(self) -> TokenRootCertifier:
        return cast(TokenRootCertifier, super().root_certifier)
    

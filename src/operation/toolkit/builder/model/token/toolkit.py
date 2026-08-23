# src/operation/toolkit/builder/model/token/toolkit.py

"""
Module: operation.toolkit.builder.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.assembler import TokenAssembler
from domain.model import Token
from assurance.checker import TokenIntegrityChecker
from operation.toolkit.builder.model.token.toolkit import ModelBuilderToolkit


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
        ModelBuilderToolkit
    """
    
    def __init__(
            self,
            assembler: Optional[TokenAssembler] | None = TokenAssembler(),
            root_certifier: Optional[TokenIntegrityChecker] |
                            None = TokenIntegrityChecker(),
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
    def root_certifier(self) -> TokenIntegrityChecker:
        return cast(TokenIntegrityChecker, super().integrity_checker)
    

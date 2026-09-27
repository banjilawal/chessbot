# src/assurance/depend/toolkit/model/token/toolkit.py

"""
Module: assurance.depend.toolkit.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import KingTokenValidator, ModelValidatorToolkit, TokenWrapperDependency
from domain import Token, TokenManifest, TokenNullGroup, TokenTypeUnion


class TokenValidatorToolkit(ModelValidatorToolkit[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Token attribute validators and type metadata.

    Attributes:
        helper: TokenManifest
        metadata: TokenHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[TokenManifest] | None = None,
            wrapper: Optional[TokenWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[TokenManifest]
            metadata: Optional[TokenHelperTable]
        """
        super().__init__(
            wrapper=wrapper or TokenWrapperDependency(),
            metadata=metadata or TokenManifest(),
        )
    
    @property
    def wrapper(self) -> TokenWrapperDependency:
        return cast(TokenWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> TokenManifest:
        return cast(TokenManifest, super().metadata)
    
    @property
    def nulls(self) -> TokenNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TokenTypeUnion:
        return self.metadata.types
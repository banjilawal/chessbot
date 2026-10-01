# src/assurance/depend/toolkit/model/token/toolkit.py

"""
Module: assurance.depend.toolkit.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, TokenWrapperDependency
from authorization import HomeSquareExtractor
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
        home_square_extractor: HomeSquareExtractor

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    _home_square_extractor: HomeSquareExtractor
    
    
    def __init__(
            self,
            metadata: Optional[TokenManifest] | None = None,
            wrapper: Optional[TokenWrapperDependency] | None = None,
            home_square_extractor: Optional[HomeSquareExtractor] | None = None,
    ):
        """
        Args:
            wrapper: Optional[TokenManifest]
            metadata: Optional[TokenHelperTable]
            home_square_extractor: Optional[HomeSquareExtractor]
        """
        super().__init__(
            wrapper=wrapper or TokenWrapperDependency(),
            metadata=metadata or TokenManifest(),
        )
        self._home_square_extractor = home_square_extractor or HomeSquareExtractor()
    
    @property
    def wrapper(self) -> TokenWrapperDependency:
        return cast(TokenWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> TokenManifest:
        return cast(TokenManifest, super().metadata)
    
    @property
    def home_square_extractor(self) -> HomeSquareExtractor:
        return self._home_square_extractor
    
    @property
    def nulls(self) -> TokenNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TokenTypeUnion:
        return self.metadata.types
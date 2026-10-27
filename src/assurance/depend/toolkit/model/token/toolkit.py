# src/assurance/depend/toolkit/model/token/toolkit.py

"""
Module: assurance.depend.toolkit.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, TokenServiceDependency
from authorization import HomeSquareExtractor
from domain import Token, TokenManifest, TokenNullWarningSet, TokenLayer


class TokenLayerToolkit(ModelLayerToolkit[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Token attribute validators and type manifest.

    Attributes:
        helper: TokenManifest
        manifest: TokenServiceDependency
        home_square_extractor: HomeSquareExtractor

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    _home_square_extractor: HomeSquareExtractor
    
    
    def __init__(
            self,
            manifest: Optional[TokenManifest] | None = None,
            dependency: Optional[TokenServiceDependency] | None = None,
            home_square_extractor: Optional[HomeSquareExtractor] | None = None,
    ):
        """
        Args:
            dependency: Optional[TokenManifest]
            manifest: Optional[TokenServiceDependency]
            home_square_extractor: Optional[HomeSquareExtractor]
        """
        super().__init__(
            dependency=dependency or TokenServiceDependency(),
            manifest=manifest or TokenManifest(),
        )
        self._home_square_extractor = home_square_extractor or HomeSquareExtractor()
    
    @property
    def dependency(self) -> TokenServiceDependency:
        return cast(TokenServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> TokenManifest:
        return cast(TokenManifest, super().manifest)
    
    @property
    def home_square_extractor(self) -> HomeSquareExtractor:
        return self._home_square_extractor
    
    @property
    def nulls(self) -> TokenNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> TokenLayer:
        return self.manifest.types
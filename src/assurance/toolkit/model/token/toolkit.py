# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import TokenHelperTable, ModelValidationToolkit
from domain import Token, TokenManifest



class TokenValidationToolkit(ModelValidationToolkit[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Token attribute validators and type metadata.

    Attributes:
        helper: Optional[TokenManifest]
        metadata: Optional[TokenHelperTable]

    Provides:

    Super Class:
    """
    _metadata: TokenManifest
    _helper: TokenHelperTable
    
    def __init__(
            self,
            metadata: Optional[TokenManifest] | None = None,
            helper: Optional[TokenHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[TokenManifest]
            metadata: Optional[TokenHelperTable]
        """
        self._helper = helper or TokenHelperTable()
        self._metadata = metadata or TokenManifest()
    
    @property
    def helper(self) -> TokenHelperTable:
        return cast(TokenHelperTable, super().helper)
    
    @property
    def metadata(self) -> TokenManifest:
        return cast(TokenManifest, super().metadata)

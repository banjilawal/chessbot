# src/assurance/depend/toolkit/struct/chart/token/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartValidatorToolkit, TokenChartDependency
from domain import (
    TokenChart, TokenChartManifest, TokenChartNullGroup,
    TokenChartTypeUnion
)


class TokenChartValidatorToolkit(ChartValidatorToolkit[TokenChart]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: TokenChartDependency
            metadata: TokenChartManifest

    Provides:

    Super Class:
       ChartValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[TokenChartDependency] | None = None,
            metadata: Optional[TokenChartManifest] | None = None,
    ):
        """
            wrapper: Optional[TokenChartDependency]
            metadata: Optional[TokenChartManifest]
        """
        super().__init__(
            wrapper=wrapper or TokenChartDependency(),
            metadata=metadata or TokenChartManifest(),
        )
    
    @property
    def wrapper(self) -> TokenChartDependency:
        return cast(TokenChartDependency, super().wrapper)
    
    @property
    def metadata(self) -> TokenChartManifest:
        return cast(TokenChartManifest, super().metadata)
    
    @property
    def nulls(self) -> TokenChartNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TokenChartTypeUnion:
        return self.metadata.types
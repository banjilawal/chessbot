# src/domain/metadata/nulls/structure/chart/token/group.py

"""
Module: domain.metadata.nulls.structure.chart.token.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartNullGroup, TokenChart
from err import (
    TokenChartBlueprintNullException, TokenChartCarrierNullException,
    TokenChartNullException
)


class TokenChartNullGroup(ChartNullGroup[TokenChart]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a TokenChart's integrity cycle.

    Attributes:
        model: TokenChartNullException
        carrier: TokenChartCarrierNullException
        blueprint:TokenChartBlueprintNullException

    Provides:

    Super Class:
        ChartNullGroup
    """

    
    def __init__(
            self,
            model: Optional[TokenChartNullException] | None = None,
            carrier: Optional[TokenChartCarrierNullException] | None = None,
            blueprint: Optional[TokenChartBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TokenChartNullException]
            carrier: Optional[TokenChartCarrierNullException]
            blueprint: Optional[TokenChartBlueprintNullException]
        """
        super().__init__(
            model=model or TokenChartNullException(),
            carrier=carrier or TokenChartCarrierNullException(),
            blueprint=blueprint or TokenChartBlueprintNullException(),
        )
        
    @property
    def structure(self) -> TokenChartNullException:
        return cast(TokenChartNullException, super().model)
    
    @property
    def model(self) -> TokenChartNullException:
        return self.structure
    
    @property
    def carrier(self) -> TokenChartCarrierNullException:
        return cast(TokenChartCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TokenChartBlueprintNullException:
        return cast(TokenChartBlueprintNullException, super().blueprint)
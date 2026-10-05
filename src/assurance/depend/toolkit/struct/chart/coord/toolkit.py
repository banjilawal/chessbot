# src/assurance/depend/toolkit/struct/chart/coord/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartValidatorToolkit, CoordChartDependency
from domain import (
    CoordChart, CoordChartManifest, CoordChartNullGroup,
    CoordChartTypeUnion
)


class CoordChartValidatorToolkit(ChartValidatorToolkit[CoordChart]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: CoordChartDependency
            metadata: CoordChartManifest

    Provides:

    Super Class:
       ChartValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[CoordChartDependency] | None = None,
            metadata: Optional[CoordChartManifest] | None = None,
    ):
        """
            wrapper: Optional[CoordChartDependency]
            metadata: Optional[CoordChartManifest]
        """
        super().__init__(
            wrapper=wrapper or CoordChartDependency(),
            metadata=metadata or CoordChartManifest(),
        )
    
    @property
    def wrapper(self) -> CoordChartDependency:
        return cast(CoordChartDependency, super().wrapper)
    
    @property
    def metadata(self) -> CoordChartManifest:
        return cast(CoordChartManifest, super().metadata)
    
    @property
    def nulls(self) -> CoordChartNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> CoordChartTypeUnion:
        return self.metadata.types
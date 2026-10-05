# src/assurance/depend/wrapper/struct/chart/depend.py

"""
Module: assurance.depend.wrapper.struct.chart.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ChartDependency
from domain import CoordChart
from exchange import CoordValidationResponseWrapper


class CoordChartDependency(ChartDependency[CoordChart]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Chart needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        coord: CoordValidationResponseWrapper

    Provides:

    Super Class:
        ChartDependency
    """
    _coord: CoordValidationResponseWrapper
    
    def __init__(
            self,
            coord: Optional[CoordValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            coord: Optional[CoordValidationResponseWrapper]
        """
        super().__init__()
        self._coord = coord or CoordValidationResponseWrapper()
        
    @property
    def coord(self) -> CoordValidationResponseWrapper:
        return self._coord
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
from domain import Participation
from exchange import TokenValidationResponseWrapper


class ParticipationDependency(ChartDependency[Participation]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Chart needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        token: TokenValidationResponseWrapper

    Provides:

    Super Class:
        ChartDependency
    """
    _token: TokenValidationResponseWrapper
    
    def __init__(
            self,
            token: Optional[TokenValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationResponseWrapper]
        """
        super().__init__()
        self._token = token or TokenValidationResponseWrapper()
        
    @property
    def token(self) -> TokenValidationResponseWrapper:
        return self._token
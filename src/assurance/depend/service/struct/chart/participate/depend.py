# src/assurance/depend/service/struct/chart/depend.py

"""
Module: assurance.depend.service.struct.chart.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ChartDependency
from domain import Participation
from exchange import TokenValidationService


class ParticipationDependency(ChartDependency[Participation]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Chart needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        token: TokenValidationService

    Provides:

    Super Class:
        ChartDependency
    """
    _token: TokenValidationService
    
    def __init__(
            self,
            token: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationService]
        """
        super().__init__()
        self._token = token or TokenValidationService()
        
    @property
    def token(self) -> TokenValidationService:
        return self._token
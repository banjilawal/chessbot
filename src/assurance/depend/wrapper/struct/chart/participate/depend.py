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
from exchange import TokenValidationServer


class ParticipationDependency(ChartDependency[Participation]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Chart needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        token: TokenValidationServer

    Provides:

    Super Class:
        ChartDependency
    """
    _token: TokenValidationServer
    
    def __init__(
            self,
            token: Optional[TokenValidationServer] | None = None,
    ):
        """
        Args:
            token: Optional[TokenValidationServer]
        """
        super().__init__()
        self._token = token or TokenValidationServer()
        
    @property
    def token(self) -> TokenValidationServer:
        return self._token
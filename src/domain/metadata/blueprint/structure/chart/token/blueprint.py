# src/domain/metadata/blueprint/structure/chart/token.blueprint.py

"""
Module: domain.metadata.blueprint.structure.chart.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Token, ChartBlueprint, TokenChart
from err import TokenChartNullException


class TokenChartBlueprint(ChartBlueprint[TokenChart]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a TokenChart.

     Attributes:
        victim: Token
        attacker: Token
        Optional[Type[TokenChart]]
        domain_null_exception: Optional[TokenChartNullException]

     Provides:

     Super Class:
        ChartBlueprint
     """
    _victim: Token
    _attacker: Token
    
    def __init__(
            self,
            victim: Token,
            attacker: Token,
            domain_class: Optional[Type[TokenChart]] | None = None,
            domain_null_exception: Optional[TokenChartNullException] | None = None,
    ):
        """
        Args:
            victim: Token
            attacker: Token
            Optional[Type[TokenChart]]
            domain_null_exception: Optional[TokenChartNullException]
        """
        super().__init__(
            domain_class=domain_class or TokenChart,
            domain_null_exception=domain_null_exception or TokenChartNullException(),
        )
        self._victim = victim
        self._attacker = attacker
        
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def attacker(self) -> Token:
        return self._attacker
    
    @property
    def domain_class(self) -> Type[TokenChart]:
        return cast(Type[TokenChart], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenChartNullException:
        return cast(TokenChartNullException, super().domain_null_exception)
    
    

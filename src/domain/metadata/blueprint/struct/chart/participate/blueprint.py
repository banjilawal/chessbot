# src/domain/metadata/blueprint/struct/chart/participate.blueprint.py

"""
Module: domain.metadata.blueprint.struct.chart.participate.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Token, ChartBlueprint, Participation
from err import ParticipationNullException


class ParticipationBlueprint(ChartBlueprint[Participation]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a Participation.

     Attributes:
        victim: Token
        attacker: Token
        Optional[Type[Participation]]
        domain_null_exception: Optional[ParticipationNullException]

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
            domain_class: Optional[Type[Participation]] | None = None,
            domain_null_exception: Optional[ParticipationNullException] | None = None,
    ):
        """
        Args:
            victim: Token
            attacker: Token
            Optional[Type[Participation]]
            domain_null_exception: Optional[ParticipationNullException]
        """
        super().__init__(
            domain_class=domain_class or Participation,
            domain_null_exception=domain_null_exception or ParticipationNullException(),
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
    def domain_class(self) -> Type[Participation]:
        return cast(Type[Participation], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ParticipationNullException:
        return cast(ParticipationNullException, super().domain_null_exception)
    
    

# src/domain/struct/chart/token/struct.py

"""
Module: domain.struct.chart.token.struct
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict

from domain import Chart, Token


class TokenChart(Chart[Token]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores TokenEncounterValidator success data.

    Attributes:
        victim: Token
        attacker: Token

    Provides:

    Super
        ValidatorChart[
    """
    _victim: Token
    _attacker: Token
    
    def __init__(
            self,
            victim: Token,
            attacker: Token,
    ):
        """
        Args:
            victim: Token
            attacker: Token
        """
        super().__init__()
        self._victim = victim
        self._attacker = attacker
    
    @property
    def victim(self) -> Token:
        return self.victim
    
    @property
    def attacker(self) -> Token:
        return self._attacker
    
    @property
    def is_full(self) -> bool:
        return self.size == 2
    
    @property
    def consistency_exists(self) -> bool:
        return self.is_full
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size == 1 or self.size > 2
    
    @property
    def to_dict(self) -> Dict[str, Token]:
        return {
            "victim": self._victim,
            "attacker": self._attacker,
        }
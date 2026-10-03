# src/assurance/data/chart/encounter/chart.py

"""
Module: assurance.data.chart.encounter.chart
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict

from assurance import ValidatorChart
from domain import Token


class EncounterParticipants(ValidatorChart[Token]):
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
    def to_dict(self) -> Dict[str, Token]:
        table: Dict[str, Token] = {}
        if self.victim is not None:
            table["encounter"] = self.victim
        if self._attacker is not None:
            table["attacker"] = self._attacker
        return table
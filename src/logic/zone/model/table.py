# src/logic/zone/mode/table.py

"""
Module: logic.zone.model.table
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from logic.schema import Schema
from logic.system import GameColor
from logic.team.model.model import Team
from logic.zone.model import Zone


class ZoneTable:
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Provide global, low-level addressing squares and tokens on the board.

    Attributes:
        color: GameColor
        schema: Schema

    Provides:
        -   def opposite(zone: Zone) -> Zone:

    Super Class:
        Enum
    """
    _table: Dict[Zone, Team]
    
    def __init__(self,):
        self._table = {}
        
    @property
    def table(self) -> Dict[Zone, Team]:
        return self._table
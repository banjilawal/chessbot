# src/model/blueprint/coord/model.py

"""
Module: model.blueprint.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Blueprint, Coord


class CoordBlueprint(Blueprint[Coord]):
    _row: int
    _column: int
    
    def __init__(self, row: int, column: int,):
        super().__init__()
        self._row = int
        self._column = int

    @property
    def row(self) -> int:
        return self._row
    
    @property
    def column(self) -> int:
        return self._column
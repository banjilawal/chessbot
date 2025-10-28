# src/chess/battle_space/calculate.py

"""
Module: chess.battle_space.calculate
Author: Banji Lawal
Created: 2025-10-27
version: 1.0.0
"""

from chess.battle_space import TeamProjectionTable, ProjectionCalculator, ProjectionSearch
from chess.piece import Piece


class ProjectionService:
    _projection_search: ProjectionSearch
    _projection_table: TeamProjectionTable
    _projection_calculator: ProjectionCalculator
    
    def __init__(
            self,
            projection_search: ProjectionSearch,
            projection_table: TeamProjectionTable,
            projection_calculator: ProjectionCalculator
    ):
        self._projection_search = projection_search
        self._projection_table = projection_table
        self._projection_calculator = projection_calculator
    
    def calculate(self, piece: Piece) -> Projection:
        return self._projection_calculator.calculate(piece)

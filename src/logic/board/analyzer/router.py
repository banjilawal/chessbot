# src/logic/board/analyzer/provider.py

"""
Module: logic.board.analyzer.provider
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.board import BoardSquareRelationAnalyzer, BoardTeamRelationAnalyzer
from logic.board.analyzer.context import BoardRelationAnalysisContext
from logic.system import LoggingLevelRouter, RelationReport


class BoardRelationAnalyzer:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService runs.

    Attributes:
        team_relation: BoardTeamRelationAnalyzer
        square_relation: BoardSquareRelationAnalyzer

    Provides:
         -  analyze(self, context: BoardRelationAnalysisContext) -> RelationReport
    Parent:
    """
    _team_relation: BoardTeamRelationAnalyzer
    _square_relation: BoardSquareRelationAnalyzer
    
    def __init__(
            self,
            team_relation: BoardTeamRelationAnalyzer = BoardTeamRelationAnalyzer(),
            square_relation: BoardSquareRelationAnalyzer = BoardSquareRelationAnalyzer(),
    ):
        self._square_relation = square_relation
        self._team_relation = team_relation
        
    @LoggingLevelRouter.monitor
    def analyze(self, context: BoardRelationAnalysisContext) -> RelationReport:
        
        if context.team is not None:
            return self._team_relation.analyze(
                candidate_primary=context.board,
                candidate_secondary=context.team,
            )
        
        return self._square_relation.analyze(
            candidate_primary=context.board,
            candidate_secondary=context.square,
        )
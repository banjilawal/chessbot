# src/logic/board/analyzer/provider.py

"""
Module: logic.board.analyzer.provider
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from logic.board import BoardSquareRelationAnalysis, BoardTeamRelationAnalysis
from logic.board.analyzer.context import BoardRelationAnalysisContext
from system import LoggingLevelRouter, RelationReport


class BoardRelationAnalyzer:
    """
    Role:
        - Utilities Provider

    Responsibilities:
        1.  Provide a single entry point for transactions TokenStackService runs.

    Attributes:
        team_relation: BoardTeamRelationAnalysis
        square_relation: BoardSquareRelationAnalysis

    Provides:
         -  analyze(self, context: BoardRelationAnalysisContext) -> RelationReport
    Parent:
    """
    _team_relation: BoardTeamRelationAnalysis
    _square_relation: BoardSquareRelationAnalysis
    
    def __init__(
            self,
            team_relation: BoardTeamRelationAnalysis = BoardTeamRelationAnalysis(),
            square_relation: BoardSquareRelationAnalysis = BoardSquareRelationAnalysis(),
    ):
        self._square_relation = square_relation
        self._team_relation = team_relation
        
    @LoggingLevelRouter.monitor
    def analyze(self, context: BoardRelationAnalysisContext) -> RelationReport:
        
        if context.team is not None:
            return self._team_relation.build(
                candidate_primary=context.board,
                candidate_secondary=context.team,
            )
        
        return self._square_relation.execute(
            candidate_primary=context.board,
            candidate_secondary=context.square,
        )
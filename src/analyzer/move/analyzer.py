# src/analyzer/move/analyzer.py

"""
Module: analyzer.move.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer, SquareTokenRelationAnalyzer
from logic.move.move import Move
from model import Square, Token
from report import MoveOrder
from result import AnalysisResult
from util import LoggingLevelRouter


class MovePermissionManager(Analyzer):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyse(
            cls,
            token: Token,
            destination: Square,
            square_token_relation_analyzer: SquareTokenRelationAnalyzer | None = None,
    ) -> AnalysisResult[MoveOrder]:
        pass
    

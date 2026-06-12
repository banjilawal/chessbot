# src/analyzer/itinerary/analyzer.py

"""
Module: analyzer.itinerary.analyzer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import Analyzer, SquareTokenRelationAnalyzer, TokenFreedomAnalyzer
from logic.itinerary.itinerary import Itinerary
from model import Square, Token
from report import ItineraryOrder
from result import AnalysisResult
from util import LoggingLevelRouter


class ItineraryPermissionManager(Analyzer):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def analyse(
            cls,
            token: Token,
            destination: Square,
            token_freedom_analyzer: TokenFreedomAnalyzer | None = None,
            square_token_relation_analyzer: SquareTokenRelationAnalyzer | None = None,
    ) -> AnalysisResult[ItineraryOrder]:
        pass
    

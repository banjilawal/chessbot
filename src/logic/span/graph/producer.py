# src/logic/span/square/graph/builder.py

"""
Module: logic.span.square.graph.builder
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations

from logic.graph import Graph
from logic.span import SquareSpan
from logic.square import SquareStackService
from logic.system import BuildResult, Builder, LoggingLevelRouter


class SpanningGraphProducer(Builder[Graph]):
    
    @classmethod
    @LoggingLevelRouter
    def build(
        cls,
        square_span: SquareSpan,
        square_stack: SquareStackService,
    ) -> BuildResult[Graph]:
        """
        Args:
            square_span: SquareSpan
            square_stack: SquareStackService
            
        Returns:
            BuildResult[Graph]
        
        Raises:
            SpanningGraphProductionException
        """
        method = f"{cls.__class__.__name__}.build"
        
        graph = Graph()
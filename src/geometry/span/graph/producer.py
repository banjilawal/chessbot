# src/geometry/span/square/graph/exception.py

"""
Module: geometry.span.square.graph.build
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations

from graph.graph import Graph
from math.span import SquareSpan
from geometry.square import SquareStackService
from system import BuildResult, Builder, LoggingLevelRouter


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
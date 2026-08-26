# src/fabrication/builder/query/fabrication/builder.py

"""
Module: fabrication.builder.query.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.model import Query
from artifcat import BuildResult
from fabrication.builder import Builder
from util import LoggingLevelRouter

class QueryBuilder(Builder[Query]):
    NAME = "query_builder"
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: QueryBlueprint,) -> BuildResult[Query]:
        """
        Assemble the appropriate Query.

        Args:
            blueprint: QueryBlueprint
        Returns:
            BuildResult[Query]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        return BuildResult.success(
            Query(
                x=blueprint.x,
                y=blueprint.y,
            )
        )
        
        

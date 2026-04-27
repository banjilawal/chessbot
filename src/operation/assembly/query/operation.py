# src/operation/assembly/query/operation.py

"""
Module: operation.assembly.query.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from operation import Assembler
from system import LoggingLevelRouter
from model import Query, QueryBlueprint

class QueryAssembler(Assembler[Query]):
    OPERATION_NAME = "query_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: QueryBlueprint,) -> BuildResult[Query]:
        """
        Assemble the appropriate Query.

        Args:
            blueprint: QueryBlueprint
        Returns:
            BuildResult[Query]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        return BuildResult.success(
            Query(
                x=blueprint.x,
                y=blueprint.y,
            )
        )
        
        

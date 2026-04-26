# src/operation/assembly/board/operation.py

"""
Module: operation.assembly.board.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from operation import Assembler
from system import LoggingLevelRouter
from model import Board, BoardBlueprint


class BoardAssembler(Assembler[Board]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: BoardBlueprint,) -> BuildResult[Board]:
        """
       .Assembly.he appropriate Board.

        Args:
            blueprint: BoardBlueprint
        Returns:
            BuildResult[Board]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        
        return BuildResult.success(Board(id=blueprint.id, arena=blueprint.arena,))
    
        
        

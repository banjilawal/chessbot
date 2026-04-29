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
from util import LoggingLevelRouter
from model import Board, BoardBlueprint
from controller import WorkerRegistryController


class BoardAssembler(Assembler[Board]):
    OPERATION_NAME = "board_assembler"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, blueprint: BoardBlueprint,) -> BuildResult[Board]:
        """
        Assemble the appropriate Board.

        Args:
            blueprint: BoardBlueprint
        Returns:
            BuildResult[Board]
        Raises:
        """
        method = f"{cls.__name__}.execute"
        
        return BuildResult.success(Board(id=blueprint.id, arena=blueprint.arena,))

# Register the operation.
WorkerRegistryController.register(worker=BoardAssembler)
    
        
        

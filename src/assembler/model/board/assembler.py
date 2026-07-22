# src/assembler/model/board/assembler.py

"""
Module: assembler.model.board.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from assembler import ModelAssembler
from blueprint import BoardBlueprint
from model import Board
from result import BuildResult
from util import LoggingLevelRouter


class BoardAssembler(ModelAssembler[Board]):
    """
    Role
        -   Builder

    Responsibilities:
        1.  Create a Board instance from the safe blueprint.

    Attributes:

    Provides:
        -   def execute(self, blueprint: BoardBlueprint,) -> BuildResult[Board]

    Super Class:
        ModelAssembler
    """
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: BoardBlueprint,) -> BuildResult[Board]:
        """
        Assemble a Board from the Blueprint's contents.

        Args:
            blueprint: BoardBlueprint
        Returns:
            BuildResult[Board]
        Raises:
        """
        method = f"{self.__class__.__name__}.execute"
        
        return BuildResult.success(Board(id=blueprint.id, arena=blueprint.arena,))

    
        
        

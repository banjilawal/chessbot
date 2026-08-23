# src/assembler/model/board/assembler.py

"""
Module: assembler.model.board.assembler
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from fabrication.assembler import ModelAssembler
from domain.metadata.blueprint import BoardBlueprint
from domain.model import Board
from artifcat.result import BuildResult
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

    
        
        

# src/fabrication/builder/model/board/fabrication/builder.py

"""
Module: fabrication.builder.model.board.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from fabrication.builder import ModelBuilder
from domain.metadata.blueprint import BoardBlueprint
from domain.model import Board
from artifcat import BuildResult
from util import LoggingLevelRouter


class BoardBuilder(ModelBuilder[Board]):
    """
    Role
        -  Builder

    Responsibilities:
        1.  Create a Board instance from the safe blueprint.

    Attributes:

    Provides:
        -  def execute(self, blueprint: BoardBlueprint,) -> BuildResult[Board]

    Super Class:
        ModelBuilder
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

    
        
        

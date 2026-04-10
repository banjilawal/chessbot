# src/toolkit/context/board/toolkit.py

"""
Module: toolkit.context.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import TeamValidator
from model import BoardContext
from toolkit import BoardToolkit, Toolkit


class BoardContextToolkit(Toolkit[BoardContext]):
    """
    Role:
        -   Container
        -   Data Holder

    Responsibilities:
        1.  Collection of workers and services that are required for BoardContext tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        board_toolkit: BoardToolkit
        team_validator: TeamValidator
            
    Provides:

    Super Class:
    """
    _board_toolkit: BoardToolkit | None = None
    _team_validator: TeamValidator | None = None
    
    def __init__(
            self,
            board_toolkit: BoardToolkit | None = None,
            team_validator: TeamValidator | None = None,
    ):
        """
        Args:
            board_toolkit: BoardToolkit
            team_validator: TeamValidator
        """
        super().__init__()
        self._board_toolkit = board_toolkit or BoardToolkit()
        self._team_validator = team_validator or TeamValidator()
        
    @property
    def board_toolkit(self) -> BoardToolkit:
        return self._board_toolkit
    
    @property
    def team_validator(self) -> TeamValidator:
        return self._team_validator
        
    
    
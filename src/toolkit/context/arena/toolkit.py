# src/toolkit/context/arena/toolkit.py

"""
Module: toolkit.context.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from integrity import PlayerValidator
from model import ArenaContext
from toolkit import ArenaToolkit, Toolkit


class ArenaContextToolkit(Toolkit[ArenaContext]):
    """
    Role:
        -   Container
        -   Data Holder

    Responsibilities:
        1.  Collection of workers and services that are required for ArenaContext tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        arena_toolkit: ArenaToolkit
        player_validator: PlayerValidator
            
    Provides:

    Super Class:
    """
    _arena_toolkit: ArenaToolkit | None = None
    _player_validator: PlayerValidator | None = None
    
    def __init__(
            self,
            arena_toolkit: ArenaToolkit | None = None,
            player_validator: PlayerValidator | None = None,
    ):
        """
        Args:
            arena_toolkit: ArenaToolkit
            player_validator: PlayerValidator
        """
        super().__init__()
        self._arena_toolkit = arena_toolkit or ArenaToolkit()
        self._player_validator = player_validator or PlayerValidator()
        
    @property
    def arena_toolkit(self) -> ArenaToolkit:
        return self._arena_toolkit
    
    @property
    def player_validator(self) -> PlayerValidator:
        return self._player_validator
        
    
    
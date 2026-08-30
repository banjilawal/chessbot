# src/domain/metadata/blueprint/context/model/arena/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import ArenaContext, Board, Game, ModelContextBlueprint, Player
from err import ArenaContextNullException


class ArenaContextBlueprint(ModelContextBlueprint[ArenaContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an ArenaContext.
         
     Attributes:
        id: Optional[int]
        game: Optional[Game]
        board: Optional[Board]
        player: Optional[Player]
        player_color: Optional[GameColor]
        
        domain_class: Type[ArenaContext]
        domain_null_exception: ArenaContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _game: Optional[Game]
    _board: Optional[Board]
    _player: Optional[Player]
    _player_color: Optional[GameColor]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            board: Optional[Board] | None = None,
            player: Optional[Player] | None = None,
            player_color: Optional[GameColor] | None = None,
            domain_class: Optional[Type[ArenaContext]] | None = None,
            domain_null_exception: Optional[ArenaContextNullException] | None = None,
    ):
        """
        Args:
            game: Optional[Game]
            board: Optional[Board]
            player: Optional[Player]
            player_color: Optional[GameColor]
            domain_class: Type[ArenaContext]
            domain_null_exception: ArenaContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[ArenaContext],
            domain_null_exception=domain_null_exception or ArenaContextNullException(),
        )
        self._game = game
        self._board = board
        self._player = player
        self._player_color = player_color

    
    @property
    def domain_class(self) -> Type[ArenaContext]:
        return cast(Type[ArenaContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ArenaContextNullException:
        return  cast(ArenaContextNullException, super().domain_null_exception)
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def player(self) -> Optional[Player]:
        return self._player
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def player_color(self) -> Optional[GameColor]:
        return self._player_color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self._game,
            "board": self._board,
            "player": self._player,
            "player_color": self._player_color,
        }
    
    
    
    
    



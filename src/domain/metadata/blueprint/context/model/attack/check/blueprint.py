# src/domain/metadata/blueprint/context/model/attack/check/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.attack.check.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import CheckContext, Board, Game, ContextBlueprint, Player
from err import CheckContextNullException


class CheckContextBlueprint(ModelContextBlueprint[CheckContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an CheckContext.
         
     Attributes:
        domain_class: Type[CheckContext]
        domain_null_exception: CheckContextNullException
        id: Optional[int]
        game: Optional[Game]
        board: Optional[Board]
        player: Optional[Player]
        color: Optional[GameColor]

     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _game: Optional[Game]
    _board: Optional[Board]
    _player: Optional[Player]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            domain_class: Optional[Type[CheckContext]] | None = None,
            domain_null_exception: Optional[CheckContextNullException] | None = None,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            board: Optional[Board] | None = None,
            player: Optional[Player] | None = None,
            color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            domain_class: Type[CheckContext]
            domain_null_exception: CheckContextNullException
            game: Optional[Game]
            board: Optional[Board]
            player: Optional[Player]
            color: Optional[GameColor]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[CheckContext],
            domain_null_exception=domain_null_exception or CheckContextNullException(),
        )
        self._game = game
        self._board = board
        self._color = color
        self._player = player
    
    @property
    def domain_class(self) -> Type[CheckContext]:
        return cast(Type[CheckContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CheckContextNullException:
        return  cast(CheckContextNullException, super().domain_null_exception)
    
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
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self._game,
            "board": self._board,
            "player": self._player,
            "color": self._color,
        }
    
    
    
    
    



# src/domain/metadata/blueprint/context/model/token/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import TokenSearchContext, Board, Game, ContextBlueprint, Player
from err import TokenSearchContextNullException


class TokenContextBlueprint(ModelContextBlueprint[TokenSearchContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an TokenSearchContext.
         
     Attributes:
        domain_class: Type[TokenSearchContext]
        domain_null_exception: TokenSearchContextNullException
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
            domain_class: Optional[Type[TokenSearchContext]] | None = None,
            domain_null_exception: Optional[TokenSearchContextNullException] | None = None,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            board: Optional[Board] | None = None,
            player: Optional[Player] | None = None,
            color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            domain_class: Type[TokenSearchContext]
            domain_null_exception: TokenSearchContextNullException
            game: Optional[Game]
            board: Optional[Board]
            player: Optional[Player]
            color: Optional[GameColor]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[TokenSearchContext],
            domain_null_exception=domain_null_exception or TokenSearchContextNullException(),
        )
        self._game = game
        self._board = board
        self._color = color
        self._player = player
    
    @property
    def domain_class(self) -> Type[TokenSearchContext]:
        return cast(Type[TokenSearchContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenSearchContextNullException:
        return  cast(TokenSearchContextNullException, super()._domain_null_exception)
    
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
    
    
    
    
    



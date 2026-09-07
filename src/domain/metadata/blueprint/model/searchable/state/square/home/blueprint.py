# src/domain/metadata/blueprint/model/searchable/state/square/home/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.square.home.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Board, Coord, Formation, HomeSquare, SquareBlueprint, Token
from err import HomeSquareNullException


class HomeSquareBlueprint(SquareBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a HomeSquare object.

     Attributes:
        formation: Formation

        domain_class: Type[HomeSquare]
        domain_null_exception: HomeSquareNullException

     Provides:

     Super Class:
        SquareBlueprint
     """
    _formation: Formation
    
    def __init__(
            self,
            name: str,
            board: Board,
            coord: Coord,
            formation: Formation,
            occupant: Optional[Token] | None = None,
            domain_class: Optional[Type[HomeSquare]] | None = None,
            domain_null_exception: Optional[HomeSquareNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            name: str
            board: Board
            coord: Coord
            occupant: Optional[Token]
            formation: Optional[Formation]
            domain_class: Optional[Type[Square]]
            domain_null_exception: Optional[HomeSquareNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            name=name,
            board=board,
            coord=coord,
            occupant=occupant,
            domain_class=domain_class or Type[HomeSquare],
            domain_null_exception=domain_null_exception or HomeSquareNullException(),
        )
        self._formation = formation
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def occupant(self) -> Optional[Token]:
        return self._occupant
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def domain_class(self) -> Type[HomeSquare]:
        return cast(Type[HomeSquare], super().domain_class)
    
    @property
    def domain_null_exception(self) -> HomeSquareNullException:
        return cast(HomeSquareNullException, super().domain_null_exception)
    
    @property
    def is_home_square_blueprint(self) -> bool:
        return (
                isinstance(self, HomeSquareBlueprint) and
                self._formation is not None
        )
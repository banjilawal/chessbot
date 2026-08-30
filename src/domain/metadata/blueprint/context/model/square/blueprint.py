# src/domain/metadata/blueprint/context/model/square/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.square.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Board, Coord, ModelContextBlueprint, SquareContext, SquareState, SquareType, Token
from err import SquareContextNullException


class SquareContextBlueprint(ModelContextBlueprint[SquareContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a SquareContext.
         
     Attributes:
        id: Optional[int]
        id: Optional[str]
        board: Optional[Board]
        coord: Optional[Coord]
        occupant: Optional[Token]
        state: Optional[SquareState]
        square_type: Optional[SquareType]
        
        domain_class: Type[SquareContext]
        domain_null_exception: SquareContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    _board: Optional[Board]
    _coord: Optional[Coord]
    _occupant: Optional[Token]
    _state: Optional[SquareState]
    _square_type: Optional[SquareType]
    
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            board: Optional[Board] | None = None,
            coord: Optional[Coord] | None = None,
            occupant: Optional[Token] | None = None,
            state: Optional[SquareState] | None = None,
            square_type: Optional[SquareType] | None = None,
            domain_class: Optional[Type[SquareContext]] | None = None,
            domain_null_exception: Optional[SquareContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[id]
            name: Optional[str]
            board: Optional[Board]
            coord: Optional[Coord]
            occupant: Optional[Token]
            state: Optional[SquareState]
            square_type: Optional[SquareType]
            domain_class: Type[SquareContext]
            domain_null_exception: SquareContextNullException

        """
        super().__init__(
            id=id,
            name=name,
            domain_class=domain_class or Type[SquareContext],
            domain_null_exception=domain_null_exception or SquareContextNullException(),
        )
        self._coord = coord
        self._board = board
        self._state = state
        self._occupant = occupant
        self._square_type = square_type

    
    @property
    def domain_class(self) -> Type[SquareContext]:
        return cast(Type[SquareContext], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> SquareContextNullException:
        return  cast(SquareContextNullException, super().domain_null_exception)
    

    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    
    @property
    def occupant(self) -> Optional[Token]:
        return self._occupant
    
    
    @property
    def state(self) -> Optional[SquareState]:
        return self._state
    
    
    @property
    def square_type(self)-> Optional[SquareType]:
        return self._square_type
    
        
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self._board,
            "coord": self._coord,
            "state": self._state,
            "occupant": self._occupant,
            "square_type": self._square_type,
        }
    
    
    
    
    


 
# src/domain/metadata/blueprint/context/model/coord/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import Idcolumn
from domain import CoordContext, Board, Id, ContextBlueprint, ContextBlueprint, row
from err import CoordContextNullException


class CoordContextBlueprint(ContextBlueprint[CoordContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an CoordContext.
         
     Attributes:
        domain_class: Type[CoordContext]
        domain_null_exception: CoordContextNullException
        id: Optional[int]
        
        board: Optional[Board]
        row: Optional[int]
        column: Optional[int]

     Provides:

     Super Class:
        ContextBlueprint
     """

    _id: Optional[int]
    _row: Optional[int]
    _column: Optional[int]
    _board: Optional[Board]

    
    def __init__(
            self,
            domain_class: Optional[Type[CoordContext]] | None = None,
            domain_null_exception: Optional[CoordContextNullException] | None = None,
            id: Optional[int] | None = None,
            row: Optional[int] | None = None,
            column: Optional[int] | None = None,
            board: Optional[Board] | None = None,
    ):
        """
        Args:
            domain_class: Type[CoordContext]
            domain_null_exception: CoordContextNullException
            id: Optional[int]
            row: Optional[int]
            column: Optional[int]
            board: Optional[Board]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[CoordContext],
            domain_null_exception=domain_null_exception or CoordContextNullException(),
        )
        self._id = id
        self._board = board
        self._column = column
        self._row = row
    
    @property
    def domain_class(self) -> Type[CoordContext]:
        return cast(Type[CoordContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordContextNullException:
        return  cast(CoordContextNullException, super().domain_null_exception)
    
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def column(self) -> Optional[int]:
        return self._column
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self._board,
            "row": self._row,
            "column": self._column,
        }
    
    
    
    
    



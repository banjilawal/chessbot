# src/domain/metadata/blueprint/model/searchable/state/board/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import AttackDatabase, ManeuverDatabase, SquareDatabase, TokenDatabase
from domain import Board, BoardContext, BoardTeamColorBinder, StateModelBlueprint
from err import BoardNullException


class BoardBlueprint(StateModelBlueprint[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Board object.

     Attributes:
        id: Optional[int]
        squares: SquareDatabase
        maneuver_log: ManeuverDatabase
        attack_records: AttackDatabase
        captured_tokens: TokenDatabase
        team_binder: BoardTeamColorBinder
        
        domain_class: Type[Board]
        search_context_class: Type[BoardContext]
        domain_null_exception: BoardNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _squares: SquareDatabase
    _maneuver_log: ManeuverDatabase
    _attack_records: AttackDatabase
    _captured_tokens: TokenDatabase
    _team_binder: BoardTeamColorBinder
    
    def __init__(
            self,
            squares: SquareDatabase,
            team_binder: BoardTeamColorBinder,
            domain_class: Optional[Type[Board]] | None = None,
            search_context_class: Optional[Type[BoardContext]] | None = None,
            domain_null_exception: Optional[BoardNullException] | None = None,
            id: Optional[int] | None = None,
            maneuver_log: Optional[ManeuverDatabase] | None = None,
            attack_records: Optional[AttackDatabase] | None = None,
            captured_tokens: Optional[TokenDatabase] | None = None,
    ):
        """
        Args:
            squares: SquareDatabase
            team_binder: BoardTeamColorBinder
            domain_class: Optional[Type[Board]]
            search_context_class: Optional[Type[BoardContext]]
            domain_null_exception: Optional[BoardNullException]
            
            maneuver_log: Optional[ManeuverDatabase]
            attack_records: Optional[AttackDatabase]
            captured_tokens: Optional[TokenDatabase]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Board],
            search_context_class=search_context_class or Type[BoardContext],
            domain_null_exception=domain_null_exception or BoardNullException(),
        )
        self._squares = squares
        self._team_binder = team_binder
        self._maneuver_log = maneuver_log
        self._attack_records = attack_records
        self._captured_tokens = captured_tokens
    
    @property
    def domain_class(self) -> Type[Board]:
        return cast(Type[Board], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[BoardContext]:
        return cast(Type[BoardContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> BoardNullException:
        return cast(BoardNullException, super().domain_null_exception)
    
    @property
    def squares(self) -> SquareDatabase:
        return self._squares
    
    @property
    def maneuver_log(self) -> ManeuverDatabase:
        return self._maneuver_log
    
    @property
    def attack_records(self) -> AttackDatabase:
        return self._attack_records
    
    @property
    def captured_tokens(self) -> TokenDatabase:
        return self._captured_tokens
    
    @property
    def team_binder(self) -> BoardTeamColorBinder:
        return self._team_binder
    


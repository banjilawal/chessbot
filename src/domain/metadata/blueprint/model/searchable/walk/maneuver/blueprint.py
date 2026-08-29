# src/domain/metadata/blueprint/model/searchable/walk/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Attack, Maneuver, ManeuverSearchContext, Path, SearchableModelBlueprint, Token
from err import ManeuverNullException


class ManeuverBlueprint(SearchableModelBlueprint[Maneuver]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a Maneuver object.

     Attributes:
        path: Path
        benefit: int
        traveller: Token
        attack: Optional[Attack]

        domain_class: Optional[Type[Maneuver]]
        search_context_class: Type[ManeuverSearchContext]
        domain_null_exception: Optional[ManeuverNullException]

     Provides:

     Super Class:
        SearchableModelBlueprint
     """
    _path: Path
    _benefit: int
    _traveller: Token
    _attack: Optional[Attack]
    
    def __init__(
            self,
            path: Path,
            traveller: Token,
            domain_class: Optional[Type[Maneuver]] | None = None,
            search_context_class: Optional[Type[ManeuverSearchContext]] | None = None,
            domain_null_exception: Optional[ManeuverNullException] | None = None,
            benefit: Optional[int] | None = 0,
            attack: Optional[Attack] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Maneuver]]
            search_context_class: Optional[Type[ManeuverSearchContext]]
            domain_null_exception: Optional[ManeuverNullException]
            path: Path
            benefit: int
            traveller: Token
            attack: Optional[Attack]
        """
        super().__init__(
            domain_class=domain_class or Type[Maneuver],
            search_context_class=search_context_class or Type[ManeuverSearchContext],
            domain_null_exception=domain_null_exception or ManeuverNullException(),
        )
        self._path = path
        self._benefit = benefit
        self._traveller = traveller
        self._attack = attack
    
    @property
    def domain_class(self) -> Type[Maneuver]:
        return cast(Type[Maneuver], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[ManeuverSearchContext]:
        return cast(Type[ManeuverSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> ManeuverNullException:
        return cast(ManeuverNullException, super().domain_null_exception)
    
    @property
    def traveller(self) -> Token:
        return self._traveller
    
    @property
    def path(self) -> Path:
        return self._path
    
    @property
    def benefit(self) -> int:
        return self._benefit
    
    @property
    def attack(self) -> Optional[Attack]:
        return self._attack




    
    

        
        
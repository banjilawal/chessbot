# src/domain/metadata/blueprint/model/searchable/walk/path/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.walk.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Path, SearchableModelBlueprint, SquareRegister
from err import PathNullException


class PathBlueprint(SearchableModelBlueprint[Path]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a Path object.

     Attributes:
        endpoints: SquareRegister
        domain_class: Optional[Type[Path]]
        search_context_class: Type[PathSearchContext]
        domain_null_exception: Optional[PathNullException]
        label: Optional[int]
     Provides:

     Super Class:
        SearchableModelBlueprint
     """
    _endpoints: SquareRegister
    _label: Optional[int]
    
    def __init__(
            self,
            endpoints: SquareRegister,
            domain_class: Optional[Type[Path]] | None = None,
            search_context_class: Optional[Type[PathSearchContext]] | None = None,
            domain_null_exception: Optional[PathNullException] | None = None,
            label: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Path]]
            search_context_class: Optional[Type[PathSearchContext]]
            domain_null_exception: Optional[PathNullException]
            id: Optional[int]
            squares: SquareDatabase
            team_binder: PathTeamColorBinder
        """
        super().__init__(
            domain_class=domain_class or Type[Path],
            search_context_class=search_context_class or Type[PathSearchContext],
            domain_null_exception=domain_null_exception or PathNullException(),
        )
        self._label = label
        self._endpoints = endpoints
    
    @property
    def domain_class(self) -> Type[Path]:
        return cast(Type[Path], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[PathSearchContext]:
        return cast(Type[PathSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> PathNullException:
        return cast(PathNullException, super().domain_null_exception)
    
    @property
    def label(self) -> Optional[int]:
        return self._label
    
    @property
    def endpoints(self) -> SquareRegister:
        return self._endpoints




    
    

        
        
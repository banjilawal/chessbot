# src/domain/metadata/blueprint/model/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.model.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from config import NumericSetting
from domain import Maneuver, ModelBlueprint, Path, Token
from err import ManeuverNullException


class ManeuverBlueprint(ModelBlueprint[Maneuver]):
    """
     Role:
        1.  Metadata

     Responsibilities:
        1.  Provides values for hydrating a Maneuver object.

     Attributes:
        path: Path
        benefit: int
        traveler: Token

        domain_class: Optional[Type[Maneuver]]
        domain_null_exception: Optional[ManeuverNullException]

     Provides:

     Super Class:
        SearchableModelBlueprint
     """
    
    _path: Path
    _benefit: int
    _traveler: Token
    
    def __init__(
            self,
            path: Path,
            traveler: Token,
            benefit: Optional[int] | None = None,
            domain_class: Optional[Type[Maneuver]] | None = None,
            domain_null_exception: Optional[ManeuverNullException] | None = None,
    ):
        """
        Args:
            path: Path
            traveler: Token
            benefit: Optional[int]
            domain_class: Optional[Type[Maneuver]]
            domain_null_exception: Optional[ManeuverNullException]
        """
        super().__init__(
            domain_class=domain_class or Type[Maneuver],
            domain_null_exception=domain_null_exception or ManeuverNullException(),
        )
        self._path = path
        self._traveler = traveler
        self._benefit = benefit or NumericSetting.negative_infinity()
    
    @property
    def traveler(self) -> Token:
        return self._traveler
    
    @property
    def path(self) -> Path:
        return self._path
    
    @property
    def benefit(self) -> int:
        return self._benefit
    
    @property
    def domain_class(self) -> Type[Maneuver]:
        return cast(Type[Maneuver], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ManeuverNullException:
        return cast(ManeuverNullException, super().domain_null_exception)




    
    

        
        
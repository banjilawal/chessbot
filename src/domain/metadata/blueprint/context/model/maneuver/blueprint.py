# src/domain/metadata/blueprint/context/model/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Token, ManeuverContext, ContextBlueprint, Path, Token
from err import ManeuverContextNullException


class ManeuverContextBlueprint(ContextBlueprint[ManeuverContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a ManeuverContext.
         
     Attributes:
        path: Optional[Path]
        benefit: Optional[int]
        victim: Optional[Token]
                 
        domain_class: Type[ManeuverContext]
        domain_null_exception: ManeuverContextNullException
        
     Provides:

     Super Class:
        ContextBlueprint
     """

    _path: Optional[Path]
    _benefit: Optional[int]
    _traveler: Optional[Token]


    def __init__(
            self,
            id: Optional[int] | None = None,
            path: Optional[Path] | None = None,
            benefit: Optional[int] | None = None,
            traveler: Optional[Token] | None = None,
            domain_class: Optional[Type[ManeuverContext]] | None = None,
            domain_null_exception: Optional[ManeuverContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            path: Optional[Path]
            benefit: Optional[[int]]
            domain_class: Type[ManeuverContext]
            domain_null_exception: ManeuverContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[ManeuverContext],
            domain_null_exception=domain_null_exception or ManeuverContextNullException(),
        )
        self._path = path
        self._traveler = traveler
        self._benefit = benefit
    
    @property
    def domain_class(self) -> Type[ManeuverContext]:
        return cast(Type[ManeuverContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> ManeuverContextNullException:
        return  cast(ManeuverContextNullException, super().domain_null_exception)
    
    @property
    def path(self) -> Optional[Path]:
        return self._path
    
    @property
    def benefit(self) -> Optional[int]:
        return self._benefit
    
    @property
    def traveler(self) -> Optional[Token]:
        return self._traveler
 
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "path": self._path,
            "traveler": self._traveler,
            "benefit": self._benefit,
        }
    
    
    
    
    



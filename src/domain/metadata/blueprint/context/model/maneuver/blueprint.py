# src/domain/metadata/blueprint/context/model/maneuver/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.maneuver.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Attack, ManeuverContext, ModelContextBlueprint, Path, Token
from err import ManeuverContextNullException


class ManeuverContextBlueprint(ModelContextBlueprint[ManeuverContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a ManeuverContext.
         
     Attributes:
        path: Optional[Path]
        benefit: Optional[int]
        attack: Optional[Attack]
        traveller: Optional[Token]
                 
        domain_class: Type[ManeuverContext]
        domain_null_exception: ManeuverContextNullException
        
     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _path: Optional[Path]
    _benefit: Optional[int]
    _attack: Optional[Attack]
    _traveller: Optional[Token]


    def __init__(
            self,
            path: Optional[Path] | None = None,
            benefit: Optional[int] | None = None,
            attack: Optional[Attack] | None = None,
            traveller: Optional[Token] | None = None,
            domain_class: Optional[Type[ManeuverContext]] | None = None,
            domain_null_exception: Optional[ManeuverContextNullException] | None = None,
    ):
        """
        Args:
            path: Optional[Path]
            attack: Optional[Attack]
            traveller: Optional[Token]
            benefit: Optional[PathBenefit]
            domain_class: Type[ManeuverContext]
            domain_null_exception: ManeuverContextNullException
        """
        super().__init__(
            domain_class=domain_class or Type[ManeuverContext],
            domain_null_exception=domain_null_exception or ManeuverContextNullException(),
        )
        self._path = path
        self._attack = attack
        self._benefit = benefit
        self._traveller = traveller
    
    
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
    def attack(self) -> Optional[Attack]:
        return self._attack
    
    
    @property
    def traveller(self) -> Optional[Token]:
        return self._traveller
 
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self._path,
            "attack": self._attack,
            "benefit": self._benefit,
            "traveller": self._traveller,
        }
    
    
    
    
    



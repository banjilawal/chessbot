# src/domain/metadata/blueprint/context/model/path/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import ModelContextBlueprint, PathContext, Square
from err import PathContextNullException


class PathContextBlueprint(ModelContextBlueprint[PathContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a PathContext.
         
     Attributes:
        label: Optional[int]
        origin: Optional[Square]
        destination: Optional[Square]
        
        domain_class: Type[PathContext]
        domain_null_exception: PathContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _label: Optional[int]
    _origin: Optional[Square]
    _destination: Optional[Square]
    
    
    def __init__(
            self,
            label: Optional[int] | None = None,
            origin: Optional[Square] | None = None,
            destination: Optional[Square] | None = None,
            domain_class: Optional[Type[PathContext]] | None = None,
            domain_null_exception: Optional[PathContextNullException] | None = None,

    ):
        """
        Args:
            label: Optional[int]
            origin: Optional[Square]
            destination: Optional[Square]
            domain_class: Type[PathContext]
            domain_null_exception: PathContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[PathContext],
            domain_null_exception=domain_null_exception or PathContextNullException(),
        )
        self._label = label
        self._origin = origin
        self._destination = destination

    
    @property
    def domain_class(self) -> Type[PathContext]:
        return cast(Type[PathContext], super().domain_class)
    
    
    @property
    def domain_null_exception(self) -> PathContextNullException:
        return  cast(PathContextNullException, super().domain_null_exception)
    
    
    @property
    def label(self) -> Optional[int]:
        return self._label
    
    
    @property
    def origin(self) -> Optional[Square]:
        return self._origin
    
    
    @property
    def destination(self) -> Optional[Square]:
        return self._destination
    
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self._label,
            "origin": self._origin,
            "destination": self._destination,
        }
    
    
    
    
    



# src/domain/metadata/blueprint/model/path/blueprint.py

"""
Module: domain.metadata.blueprint.model.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import ModelBlueprint, SquareRegister, Path
from err import PathNullException


class PathBlueprint(ModelBlueprint[Path]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Path object.


    Attributes:
        endpoints: SquareRegister
        domain_class: Optional[Type[Path]]
        domain_null_exception: Optional[PathNullException]
        id: Optional[int]

    Provides:

     Super Class:
        ModelBlueprint
     """
    _endpoints: SquareRegister
    _id: Optional[int]
    
    def __init__(
            self,
            endpoints: SquareRegister,
            domain_class: Optional[Type[Path]] | None = None,
            domain_null_exception: Optional[PathNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            endpoints: SquareRegister
            domain_class: Optional[Type[Path]]
            domain_null_exception: Optional[PathNullException]
            id: Optional[int]
        """
        super().__init__(
            domain_class=domain_class or Type[Path],
            domain_null_exception=domain_null_exception or PathNullException(),
        )
        self._id = id
        self._endpoints = endpoints
    
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def endpoints(self) -> SquareRegister:
        return self._endpoints
    
    @property
    def domain_class(self) -> Type[Path]:
        return cast(Type[Path], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PathNullException:
        return cast(PathNullException, super().domain_null_exception)


    
    

        
        
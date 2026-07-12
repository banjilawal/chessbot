# src/blueprint/model/path/blueprint.py

"""
Module: blueprint.model.path.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import ModelBlueprint
from model import Path
from register import SquareRegister


class PathBlueprint(ModelBlueprint[Path]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Path object.
        2.  DTO
        
    Attributes:
        id: int
        endpoints: SquareRegister
        cost: Optional[Cost]
        model_class: Type[Path]
        
    Provides:

     Super Class:
        ModelBlueprint
     """
    _endpoints: SquareRegister
    _id: Optional[int]
    _cost: Optional[int]
    
    def __init__(
            self,
            endpoints: SquareRegister,
            id: Optional[int] | None = None,
            cost: Optional[int] | None = None,
            model_class: Type[Path] = Path,
    ):
        """
        Args:
            endpoints: SquareRegister
            id: Optional[int]
            cost: Optional[int]
            model_class: Type[Path]
        """
        super().__init__(model_class=model_class)
        self._id = id
        self._cost = cost
        self._endpoints = endpoints
        
    @property
    def model_class(self) -> Type[Path]:
        return cast(Type[Path], self.model_class)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def endpoints(self) -> SquareRegister:
        return self._endpoints
    
    @property
    def cost(self) -> Optional[int]:
        return self._cost
    
    

        
        
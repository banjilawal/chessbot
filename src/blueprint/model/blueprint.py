# src/blueprint/model/blueprint.py

"""
Module: blueprint.model.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Type, cast

from blueprint import Blueprint
from model import Model


class ModelBlueprint(Blueprint[Model]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Model object
         2.  DTO

     Attributes:
         model_class: Type[Model]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[Model]):
        """
        Args:
            model_class: Type[Model[T]]
        
        """
        super().__init__(model_class=model_class,)
    
    @property
    def model_class(self) -> Type[Model]:
        return cast(Type[Model], self.model_class)

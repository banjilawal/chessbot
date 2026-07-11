# src/blueprint/model/blueprint.py

"""
Module: blueprint.model.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, Type, TypeVar, cast

from blueprint import Blueprint
from model import Model

T = TypeVar("T", bound="Model")


class ModelBlueprint(Blueprint[Model[T]]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a Model object
         2.  DTO

     Attributes:
         model_class: Type[Model[T]]
         
     Provides:

     Super Class:
        Blueprint
     """
    
    def __init__( self, model_class: Type[Model[T]],):
        """
        Args:
            model_class: Type[Model[T]]
        
        """
        super().__init__(model_class=model_class,)
    
    @property
    def model_class(self) -> Type[Model[T]]:
        return cast(Type[Model[T]], self.model_class)

# src/blueprint/blueprint.py

"""
Module: blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar


T = TypeVar("T")

class Blueprint(ABC, Generic[T]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating an object.
         2.  DTO

     Attributes:
         model_class: Type[T]
         model_class_name: str
         
     Provides:

     Super Class:
     """
    _model_class: Type[T]
    
    def __init__(self, model_class: Type[T],):
        """
        Args:
            model_class: Type[T]
        """
        self._model_class = model_class
    
    @property
    def model_class(self) -> Type[T]:
        return self._model_class
    
    @property
    def model_class_name(self) -> str:
        return self._model_class.__class__.__name__

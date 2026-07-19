# src/blueprint/blueprint.py

"""
Module: blueprint.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, Type, TypeVar

from err import NullException

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
         null_exception: NullException
         
     Provides:

     Super Class:
     """
    _model_class: Type[T]
    _null_exception: NullException
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: Optional[NullException] | None = NullException(),
    ):
        """
        Args:
            model_class: Type[T]
            null_exception: Optional[NullException]
        """
        self._model_class = model_class
        self._null_exception = null_exception
    
    @property
    def model_class(self) -> Type[T]:
        return self._model_class
    
    @property
    def model_class_name(self) -> str:
        return self._model_class.__class__.__name__
    
    @property
    def null_exception(self) -> NullException:
        return self._null_exception

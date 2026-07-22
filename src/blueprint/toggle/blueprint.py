# src/blueprint/toggle/blueprint.py

"""
Module: blueprint.toggle.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional, Type, cast

from blueprint import Blueprint
from err import ToggleNullException
from toggle import Toggle


class ToggleBlueprint(Blueprint[Toggle]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a B object.
    
    Attributes:
        model_class: Type[Toggle]
        null_exception: Optional[ToggleNullException]
        max_enabled_toggles: Optional[int]
    
    Provides:
    
    Super Class:
        Blueprint
    """
    _max_enabled_toggles: int
    
    def __init__(
            self,
            model_class: Type[Toggle] = Toggle,
            null_exception: Optional[ToggleNullException] | None = ToggleNullException(),
            max_enabled_toggles: Optional[int] | None = 1,
    ):
        """
        Args:
            model_class: Type[Toggle]
            null_exception: Optional[ToggleNullException]
            max_enabled_toggles: Optional[int]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
        self._max_enabled_toggles = max_enabled_toggles
    
    @property
    def model_class(self) -> Type[Toggle]:
        return cast(Type[Toggle], super().model_class)
    
    @property
    def null_exception(self) -> ToggleNullException:
        return cast(ToggleNullException, super().null_exception)
    
    @property
    def max_enabled_toggles(self) -> int:
        return self._max_enabled_toggles
    
    @property
    @abstractmethod
    def excess_active_toggles(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def no_active_toggles(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def enabled_toggles_count(self) -> int:
        pass
    
    

# src/blueprint/toggle/blueprint.py

"""
Module: blueprint.toggle.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


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
        model_type: Type[Toggle]

    Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(
            self,
            model_class: Type[Toggle] = Toggle,
            null_exception: Optional[ToggleNullException] | None = ToggleNullException(),
    ):
        """
        Args:
            model_class: Type[Toggle]
        """
        super().__init__(model_class=model_class, null_exception=null_exception)
    
    @property
    def model_class(self) -> Type[Toggle]:
        return cast(Type[Toggle], super().model_class)
    
    @property
    def null_exception(self) -> ToggleNullException:
        return cast(ToggleNullException, super().null_exception)
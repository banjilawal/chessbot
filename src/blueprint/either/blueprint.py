# src/blueprint/either/blueprint.py

"""
Module: blueprint.either.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import Blueprint
from chooser import Chooser


class EitherBlueprint(Blueprint[Chooser]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a B object.

    Attributes:
        model_type: Type[Either]

    Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[Chooser]):
        """
        Args:
            model_class: Type[Either]
        """
        super().__init__(model_class=model_class)
    
    @property
    def model_class(self) -> Type[Chooser]:
        return cast(Type[Chooser], self.model_class)
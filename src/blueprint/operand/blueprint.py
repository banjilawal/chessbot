# src/blueprint/operand/blueprint.py

"""
Module: blueprint.operand.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import Blueprint
from operand import Operand


class OperandBlueprint(Blueprint[Operand]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a B object.

    Attributes:
        model_type: Type[Operand]

    Provides:

     Super Class:
        Blueprint
     """
    
    def __init__(self, model_class: Type[Operand]):
        """
        Args:
            model_class: Type[Operand]
        """
        super().__init__(model_class=model_class)
    
    @property
    def mode_class(self) -> Type[Operand]:
        return cast(Type[Operand], self.model_class)
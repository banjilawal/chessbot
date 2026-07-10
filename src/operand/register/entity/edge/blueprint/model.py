# src/operand/register/entity/edge/blueprint/operand.py

"""
Module: operand.register.entity.edge.blueprint.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import EdgeBlueprint
from err import EdgeBlueprintNullException
from operand import EntityRegister


class EdgeBlueprintEntityRegister(EntityRegister[EdgeBlueprint]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: EdgeBlueprint
        null_exception: EdgeBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: EdgeBlueprint = Type[EdgeBlueprint],
            null_exception: EdgeBlueprintNullException = EdgeBlueprintNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> EdgeBlueprint:
        return cast(EdgeBlueprint, self.operand)
    
    @property
    def null_exception(self) -> EdgeBlueprintNullException:
        return cast(EdgeBlueprintNullException, self.null_exception)
    
    @property
    def is_edge_blueprint_entity_register(self) -> bool:
        return isinstance(self, EdgeBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EdgeBlueprintEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    

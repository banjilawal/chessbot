# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import EdgeNullException
from operand import EntityRegister, Edge


class EdgeEntityRegister(EntityRegister[Edge]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Edge
        null_exception: EdgeNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Edge = Type[Edge],
            null_exception: EdgeNullException = EdgeNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Edge:
        return cast(Edge, self.a)
    
    @property
    def null_exception(self) -> EdgeNullException:
        return cast(EdgeNullException, self.null_exception)
    
    @property
    def edge(self) -> Edge:
        return self.operand
    
    @property
    def is_edge_entity_register(self) -> bool:
        return isinstance(self, EdgeEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EdgeEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    

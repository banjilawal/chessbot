# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import NodeNullException
from operand import EntityRegister, Node


class NodeEntityRegister(EntityRegister[Node]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Node
        null_exception: NodeNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Node = Type[Node],
            null_exception: NodeNullException = NodeNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Node:
        return cast(Node, self.a)
    
    @property
    def null_exception(self) -> NodeNullException:
        return cast(NodeNullException, self.null_exception)
    
    @property
    def node(self) -> Node:
        return self.operand
    
    @property
    def is_node_entity_register(self) -> bool:
        return isinstance(self, NodeEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    

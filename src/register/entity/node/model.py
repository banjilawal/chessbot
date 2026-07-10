# src/model/register/entity/model.py

"""
Module: model.register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import NodeNullException
from model import EntityRegister, Node


class NodeEntityRegister(EntityRegister[Node]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Node
        null_exception: NodeNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Node = Type[Node],
            null_exception: NodeNullException = NodeNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Node:
        return cast(Node, self.a)
    
    @property
    def null_exception(self) -> NodeNullException:
        return cast(NodeNullException, self.null_exception)
    
    @property
    def node(self) -> Node:
        return self.model
    
    @property
    def is_node_entity_register(self) -> bool:
        return isinstance(self, NodeEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    

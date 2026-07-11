# src/blueprint/model/state/node/blueprint.py

"""
Module: blueprint.model.state.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import StateModelBlueprint
from err import NodeNullException
from model import Node, Square

@dataclass
class NodeBlueprint(StateModelBlueprint[Node]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Node object.

    Attributes:
        square: Square
        priority: Optional[int]
        predecessor: Optional[Node]
        
    Provides:

     Super Class:
        StateModelBlueprint
     """
    """
    Args:
        priority: int
        square: Square
        predecessor: Optional[Node]
        id: Optional[int]
        null_exception: NodeNullException
        owner: Node
        owner_name: str
    """
    priority: int
    square: Square
    predecessor: Optional[Node]
    id: Optional[int] | None = None
    null_exception: NodeNullException = NodeNullException()
    model_class: Node = Type[Node]
    owner_name: str = type(owner).__name__

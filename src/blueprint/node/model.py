# src/blueprint/node/model.py

"""
Module: blueprint.node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import Blueprint, Node, Square

@dataclass
class NodeBlueprint(Blueprint[Node]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Node object.

    Attributes:
        square: Square
        priority: Optional[int]
        predecessor: Optional[Node]
        null_exception: NodeNullException
        model_type: Node
        
    Provides:

     Super Class:
        Blueprint
     """
    priority: int
    square: Square
    predecessor: Optional[Node]
    id: Optional[int] | None = None
    null_exception: NodeNullException = NodeNullException()
    model_type: Node = Node

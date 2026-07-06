# src/blueprint/model/node/blueprint.py

"""
Module: blueprint.model.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from model import Node, Square

@dataclass
class NodeBlueprint(Blueprint[Node]):
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
        Blueprint
     """
    priority: int
    square: Square
    predecessor: Optional[Node]
    id: Optional[int] | None = None

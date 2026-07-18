# src/blueprint/container/state/edge/blueprint.py

"""
Module: blueprint.container.state.edge.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import StateContainerBlueprint
from err import EdgeNullException
from container import Edge, Node, Square

@dataclass
class EdgeBlueprint(StateContainerBlueprint[Edge]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Edge object.

    Attributes:
        square: Square
        priority: Optional[int]
        predecessor: Optional[Edge]
        
    Provides:

     Super Class:
        StateContainerBlueprint
     """
    """
    Args:
        label: int
        head: Node
        tail: Node
        distance: int
        weight: Optional[int]
        heuristic: Optional[int]
        null_exception: EdgeNullException
        owner: Edge
        owner_name: str
    """
    label: int
    head: Node
    tail: Node
    distance: int
    weight: Optional[int]
    heuristic: Optional[int]
    null_exception: EdgeNullException = EdgeNullException()
    container_class: Edge = Type[Edge]
    owner_name: str = type(owner).__name__

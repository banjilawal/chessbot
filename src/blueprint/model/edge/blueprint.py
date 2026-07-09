# src/blueprint/model/edge/blueprint.py

"""
Module: blueprint.model.edge.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import Blueprint
from err import EdgeNullException
from model import Edge, Node, Square

@dataclass
class EdgeBlueprint(Blueprint[Edge]):
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
        Blueprint
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
    owner: Edge = Type[Edge]
    owner_name: str = type(owner).__name__

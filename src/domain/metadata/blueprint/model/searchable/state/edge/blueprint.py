# src/domain/metadata/blueprint/model/searchable/state/edge/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.edge.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from err import EdgeNullException
from domain.model import Edge, Node


@dataclass
class EdgeBlueprint(StateModelBlueprint[Edge]):
    """
     Role:
        1.  Metadata
        -  DTO
        
    Responsibilities:
        1.  Provides values for hydrating a Edge object.

    Attributes:
        square: Square
        priority: Optional[int]
        predecessor: Optional[Edge]
        
    Provides:

     Super Class:
        StateModelBlueprint
     """
    """
    Args:
        label: int
        head: Node
        tail: Node
        distance: int
        weight: Optional[int]
        heuristic: Optional[int]
        domain_null_exception: EdgeNullException
        owner: Edge
        owner_name: str
    """
    label: int
    head: Node
    tail: Node
    distance: int
    weight: Optional[int]
    heuristic: Optional[int]
    domain_null_exception: EdgeNullException = EdgeNullException()
    domain_class: Edge = Type[Edge]
    owner_name: str = type(owner).__name__

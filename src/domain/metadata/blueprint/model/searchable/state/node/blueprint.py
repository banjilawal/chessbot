# src/domain/metadata/blueprint/model/searchable/state/node/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Type

from domain.metadata.blueprint import StateModelBlueprint
from err import NodeNullException
from domain.model import Node, Square

@dataclass
class NodeBlueprint(StateModelBlueprint[Node]):
    """
     Role:
        1.  Metadata
        
    Responsibilities:
        1.  Provides values for hydrating a Node object.

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
        domain_null_exception: NodeNullException
        owner: Node
        owner_name: str
    """
    priority: int
    square: Square
    predecessor: Optional[Node]
    id: Optional[int] | None = None
    domain_null_exception: NodeNullException = NodeNullException()
    domain_class: Node = Type[Node]
    owner_name: str = type(owner).__name__

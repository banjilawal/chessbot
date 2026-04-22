# src/model/blueprint/node/model.py

"""
Module: model.blueprint.node.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Blueprint, Node, Square


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
        
    Provides:

     Super Class:
        Blueprint
     """
    _priority: int
    _square: Square
    _predecessor: Optional[Node]
    
    def __init__(
            self, 
            square: Square,
            priority: Optional[int],
            predecessor: Optional[Node] | None = None,
    ):
        """
        Args:
            square: Square
            priority: Optional[int]
            predecessor: Optional[Node]
        """
        super().__init__()
        self._square = square
        self._priority = priority
        self._predecessor = predecessor

    @property
    def square(self) -> int:
        return self._square
    
    @property
    def priority(self) -> int:
        return self._priority
    
    @property
    def predecessor(self) -> Optional[Node]:
        return self._predecessor
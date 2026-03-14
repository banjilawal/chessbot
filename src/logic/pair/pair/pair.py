# src/logic/node/pair/pair.py

"""
Module: logic.node.pair.
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List

from logic.node import Node


@dataclass
class NodePair:
    """
    # RESPONSIBILITY:
    1.  Provide the order of nodes which are derived from a SquareSpan. Spans do
        not guarantee the order of spanned squares matches order in the graph.
    2.  Indicates the natural direction of an asymmetric edge between the nodes.
    """
    head: Node
    tail: Node
    
    @property
    def members(self) -> List[Node]:
        """Puts the head and tail nodes into a list."""
        return [self.head, self.tail]
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodePair):
            return self.head == other.head and self.tail == other.tail
        return False
    

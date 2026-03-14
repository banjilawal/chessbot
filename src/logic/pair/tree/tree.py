# src/logic/pair/tree.py

"""
Module: logic.pair.tree
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List

from logic.node import Node, NodePairList
from logic.pair.pair.service.service import NodePairService


@dataclass
class NodeTree:
    """
    # RESPONSIBILITY:
    1.  Represents the NodePairs emanating from a source. The tree might have one
        root or subtrees.
    2.  It does not contain any link information
    """
    root: Node
    branches: List[NodePairList]
    integrity_service: NodePairService = NodePairService()
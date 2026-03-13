# src/logic/node/pair/array.py

"""
Module: logic.node.pair.array
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from logic.node import NodePair


@dataclass
class NodePairList:
    """
    NodePairList's physical structure can be either
    a list or tree.
    """
    items: List[NodePair]
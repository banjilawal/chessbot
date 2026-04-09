# src/model/graph/edge/model.py

"""
Module: model.graph.edge.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import dataclasses

from model import Edge, Node
from stack import StackService


@dataclasses
class Graph:
    nodes: StackService[Node]
    edges: StackService[Edge]

    
    
    
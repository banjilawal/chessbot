# src/model/query/stack/node/model.py

"""
Module: model.query.stack.node.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Node, NodeContext
from model.query import StackQuery


@dataclass
class NodeQuery(StackQuery[Node]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of nodes to search with context.


    Attributes:
        items: List[Node]
        context: NodeContext

    Provides:

    Super Class:
        StackQuery
    """
    items: List[Node]
    context: NodeContext


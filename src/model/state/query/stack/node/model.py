# src/model/state/query/stack/node/model/state.py

"""
Module: model.state.query.stack.node.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Node, NodeContext
from model.query import StackQuery
from collection.stack import VertexStackService


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
        stack: NodeStackService
        context: NodeContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: VertexStackService
    context: NodeContext


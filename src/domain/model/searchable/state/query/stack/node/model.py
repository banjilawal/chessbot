# src/domain/model/state/query/stack/node/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.node.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Node, NodeContext
from domain.model import StackQuery
from collection.stack import VertexStackService


@dataclass
class NodeQuery(StackQuery[Node]):
    """
    Role:
        -  Model
        -  Search
        -  Stateless Data-Holder

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


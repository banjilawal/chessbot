# src/operand/state/query/stack/node/operand/state.py

"""
Module: operand.state.query.stack.node.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Node, NodeContext
from operand.query import StackQuery
from stack import NodeStackService


@dataclass
class NodeQuery(StackQuery[Node]):
    """
    Role:
        -   Operand
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
    stack: NodeStackService
    context: NodeContext


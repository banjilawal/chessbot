# src/operand/state/query/stack/edge/operand/state.py

"""
Module: operand.state.query.stack.edge.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Edge, EdgeContext
from operand.query import StackQuery
from stack import EdgeStackService


@dataclass
class EdgeQuery(StackQuery[Edge]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of edges to search with context.


    Attributes:
        stack: EdgeStackService
        context: EdgeContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: EdgeStackService
    context: EdgeContext


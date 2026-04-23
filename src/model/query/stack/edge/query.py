# src/query/stack/edge/query.py

"""
Module: query.stack.edge.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Edge, EdgeContext
from model.query import StackQuery


@dataclass
class EdgeQuery(StackQuery[Edge]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of edges to search with context.


    Attributes:
        stack: List[Edge]
        context: EdgeContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Edge]
    context: EdgeContext


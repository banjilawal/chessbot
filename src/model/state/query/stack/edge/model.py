# src/model/state/query/stack/edge/model/state.py

"""
Module: model.state.query.stack.edge.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Edge, EdgeContext
from model.query import StackQuery
from stack import EdgeStackService


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
        stack: EdgeStackService
        context: EdgeContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: EdgeStackService
    context: EdgeContext


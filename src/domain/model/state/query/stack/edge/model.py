# src/domain/model/state/query/stack/edge/dossier/model/state.py

"""
Module: domain.model.state.query.stack.edge.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Edge, EdgeContext
from domain.model import StackQuery
from collection.stack import EdgeStackService


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


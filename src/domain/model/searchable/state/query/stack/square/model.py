# src/domain/model/searchable/state/query/stack/square/dossier/model/searchable/state.py

"""
Module: domain.model.searchable.state.query.stack.square.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Square, SquareContext
from domain.model import StackQuery
from collection.stack import SquareStackService


@dataclass
class SquareQuery(StackQuery[Square]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

    Responsibilities:
        1.  A list of squares to search with context.


    Attributes:
        stack: SquareStackService
        context: SquareContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: SquareStackService
    context: SquareContext


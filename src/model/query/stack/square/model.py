# src/model/query/stack/square/model.py

"""
Module: model.query.stack.square.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Square, SquareContext
from model.query import StackQuery


@dataclass
class SquareQuery(StackQuery[Square]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of squares to search with context.


    Attributes:
        stack: List[Square]
        context: SquareContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Square]
    context: SquareContext


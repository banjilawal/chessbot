# src/query/stack/square/query.py

"""
Module: query.stack.square.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Square, SquareContext
from query import StackQuery


@dataclass
class SquareStackQuery(StackQuery[Square]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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


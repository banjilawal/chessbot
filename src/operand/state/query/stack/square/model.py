# src/operand/state/query/stack/square/operand/state.py

"""
Module: operand.state.query.stack.square.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operand import Square, SquareContext
from operand.query import StackQuery
from stack import SquareStackService


@dataclass
class SquareQuery(StackQuery[Square]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

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


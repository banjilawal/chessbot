# src/operand/state/query/stack/board/operand/state.py

"""
Module: operand.state.query.stack.board.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Board, BoardContext
from operand.query import StackQuery
from stack import BoardStackService


@dataclass
class BoardQuery(StackQuery[Board]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of boards to search with context.


    Attributes:
        stack: BoardStackService
        context: BoardContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: BoardStackService
    context: BoardContext


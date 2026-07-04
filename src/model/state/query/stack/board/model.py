# src/model/state/query/stack/board/model/state.py

"""
Module: model.state.query.stack.board.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Board, BoardContext
from model.query import StackQuery
from stack import BoardStackService


@dataclass
class BoardQuery(StackQuery[Board]):
    """
    Role:
        -   Model
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


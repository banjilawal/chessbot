# src/model/query/stack/board/model.py

"""
Module: model.query.stack.board.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Board, BoardContext
from model.query import StackQuery


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
        items: List[Board]
        context: BoardContext

    Provides:

    Super Class:
        StackQuery
    """
    items: List[Board]
    context: BoardContext


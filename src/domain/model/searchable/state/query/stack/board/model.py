# src/domain/model/state/query/stack/board/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.board.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Board, BoardContext
from domain.model import StackQuery
from collection.stack import BoardStackService


@dataclass
class BoardQuery(StackQuery[Board]):
    """
    Role:
        -  Model
        -  Search
        -  Stateless Data-Holder

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


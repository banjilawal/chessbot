# src/operand/state/query/stack/rank/operand/state.py

"""
Module: operand.state.query.stack.rank.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from operand import Rank, RankContext
from operand.query import StackQuery



@dataclass
class RankQuery(StackQuery[Rank]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of ranks to search with context.


    Attributes:
        stack: RankStackService
        context: RankContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: RankStackService
    context: RankContext


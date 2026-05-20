# src/model/query/stack/rank/model.py

"""
Module: model.query.stack.rank.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Rank, RankContext
from model.query import StackQuery



@dataclass
class RankQuery(StackQuery[Rank]):
    """
    Role:
        -   Model
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


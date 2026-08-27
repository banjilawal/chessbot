# src/domain/model/state/query/stack/rank/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.rank.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Rank, RankContext
from domain.model import StackQuery



@dataclass
class RankQuery(StackQuery[Rank]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

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


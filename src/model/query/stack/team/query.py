# src/query/stack/team/query.py

"""
Module: query.stack.team.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model.query import StackQuery
from model import Team, TeamContext



@dataclass
class TeamQuery(StackQuery[Team]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of teams to search with context.


    Attributes:
        stack: List[Team]
        context: TeamContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Team]
    context: TeamContext


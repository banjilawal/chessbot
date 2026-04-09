# src/query/stack/team/query.py

"""
Module: query.stack.team.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Team, TeamContext
from query import StackQuery


@dataclass
class TeamStackQuery(StackQuery[Team]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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


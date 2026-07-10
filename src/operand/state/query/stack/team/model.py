# src/operand/state/query/stack/team/operand/state.py

"""
Module: operand.state.query.stack.team.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operand.query import StackQuery
from operand import Team, TeamContext
from stack import TeamStackService


@dataclass
class TeamQuery(StackQuery[Team]):
    """
    Role:
        -   Operand
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
    stack: TeamStackService
    context: TeamContext


# src/model/query/stack/team/model.py

"""
Module: model.query.stack.team.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model.query import StackQuery
from model import Team, TeamContext
from stack import TeamStackService


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
    stack: TeamStackService
    context: TeamContext


# src/domain/model/state/query/stack/team/dossier/model/state.py

"""
Module: domain.model.state.query.stack.team.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from dataclasses import dataclass

from domain.model import StackQuery
from domain.model import Team, TeamContext
from collection.stack import TeamStackService


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


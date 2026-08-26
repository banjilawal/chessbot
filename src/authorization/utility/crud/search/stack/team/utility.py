# src/authorization/utility/crud/search/stack/team/utility.py

"""
Module: authorization.utility.crud.search.stack.team.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackSearchContextValidator, TeamContextValidator
from authorization import StackSearchPermissionUtility
from domain import TeamSearchSearchContext


@dataclass
class TeamStackSearchPermissionUtility(StackSearchPermissionUtility[TeamSearchSearchContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the TeamSearchAuthorizer needs to evaluate a TeamSearchRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        team_context_validator: TeamContextValidator
        
    Provides:

    Super Class:
        StackSearchPermissionUtility
    """
    validator: Dict[str, StackSearchContextValidator] = field(
        default_factory=lambda: {
            "team_context_validator": TeamContextValidator(),
        }
    )
    
    @property
    def team_context_validator(self) -> TeamContextValidator:
        return self.resources["team_context_validator"]

    
# src/authorization/utility/crud/delete/stack/team/utility.py

"""
Module: authorization.utility.crud.delete.stack.team.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackDeleteContextValidator, TeamContextValidator
from authorization import StackDeletePermissionUtility
from domain import TeamDeleteContext


@dataclass
class TeamStackDeletePermissionUtility(StackDeletePermissionUtility[TeamDeleteContext]):
    """
    Role:
        -   Utility

    Responsibilities:
        1.  Bundles resources the TeamDeleteAuthorizer needs to evaluate a TeamDeleteRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        team_context_validator: TeamContextValidator
        
    Provides:

    Super Class:
        StackDeletePermissionUtility
    """
    validator: Dict[str, StackDeleteContextValidator] = field(
        default_factory=lambda: {
            "team_context_validator": TeamContextValidator(),
        }
    )
    
    @property
    def team_context_validator(self) -> TeamContextValidator:
        return self.resources["team_context_validator"]

    
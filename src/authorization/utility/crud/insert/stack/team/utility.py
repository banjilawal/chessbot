# src/authorization/utility/crud/insert/stack/team/utility.py

"""
Module: authorization.utility.crud.insert.stack.team.utility
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from assurance import StackInsertContextValidator, TeamContextValidator
from authorization import StackInsertPermissionUtility
from domain import TeamInsertContext


@dataclass
class TeamStackInsertPermissionUtility(StackInsertPermissionUtility[TeamInsertContext]):
    """
    Role:
        - Utility

    Responsibilities:
        1.  Bundles resources the TeamInsertAuthorizer needs to evaluate a TeamInsertRequest.

    Attributes:
        validator: Dict[str, ContextValidator]
        team_context_validator: TeamContextValidator
        
    Provides:

    Super Class:
        StackInsertPermissionUtility
    """
    validator: Dict[str, StackInsertContextValidator] = field(
        default_factory=lambda: {
            "team_context_validator": TeamContextValidator(),
        }
    )
    
    @property
    def team_context_validator(self) -> TeamContextValidator:
        return self.resources["team_context_validator"]

    
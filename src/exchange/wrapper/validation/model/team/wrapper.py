# src/exchange/wrapper/validation/model/team/wrapper.py

"""
Module: exchange.wrapper.validation.model.team.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from domain import Team
from exchange import ModelValidationResponseWrapper, TeamValidationRequest, TeamValidationResponder
from util import LoggingLevelRouter


class TeamValidationResponseWrapper(
    ModelValidationResponseWrapper[Team]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Team
                _   The TeamBlueprint
            from TeamValidationResponse.

    Attributes:
        responder: TeamValidationResponder
        
    Provides:
        -   def execute(self, request: TeamValidationRequest) -> Any

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[TeamValidationResponder] | None = None,
    ):
        """
        Args:
            responder: TOptional[TeamValidationResponder]
        """
        super().__init__(responder=responder or TeamValidationResponder())
    
    @property
    def responder(self) -> TeamValidationResponder:
        return cast(TeamValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: TeamValidationRequest) -> Any:
        pass
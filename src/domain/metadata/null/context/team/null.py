# src/domain/metadata/null/context/team/null.py

"""
Module: domain.metadata.null.context.team.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullWarningSet,
    TeamContextBlueprintNullException, TeamContextCarrierNullException, TeamContextNullException
)


class TeamContextNullWarningSet(ContextNullWarningSet[TeamContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Team's integrity cycle.

    Attributes:
        model: TeamContextNullException
        carrier: TeamContextCarrierNullException
        blueprint: TeamContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[TeamContextNullException] | None = None,
            carrier: Optional[TeamContextCarrierNullException] | None = None,
            blueprint: Optional[TeamContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TeamContextNullException]
            carrier: Optional[TeamContextCarrierNullException]
            blueprint: Optional[TeamContextBlueprintNullException]
        """
        super().__init__(
            model=model or TeamContextNullException(),
            carrier=carrier or TeamContextCarrierNullException(),
            blueprint=blueprint or TeamContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> TeamContextNullException:
        return cast(TeamContextNullException, super().model)
    
    @property
    def carrier(self) -> TeamContextCarrierNullException:
        return cast(TeamContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TeamContextBlueprintNullException:
        return cast(TeamContextBlueprintNullException, super().blueprint)
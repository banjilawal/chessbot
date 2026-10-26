# src/domain/metadata/nulls/struct/binder/team/group.py

"""
Module: domain.metadata.nulls.struct.binder.team.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import BinderNullWarningSet, TeamBinder
from err import (
    TeamBinderBlueprintNullException, TeamBinderCarrierNullException,
    TeamBinderNullException
)


class TeamBinderNullWarningSet(BinderNullWarningSet[TeamBinder]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a TeamBinder's integrity cycle.

    Attributes:
        model: TeamBinderNullException
        carrier: TeamBinderCarrierNullException
        blueprint:TeamBinderBlueprintNullException

    Provides:

    Super Class:
        BinderNullGroup
    """

    
    def __init__(
            self,
            model: Optional[TeamBinderNullException] | None = None,
            carrier: Optional[TeamBinderCarrierNullException] | None = None,
            blueprint: Optional[TeamBinderBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[TeamBinderNullException]
            carrier: Optional[TeamBinderCarrierNullException]
            blueprint: Optional[TeamBinderBlueprintNullException]
        """
        super().__init__(
            model=model or TeamBinderNullException(),
            carrier=carrier or TeamBinderCarrierNullException(),
            blueprint=blueprint or TeamBinderBlueprintNullException(),
        )
        
    @property
    def struct(self) -> TeamBinderNullException:
        return cast(TeamBinderNullException, super().model)
    
    @property
    def model(self) -> TeamBinderNullException:
        return self.struct
    
    @property
    def carrier(self) -> TeamBinderCarrierNullException:
        return cast(TeamBinderCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> TeamBinderBlueprintNullException:
        return cast(TeamBinderBlueprintNullException, super().blueprint)
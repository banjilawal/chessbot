# src/assurance/toolkit/model/team/toolkit.py

"""
Module: assurance.toolkit.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, TeamBlueprintLoader, TeamHelperTable
from domain import Team, TeamManifest, TeamNullGroup, TeamTypeUnion


class TeamValidatorToolkit(ModelValidatorToolkit[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Team attribute validators and type metadata.

    Attributes:
        helper: TeamManifest
        metadata: TeamHelperTable
        blueprint_loader: TeamBlueprintLoader

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[TeamManifest] | None = None,
            helper: Optional[TeamHelperTable] | None = None,
            blueprint_loader: Optional[TeamBlueprintLoader] | None = None,
    ):
        """
        Args:
            helper: Optional[TeamManifest]
            metadata: Optional[TeamHelperTable]
            blueprint_loader: Optional[TeamBlueprintLoader]
        """
        super().__init__(
            helper=helper or TeamHelperTable(),
            metadata=metadata or TeamManifest(),
            blueprint_loader=blueprint_loader or TeamBlueprintLoader(),
        )
    
    @property
    def helper(self) -> TeamHelperTable:
        return cast(TeamHelperTable, super().helper)
    
    @property
    def metadata(self) -> TeamManifest:
        return cast(TeamManifest, super().metadata)
    
    @property
    def nulls(self) -> TeamNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> TeamTypeUnion:
        return self.metadata.types
    
    @property
    def blueprint_loader(self) -> TeamBlueprintLoader:
        return cast(TeamBlueprintLoader, super().blueprint_loader)
    
    Responsibilities:
    1.
    Bundles
    validatorClients
    a
    TeamValidator
    needs.


Attributes:
board_client: BoardValidatorClient
owner_client: PlayerValidatorClient
blueprint_loader: TeamBlueprintLoader

Provides:

Super
Class:
ModelHelperTable
"""
_board_client: BoardValidatorClient
_owner_client: PlayerValidatorClient
_blueprint_loader: TeamBlueprintLoader

def __init__(
        self,
        board_client: Optional[BoardValidatorClient] | None = None,
        owner_client: Optional[PlayerValidatorClient] | None = None,
        blueprint_loader: Optional[TeamBlueprintLoader] | None = None,

        identity_service: Optional[IdentityService] | None = None,
        priming_validator: Optional[PrimingValidator] | None = None,
):
    """
Args:
board_client: Optional[BoardValidatorClient]
owner_client: Optional[PlayerValidatorClient]


identity_service: Optional[IdentityService]
priming_validator: Optional[PrimingValidator]
"""
super().__init__(
    identity_service=identity_service,
    priming_validator=priming_validator,
)
self._board_client = board_client or BoardValidatorClient()
self._owner_client = owner_client or PlayerValidatorClient()
self._blueprint_loader = blueprint_loader or TeamBlueprintLoader()

@property
def board_client(self) -> BoardValidatorClient:
return self._board_client

@property
def owner_client(self) -> PlayerValidatorClient:
return self._owner_client

@property
def blueprint_loader(self) -> TeamBlueprintLoader:
return self._blueprint_loader
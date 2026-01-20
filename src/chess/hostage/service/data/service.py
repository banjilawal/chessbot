# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.hostage import CaptivityContextService, HostageManifest, HostageManifestValidator
from chess.square.service.exception.insertion import OccupiedSquareCannotRecieveFormationException
from chess.square.state import SquareState
from chess.system import EntityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.square import (
    AddingFormationToSquareFailedException, Square, SquareBuilder, HostageManifestServiceException,
    SquareValidator
)
from chess.team import FriendCannotCaptureFriendException, Team, TeamService
from chess.token import (
    CombatantActivityState, CombatantToken, KingToken, Token, TokenBoardState, TokenContext,
    TokenDoesNotExistForRemovalException,
    TokenService
)


class HostageManifestService(EntityService[HostageManifest]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   HostageManifestService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "HostageManifestService"
    
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: HostaManifestBuilder = HostgaeManifestBuilder(),
            validator: HostageManifestValidator = HostageManifestValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SquareFactory)
            *   validator (SquareValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> HostageManfiestBuilder:
        """get SquareBuilder"""
        return cast(HostageManfiestBuilderr, self.entity_builder)
    
    @property
    def validator(self) -> HostageManifestValidator:
        """get SquareValidator"""
        return cast(HostageManifestValidator, self.entity_validator)
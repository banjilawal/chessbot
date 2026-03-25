# src/logic/game/service/service.py

"""
Module: logic.game.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.system import IntegrityService, id_emitter
from logic.game import Game, GameBuildProcess, GameValidationProcess


class GameService(IntegrityService[Game]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Game microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Game state by providing single entry and exit points to Game
        lifecycle.

    Super Class:
        *   IntegrityService

    # PROVIDES:
        *   build: --> GameBuildProcess
        *   validation: --> GameValidationProcess


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    DEFAULT_NAME = "GameService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: GameBuildProcess = GameBuildProcess(),
            validator: GameValidationProcess = GameValidationProcess(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   build (GameFactory)
            *   validation (GameValidationProcess)

        # RETURNS:
        None

        Raises:
        """
        method = "GameService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def build(self) -> GameBuildProcess:
        """get GameBuildProcess"""
        return cast(GameBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> GameValidationProcess:
        """get GameValidationProcess"""
        return cast(GameValidationProcess, self.entity_validator)
    
    
    
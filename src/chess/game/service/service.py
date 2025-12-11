# src/chess/game/service/service.py

"""
Module: chess.game.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.game import Game, GameBuilder, GameValidator


class GameService(EntityService[Game]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Game State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Game state by providing single entry and exit points to Game
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   builder: --> GameBuilder
        *   validator: --> GameValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "GameService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: GameBuilder = GameBuilder(),
            validator: GameValidator = GameValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (GameFactory)
            *   validator (GameValidator)

        # Returns:
        None

        # Raises:
        None
        """
        method = "GameService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> GameBuilder:
        """get GameBuilder"""
        return cast(GameBuilder, self.entity_builder)
    
    @property
    def validator(self) -> GameValidator:
        """get GameValidator"""
        return cast(GameValidator, self.entity_validator)
    
    
    
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
    1.  Public facing API.
    2.  Protects Game instance's internal state.
    3.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    4.  Single entry point Game integrity lifecycle management with GameBuilder and GameValidator.

    # PARENT
        *   Entity
    
    # PROVIDES:
        *   GameBuilder
        *   GameValidator

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    See EntityService class for inherited attributes.
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
            *   builder (GameBuilder)
            *   validator (GameValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> GameBuilder:
        """get GameBuilder"""
        return cast(GameBuilder, self.entity_builder)
    
    @property
    def validator(self) -> GameValidator:
        """get GameValidator"""
        return cast(GameValidator, self.entity_validator)
    
    
    
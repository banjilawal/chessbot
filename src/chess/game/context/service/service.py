# src/chess/game/context/service/service.py

"""
Module: chess.game.context.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.game.finder.finder import GameFinder
from chess.system import ContextService, id_emitter
from chess.game import GameContext, GameContextBuilder, GameContextValidator


class GameContextService(ContextService[GameContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Game search microservice.
    2.  Encapsulates query building and searching functions into a single extendable module that easy to use.

    # PARENT
        *   ContextService

    # PROVIDES:
        *   GameSnapshotFinder
        *   GameContextBuilder
        *   GameContextValidator

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "GameContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: GameFinder = GameFinder(),
            builder: GameContextBuilder = GameContextBuilder(),
            validator: GameContextValidator = GameContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (GameFinder): Default value - GameFinder()
            *   builder (GameContextBuilder): Default value - GameContextBuilder()
            *   validator (GameContextValidator): Default value - GameContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "GameContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
        
    @property
    def finder(self) -> GameFinder:
        return cast(GameFinder, self.entity_finder)
    
    @property
    def builder(self) -> GameContextBuilder:
        return cast(GameContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> GameContextValidator:
        return cast(GameContextValidator, self.entity_validator)
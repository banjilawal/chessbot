# src/logic/game/service/transaction.py

"""
Module: logic.game.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.game.finder.finder import GameFinder
from logic.system import QueryService, id_emitter
from logic.game import GameContext, GameContextBuilder, GameContextValidationTransaction


class GameQueryService(QueryService[GameContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Game search microservice API.
    2.  Provides a map aware utility for searching Game objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Game search results by having single entry and exit points for the
        Game search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   GameQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    DEFAULT_NAME = "GameQueryService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: GameFinder = GameFinder(),
            builder: GameContextBuilder = GameContextBuilder(),
            validator: GameContextValidationTransaction = GameContextValidationTransaction(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   route (GameFinder): Default value - GameFinder()
            *   build (GameContextBuilder): Default value - GameContextBuilder()
            *   validation (GameContextValidationTransaction): Default value - GameContextValidationTransaction()

        # RETURNS:
        None

        Raises:
        """
        method = "GameQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> GameFinder:
        """Get GameFinder instance."""
        return cast(GameFinder, self.entity_finder)
    
    @property
    def build(self) -> GameContextBuilder:
        """Get GameContextBuilder instance."""
        return cast(GameContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> GameContextValidationTransaction:
        """Get GameContextValidationTransaction instance."""
        return cast(GameContextValidationTransaction, self.entity_validator)
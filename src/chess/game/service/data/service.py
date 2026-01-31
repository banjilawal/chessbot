# src/chess/game/database/core/service.py

"""
Module: chess.game.database.core.stack
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast


from chess.system import StackService, LoggingLevelRouter, id_emitter
from chess.game import Game, GameContext, GameContextService, GameService


class GameStackService(StackService[Game]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching Game collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Games are put in the collection.
    4.  Assure updates do not break the integrity individual bag in the collection or
        the collection itself.
    5.  Provide Game stack data structure with no guarantee of uniqueness.
    6.  Search utility.
    
    # PARENT:
        *   StackService

    # PROVIDES:
        *   GameStackService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    DEFAULT_NAME = "GameStackService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Game] = List[Game],
            service: GameService = GameService(),
            context_service: GameContextService = GameContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   bag (List[Game]): = List[Game]
            *   service (GameService): = GameService()
            *   context_service (GameContextService): = GameContextService()

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        
    @property
    def game_service(self) -> GameService:
        return cast(GameService, self.entity_service)
    
    @property
    def game_context_service(self) -> GameContextService:
        return cast(GameContextService, self.context_service)

    # @property
    # def data(self) -> GameService:
    #     return cast(GameService, self.data)
    #
    # @property
    # def builder(self) -> GameFactory:
    #     return cast(GameFactory, self.service.item_builder)
    #
    # @property
    # def validator(self) -> GameValidator:
    #     return cast(GameValidator, self.service.item_validator)
    #
    # @property
    # def context_service(self) -> GameContextService:
    #     return cast(GameContextService, self.context_service)
    #
    # @LoggingLevelRouter.monitor
    # def push_item(self, item: Game) -> InsertionResult[Game]:
    #     method = "GameStackService.push"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #         self.bag.append(item)
    #
    #         return InsertionResult.success(payload=item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             GameDataServiceException(ex=ex, message=f"{method}: {GameDataServiceException.DEFAULT_MESSAGE}")
    #         )
    #
    # @LoggingLevelRouter.monitor
    # def search(self, map: GameContext) -> SearchResult[List[Game]]:
    #     method = "GameStackService.finder"
    #     game_context_service = cast(GameContextService, self.context_service)
    #
    #     return self.context_service.finder.find(
    #         dataset=self.bag,
    #         map=map,
    #         context_validator=self.context_service.item_validator
    #     )

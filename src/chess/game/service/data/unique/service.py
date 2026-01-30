# src/chess/game/database/service_.py

"""
Module: chess.game.database.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import List, cast

from chess.game import Game, GameContext, GameContextService, GameStackService, GameService
from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter
)


class UniqueGameDataService(Database[Game]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag managed by GameStackService are unique.
    2.  Guarantee consistency of records in GameStackService.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "UniqueGameDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: GameStackService = GameStackService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   member_service (GameStackService): = GameStackService()

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, data_service=data_service)
    
    @property
    def game_service(self) -> GameService:
        return cast(GameStackService, self.data_service).game_service
    
    @property
    def context_service(self) -> GameContextService:
        return cast(GameStackService, self.data_service).game_context_service
    
    @property
    def size(self) -> int:
        return self.data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self.data_service.is_empty
    
    @LoggingLevelRouter.monitor
    def add_game(self, game: Game) -> InsertionResult[Game]:
        return self.push_unique_item(game)
    
    @LoggingLevelRouter.monitor
    def undo_add_game(self) -> DeletionResult[Game]:
        return self.data_service.pop()
    
    @LoggingLevelRouter.monitor
    def search_games(self, context: GameContext) -> SearchResult[List[Game]]:
        return self.data_service.search(context)
    
    # @LoggingLevelRouter.monitor
    # def push_unique_item(self, item: Game) -> InsertionResult[Game]:
    #     method = "UniqueGameDataService.push_unique"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #
    #         context_validation = self._member_service.context_service.item_builder.build(id=item.id)
    #         if context_validation.is_failure():
    #             return InsertionResult.failure(context_validation.exception)
    #
    #         search_result = self._member_service.search(map=context_validation.payload)
    #         if search_result.is_failure():
    #             return InsertionResult.failure(search_result.exception)
    #
    #         if search_result.is_success():
    #             return InsertionResult.failure(
    #                 AddingDuplicateGameException(
    #                     f"{method}: {AddingDuplicateGameException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         return self._member_service.push_item(item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             UniqueGameDataServiceException(
    #                 ex=ex,
    #                 message=(
    #                     f"{method}: "
    #                     f"{UniqueGameDataServiceException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )

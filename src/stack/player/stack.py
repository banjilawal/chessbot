# src/stack/player/py

"""
Module: stack.player.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List, cast




class PlayerStackService(StackService[Player]):
    """
    Role:Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Microservice API for managing and searching Player collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Players are put in the collection.
    4.  Assure updates do not break the integrity individual bag in the collection or
        the collection itself.
    5.  Provide Player schema data structure with no guarantee of uniqueness.
    6.  Search utility.
    
    Super Class:
        *   StackService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "PlayerStackService"
    
    def service(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[PlayerPlayer] = List[PlayerPlayer],
            service: PlayerService = PlayerService(),
            context_service: PlayerContextService = PlayerContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   schema (str): = SERVICE_NAME
            *   bag (List[Player]): = List[Player]
            *   service (PlayerService): = PlayerService()
            *   context_service (PlayerQueryService): = PlayerQueryService()

        # RETURNS:
        None

        Raises:
        """
        super().microservice(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        
    @property
    def player_service(self) -> PlayerService:
        return cast(PlayerService, self.entity_service)
    
    @property
    def player_context_service(self) -> PlayerContextService:
        return cast(PlayerContextService, self.context_service)
    

    # @property
    # def data(self) -> PlayerService:
    #     return cast(PlayerService, self.data)
    #
    # @property
    # def build(self) -> PlayerFactory:
    #     return cast(PlayerFactory, self.service.item_builder)
    #
    # @property
    # def validation(self) -> PlayerValidator:
    #     return cast(PlayerValidator, self.service.item_validator)
    #
    # @property
    # def context_service(self) -> PlayerQueryService:
    #     return cast(PlayerQueryService, self.context_service)
    #
    # @LoggingLevelRouter.monitor
    # def push_item(self, item: Player) -> InsertionResult[Player]:
    #     method = "PlayerStackService.push"
    #     try:
    #         validation = self.data.item_validator.validate(item)
    #         if validation.is_failure():
    #             return InsertionResult.failure(validation.exception)
    #         self.bag.append(item)
    #
    #         return InsertionResult.success(payload=item)
    #     except Exception as ex:
    #         return InsertionResult.failure(
    #             PlayerDataServiceException(ex=ex, msg=f"{method}: {PlayerDataServiceException.MSG}")
    #         )
    #
    # @LoggingLevelRouter.monitor
    # def search(self, map: PlayerContext) -> SearchResult[List[Player]]:
    #     method = "PlayerStackService.route"
    #     player_context_service = cast(PlayerQueryService, self.context_service)
    #
    #     return self.context_service.route.find(
    #         collider_candidates=self.bag,
    #         map=map,
    #         context_validator=self.context_service.item_validator
    #     )

# src/stack/game/game.py

"""
Module: stack.game.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class GameStackService(StackService[Game]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Game objects and their lifecycles.
    3.  Ensure integrity of Game data schema
    4.  Stack data structure for Game objects with no guarantee of uniqueness.

    Super Class:
        *   StackService[Game]

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "GameStackService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Game] = List[Game],
            service: GameService = GameService(),
            context_service: GameQueryService = GameQueryService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   bag (List[Team])
            *   service (TeamService)
            *   context_service (TeamQueryService)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "GameService.__init__"
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
    def game_context_service(self) -> GameQueryService:
        return cast(GameQueryService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_game(self, game: Game) -> InsertionResult[Game]:
        """
        # ACTION:
            1.  If the game is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   game (Game)
        # RETURNS:
            *   InsertionResult[Game] containing either:
                    - On failure: Exception.
                    - On success: Game in the payload.
        Raises:
            *   GameDataServiceException
        """
        method = "GameStackService.add_game"
        
        # Handle the case that, the game is unsafe.
        validation = self.game_service.execute.execute(candidate=game)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameInsertionException(
                        msg=f"{method}: {GameInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if an item in the list shares the game's arena. ---#
        search_result = self.game_context_service.finder.find(
            dataset=self.items,
            context=GameContext(arena=game.arena)
        )
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameInsertionException(
                        msg=f"{method}: {GameInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, a game in collection has the same arena.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameInsertionException(
                        msg=f"{method}: {GameInsertionException.ERR_CODE}",
                        ex=ArenaAlreadyContainsGameException(
                            f"{method}: {ArenaAlreadyContainsGameException.MSG}"
                        )
                    )
                )
            )
        # --- Game order is not required. Direct insertion into the collider_candidates is simpler that a push. ---#
        self.items.append(game)
        
        # Handle the case that, the game was not appended to the collider_candidates.
        if game not in self.items:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameInsertionException(
                        msg=f"{method}: {GameInsertionException.ERR_CODE}",
                        ex=AppendingGameDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingGameDirectlyIntoItemsFailedException.ERR_CODE}"
                        )
                    )
                )
            )
        # On success return the game in the InsertionResult
        return InsertionResult.success(payload=game)
    
    @LoggingLevelRouter.monitor
    def delete_game_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Game]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_games_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_games_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Game] containing either:
                    - On failure: Exception.
                    - On success: Game in the payload.
        Raises:
            *   GameDataServiceException
        """
        method = "GameStackService.delete_game_by_id"
        
        # Handle the case that, there are no bag in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameDeletionException(
                        msg=f"{method}: {GameDeletionException.ERR_CODE}",
                        ex=PoppingEmptyGameStackException(
                            f"{method}: {PoppingEmptyGameStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                GameDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                    ex=GameDeletionException(
                        msg=f"{method}: {GameDeletionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for a game with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Game):
                    # Send the exception chain on failure.
                    return DeletionResult.failure(
                        GameDataServiceException(
                            msg=f"ServiceId:{self.id}, {method}: {GameDataServiceException.ERR_CODE}",
                            ex=GameDeletionException(
                                msg=f"{method}: {GameDeletionException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Game, got {type(item).__name__} "
                                    f"instead of a Game."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted game in the DeletionResult. ---#
                game = cast(Game, item)
                self.items.remove(game)
                return DeletionResult.success(payload=game)
        
        # If none of the bag had that id return an empty DeletionResult.
        return DeletionResult.empty()
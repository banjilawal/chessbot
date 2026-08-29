# src/stack/arena/arena.py

"""
Module: stack.arena.arena
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class ArenaStackService(StackService[Arena]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Arena objects and their lifecycles.
    3.  Ensure integrity of Arena data schema
    4.  Stack data structure for Arena objects with no guarantee of uniqueness.

    Super Class:
        *   StackService[Arena]

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "ArenaStackService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Arena] = List[Arena],
            service: ArenaService = ArenaService(),
            context_service: ArenaQueryService = ArenaQueryService(),
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
        method = "ArenaService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def arena_service(self) -> ArenaService:
        return cast(ArenaService, self.entity_service)
    
    @property
    def arena_context_service(self) -> ArenaQueryService:
        return cast(ArenaQueryService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_arena(self, arena: Arena) -> InsertionResult[Arena]:
        """
        # ACTION:
            1.  If the arena is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   arena (Arena)
        # RETURNS:
            *   InsertionResult[Arena] containing either:
                    - On failure: Exception.
                    - On success: Arena in the payload.
        Raises:
            *   ArenaDataServiceException
        """
        method = "ArenaStackService.add_arena"
        
        # Handle the case that, the arena is unsafe.
        validation = self.arena_service.execute.execute(candidate=arena)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaInsertionException(
                        msg=f"{method}: {ArenaInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if an item in the list shares the arena's arena. ---#
        search_result = self.arena_context_service.finder.find(
            dataset=self.items,
            context=ArenaContext(arena=arena.arena)
        )
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaInsertionException(
                        msg=f"{method}: {ArenaInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, a arena in collection has the same arena.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaInsertionException(
                        msg=f"{method}: {ArenaInsertionException.ERR_CODE}",
                        ex=ArenaAlreadyContainsArenaException(
                            f"{method}: {ArenaAlreadyContainsArenaException.MSG}"
                        )
                    )
                )
            )
        # --- Arena order is not required. Direct insertion into the collider_candidates is simpler that a push. ---#
        self.items.append(arena)
        
        # Handle the case that, the arena was not appended to the collider_candidates.
        if arena not in self.items:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaInsertionException(
                        msg=f"{method}: {ArenaInsertionException.ERR_CODE}",
                        ex=AppendingArenaDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingArenaDirectlyIntoItemsFailedException.ERR_CODE}"
                        )
                    )
                )
            )
        # On success return the arena in the InsertionResult
        return InsertionResult.success(payload=arena)
    
    @LoggingLevelRouter.monitor
    def delete_arena_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Arena]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_arenas_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_arenas_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Arena] containing either:
                    - On failure: Exception.
                    - On success: Arena in the payload.
        Raises:
            *   ArenaDataServiceException
        """
        method = "ArenaStackService.delete_arena_by_id"
        
        # Handle the case that, there are no bag in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaDeletionException(
                        msg=f"{method}: {ArenaDeletionException.ERR_CODE}",
                        ex=PoppingEmptyArenaStackException(
                            f"{method}: {PoppingEmptyArenaStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                    ex=ArenaDeletionException(
                        msg=f"{method}: {ArenaDeletionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for a arena with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Arena):
                    # Send the exception chain on failure.
                    return DeletionResult.failure(
                        ArenaDataServiceException(
                            msg=f"ServiceId:{self.id}, {method}: {ArenaDataServiceException.ERR_CODE}",
                            ex=ArenaDeletionException(
                                msg=f"{method}: {ArenaDeletionException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Arena, got {type(item).__name__} "
                                    f"instead of a Arena."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted arena in the DeletionResult. ---#
                arena = cast(Arena, item)
                self.items.remove(arena)
                return DeletionResult.success(payload=arena)
        
        # If none of the bag had that id return an empty DeletionResult.
        return DeletionResult.empty()
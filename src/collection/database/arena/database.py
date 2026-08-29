# src/collection/database/arena/database.py

"""
Module: database.arena.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class ArenaDatabase(Database[Arena]):
    """
    Role:
        _   Frontend
        -  Interface
        -  Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: Microservice[T]

    Provides:
        -  iterator() ->: iter
        -  insert(item: T) -> InsertionResult:
        -  delete_by_id(id: int) -> DeletionResult[T]:
        -  search(context: Context[T]) -> SearchResult[List[T]]

    Role:Unique Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Ensure all bag in managed by ArenaStackService are unique.
    2.  Guarantee consistency of records in ArenaStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "ArenaDatabase"
    _arena_database_core: ArenaStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: ArenaStackService = ArenaStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (ArenaStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._arena_stack_service = data_service
    
    @property
    def microservice(self) -> ArenaService:
        return self._arena_database_core.arena_service
    
    @property
    def context_service(self) -> ArenaQueryService:
        return self._arena_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._arena_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._arena_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_arena(self, arena: Arena) -> InsertionResult[Arena]:
        """
        # ACTION:
            1.  If the arena fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the arena either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _arena_database_core.insert_arena fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   arena (Arena)
        # RETURN:
            *   InsertionResult[Arena] containing either:
                    - On failure: An exception.
                    - On success: Arena in payload.
        Raises:
            *   ArenaDatabaseException
            *   UniqueArenaInsertionException
            *   ArenaDatabaseException
        """
        method = "ArenaDatabase.add_unique_arena"
        
        # --- To assure uniqueness the member_service has to conduct a search. The arena should be validated first. ---#
        
        # Handle the case that, the arenais not safe.
        validation = self.microservice.execute.execute(candidate=arena)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueArenaDataServiceException.ERR_CODE}",
                    ex=UniqueArenaInsertionException(
                        msg=f"{method}: {UniqueArenaInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the arena is already in the collider_candidates before adding it. ---#
        search_result = self.search_arenas(context=ArenaContext(id=arena.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueArenaDataServiceException.ERR_CODE}",
                    ex=UniqueArenaInsertionException(
                        msg=f"{method}: {UniqueArenaInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the arena is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueArenaDataServiceException.ERR_CODE}",
                    ex=UniqueArenaInsertionException(
                        msg=f"{method}: {UniqueArenaInsertionException.ERR_CODE}",
                        ex=AddingDuplicateArenaException(f"{method}: {AddingDuplicateArenaException.MSG}")
                    )
                )
            )
        # --- Use _arena_database_core.insert_arena because order does not matter for the arena access. ---#
        insertion_result = self._arena_database_core.insert_arena(arena=arena)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueArenaDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueArenaDataServiceException.ERR_CODE}",
                    ex=UniqueArenaInsertionException(
                        msg=f"{method}: {UniqueArenaInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_arenas(self, context: ArenaContext) -> SearchResult[List[Arena]]:
        """
        # ACTION:
            1.  Get the result of calling _arena_database_core.delete_arena_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Arena] containing either:
                    - On failure: An exception.
                    - On success: Arena in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   ArenaDatabaseException
            *   ExhaustiveArenaDeletionException
        """
        method = "ArenaDatabase.search_arenas"
        
        # --- Handoff the search responsibility to _arena_database_core. ---#
        search_result = self._arena_database_core.arena_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueArenaDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueArenaDataServiceException.ERR_CODE}",
                    ex=UniqueArenaSearchException(
                        msg=f"{method}: {UniqueArenaSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
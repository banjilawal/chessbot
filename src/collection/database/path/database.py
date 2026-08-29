# src/collection/database/path/database.py

"""
Module: database.path.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class PathDatabase(Database[Path]):
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
    1.  Ensure all bag in managed by PathStackService are unique.
    2.  Guarantee consistency of records in PathStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "PathDatabase"
    _path_database_core: PathStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: PathStackService = PathStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (PathStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._path_stack_service = data_service
    
    @property
    def microservice(self) -> PathService:
        return self._path_database_core.path_service
    
    @property
    def context_service(self) -> PathQueryService:
        return self._path_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._path_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._path_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_path(self, path: Path) -> InsertionResult[Path]:
        """
        # ACTION:
            1.  If the path fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the path either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _path_database_core.insert_path fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   path (Path)
        # RETURN:
            *   InsertionResult[Path] containing either:
                    - On failure: An exception.
                    - On success: Path in payload.
        Raises:
            *   PathDatabaseException
            *   UniquePathInsertionException
            *   PathDatabaseException
        """
        method = "PathDatabase.add_unique_path"
        
        # --- To assure uniqueness the member_service has to conduct a search. The path should be validated first. ---#
        
        # Handle the case that, the pathis not safe.
        validation = self.microservice.execute.execute(candidate=path)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniquePathDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniquePathDataServiceException.ERR_CODE}",
                    ex=UniquePathInsertionException(
                        msg=f"{method}: {UniquePathInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the path is already in the collider_candidates before adding it. ---#
        search_result = self.search_paths(context=PathContext(id=path.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniquePathDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniquePathDataServiceException.ERR_CODE}",
                    ex=UniquePathInsertionException(
                        msg=f"{method}: {UniquePathInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the path is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniquePathDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniquePathDataServiceException.ERR_CODE}",
                    ex=UniquePathInsertionException(
                        msg=f"{method}: {UniquePathInsertionException.ERR_CODE}",
                        ex=AddingDuplicatePathException(f"{method}: {AddingDuplicatePathException.MSG}")
                    )
                )
            )
        # --- Use _path_database_core.insert_path because order does not matter for the path access. ---#
        insertion_result = self._path_database_core.insert_path(path=path)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniquePathDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniquePathDataServiceException.ERR_CODE}",
                    ex=UniquePathInsertionException(
                        msg=f"{method}: {UniquePathInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_paths(self, context: PathContext) -> SearchResult[List[Path]]:
        """
        # ACTION:
            1.  Get the result of calling _path_database_core.delete_path_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Path] containing either:
                    - On failure: An exception.
                    - On success: Path in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   PathDatabaseException
            *   ExhaustivePathDeletionException
        """
        method = "PathDatabase.search_paths"
        
        # --- Handoff the search responsibility to _path_database_core. ---#
        search_result = self._path_database_core.path_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniquePathDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniquePathDataServiceException.ERR_CODE}",
                    ex=UniquePathSearchException(
                        msg=f"{method}: {UniquePathSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
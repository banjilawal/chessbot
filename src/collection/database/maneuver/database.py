# src/collection/database/maneuver/database.py

"""
Module: database.maneuver.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class ManeuverDatabase(Database[Maneuver]):
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
    1.  Ensure all bag in managed by ManeuverStackService are unique.
    2.  Guarantee consistency of records in ManeuverStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "ManeuverDatabase"
    _maneuver_database_core: ManeuverStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: ManeuverStackService = ManeuverStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (ManeuverStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._maneuver_stack_service = data_service
    
    @property
    def microservice(self) -> ManeuverService:
        return self._maneuver_database_core.maneuver_service
    
    @property
    def context_service(self) -> ManeuverQueryService:
        return self._maneuver_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._maneuver_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._maneuver_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_maneuver(self, maneuver: Maneuver) -> InsertionResult[Maneuver]:
        """
        # ACTION:
            1.  If the maneuver fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the maneuver either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _maneuver_database_core.insert_maneuver fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   maneuver (Maneuver)
        # RETURN:
            *   InsertionResult[Maneuver] containing either:
                    - On failure: An exception.
                    - On success: Maneuver in payload.
        Raises:
            *   ManeuverDatabaseException
            *   UniqueManeuverInsertionException
            *   ManeuverDatabaseException
        """
        method = "ManeuverDatabase.add_unique_maneuver"
        
        # --- To assure uniqueness the member_service has to conduct a search. The maneuver should be validated first. ---#
        
        # Handle the case that, the maneuveris not safe.
        validation = self.microservice.execute.execute(candidate=maneuver)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueManeuverDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueManeuverDataServiceException.ERR_CODE}",
                    ex=UniqueManeuverInsertionException(
                        msg=f"{method}: {UniqueManeuverInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the maneuver is already in the collider_candidates before adding it. ---#
        search_result = self.search_maneuvers(context=ManeuverContext(id=maneuver.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueManeuverDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueManeuverDataServiceException.ERR_CODE}",
                    ex=UniqueManeuverInsertionException(
                        msg=f"{method}: {UniqueManeuverInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the maneuver is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueManeuverDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueManeuverDataServiceException.ERR_CODE}",
                    ex=UniqueManeuverInsertionException(
                        msg=f"{method}: {UniqueManeuverInsertionException.ERR_CODE}",
                        ex=AddingDuplicateManeuverException(f"{method}: {AddingDuplicateManeuverException.MSG}")
                    )
                )
            )
        # --- Use _maneuver_database_core.insert_maneuver because order does not matter for the maneuver access. ---#
        insertion_result = self._maneuver_database_core.insert_maneuver(maneuver=maneuver)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueManeuverDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueManeuverDataServiceException.ERR_CODE}",
                    ex=UniqueManeuverInsertionException(
                        msg=f"{method}: {UniqueManeuverInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_maneuvers(self, context: ManeuverContext) -> SearchResult[List[Maneuver]]:
        """
        # ACTION:
            1.  Get the result of calling _maneuver_database_core.delete_maneuver_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Maneuver] containing either:
                    - On failure: An exception.
                    - On success: Maneuver in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   ManeuverDatabaseException
            *   ExhaustiveManeuverDeletionException
        """
        method = "ManeuverDatabase.search_maneuvers"
        
        # --- Handoff the search responsibility to _maneuver_database_core. ---#
        search_result = self._maneuver_database_core.maneuver_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueManeuverDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueManeuverDataServiceException.ERR_CODE}",
                    ex=UniqueManeuverSearchException(
                        msg=f"{method}: {UniqueManeuverSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
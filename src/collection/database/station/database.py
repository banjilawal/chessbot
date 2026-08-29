# src/collection/database/station/database.py

"""
Module: database.station.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class StationDatabase(Database[Station]):
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
    1.  Ensure all bag in managed by StationStackService are unique.
    2.  Guarantee consistency of records in StationStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "StationDatabase"
    _station_database_core: StationStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: StationStackService = StationStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (StationStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._station_stack_service = data_service
    
    @property
    def microservice(self) -> StationService:
        return self._station_database_core.station_service
    
    @property
    def context_service(self) -> StationQueryService:
        return self._station_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._station_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._station_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_station(self, station: Station) -> InsertionResult[Station]:
        """
        # ACTION:
            1.  If the station fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the station either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _station_database_core.insert_station fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   station (Station)
        # RETURN:
            *   InsertionResult[Station] containing either:
                    - On failure: An exception.
                    - On success: Station in payload.
        Raises:
            *   StationDatabaseException
            *   UniqueStationInsertionException
            *   StationDatabaseException
        """
        method = "StationDatabase.add_unique_station"
        
        # --- To assure uniqueness the member_service has to conduct a search. The station should be validated first. ---#
        
        # Handle the case that, the stationis not safe.
        validation = self.microservice.execute.execute(candidate=station)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueStationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueStationDataServiceException.ERR_CODE}",
                    ex=UniqueStationInsertionException(
                        msg=f"{method}: {UniqueStationInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the station is already in the collider_candidates before adding it. ---#
        search_result = self.search_stations(context=StationContext(id=station.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueStationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueStationDataServiceException.ERR_CODE}",
                    ex=UniqueStationInsertionException(
                        msg=f"{method}: {UniqueStationInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the station is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueStationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueStationDataServiceException.ERR_CODE}",
                    ex=UniqueStationInsertionException(
                        msg=f"{method}: {UniqueStationInsertionException.ERR_CODE}",
                        ex=AddingDuplicateStationException(f"{method}: {AddingDuplicateStationException.MSG}")
                    )
                )
            )
        # --- Use _station_database_core.insert_station because order does not matter for the station access. ---#
        insertion_result = self._station_database_core.insert_station(station=station)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueStationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueStationDataServiceException.ERR_CODE}",
                    ex=UniqueStationInsertionException(
                        msg=f"{method}: {UniqueStationInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_stations(self, context: StationContext) -> SearchResult[List[Station]]:
        """
        # ACTION:
            1.  Get the result of calling _station_database_core.delete_station_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Station] containing either:
                    - On failure: An exception.
                    - On success: Station in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   StationDatabaseException
            *   ExhaustiveStationDeletionException
        """
        method = "StationDatabase.search_stations"
        
        # --- Handoff the search responsibility to _station_database_core. ---#
        search_result = self._station_database_core.station_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueStationDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueStationDataServiceException.ERR_CODE}",
                    ex=UniqueStationSearchException(
                        msg=f"{method}: {UniqueStationSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
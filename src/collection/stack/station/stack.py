# src/stack/station/station.py

"""
Module: stack.station.station
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class StationStackService(StackService[Station]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Station objects and their lifecycles.
    3.  Ensure integrity of Station data schema
    4.  Stack data structure for Station objects with no guarantee of uniqueness.

    Super Class:
        *   StackService[Station]

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "StationStackService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Station] = List[Station],
            service: StationService = StationService(),
            context_service: StationQueryService = StationQueryService(),
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
        method = "StationService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def station_service(self) -> StationService:
        return cast(StationService, self.entity_service)
    
    @property
    def station_context_service(self) -> StationQueryService:
        return cast(StationQueryService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_station(self, station: Station) -> InsertionResult[Station]:
        """
        # ACTION:
            1.  If the station is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   station (Station)
        # RETURNS:
            *   InsertionResult[Station] containing either:
                    - On failure: Exception.
                    - On success: Station in the payload.
        Raises:
            *   StationDataServiceException
        """
        method = "StationStackService.add_station"
        
        # Handle the case that, the station is unsafe.
        validation = self.station_service.execute.execute(candidate=station)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationInsertionException(
                        msg=f"{method}: {StationInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if an item in the list shares the station's arena. ---#
        search_result = self.station_context_service.finder.find(
            dataset=self.items,
            context=StationContext(arena=station.arena)
        )
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationInsertionException(
                        msg=f"{method}: {StationInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, a station in collection has the same arena.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationInsertionException(
                        msg=f"{method}: {StationInsertionException.ERR_CODE}",
                        ex=ArenaAlreadyContainsStationException(
                            f"{method}: {ArenaAlreadyContainsStationException.MSG}"
                        )
                    )
                )
            )
        # --- Station order is not required. Direct insertion into the collider_candidates is simpler that a push. ---#
        self.items.append(station)
        
        # Handle the case that, the station was not appended to the collider_candidates.
        if station not in self.items:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationInsertionException(
                        msg=f"{method}: {StationInsertionException.ERR_CODE}",
                        ex=AppendingStationDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingStationDirectlyIntoItemsFailedException.ERR_CODE}"
                        )
                    )
                )
            )
        # On success return the station in the InsertionResult
        return InsertionResult.success(payload=station)
    
    @LoggingLevelRouter.monitor
    def delete_station_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Station]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_stations_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_stations_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Station] containing either:
                    - On failure: Exception.
                    - On success: Station in the payload.
        Raises:
            *   StationDataServiceException
        """
        method = "StationStackService.delete_station_by_id"
        
        # Handle the case that, there are no bag in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationDeletionException(
                        msg=f"{method}: {StationDeletionException.ERR_CODE}",
                        ex=PoppingEmptyStationStackException(
                            f"{method}: {PoppingEmptyStationStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                StationDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                    ex=StationDeletionException(
                        msg=f"{method}: {StationDeletionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for a station with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Station):
                    # Send the exception chain on failure.
                    return DeletionResult.failure(
                        StationDataServiceException(
                            msg=f"ServiceId:{self.id}, {method}: {StationDataServiceException.ERR_CODE}",
                            ex=StationDeletionException(
                                msg=f"{method}: {StationDeletionException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Station, got {type(item).__name__} "
                                    f"instead of a Station."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted station in the DeletionResult. ---#
                station = cast(Station, item)
                self.items.remove(station)
                return DeletionResult.success(payload=station)
        
        # If none of the bag had that id return an empty DeletionResult.
        return DeletionResult.empty()
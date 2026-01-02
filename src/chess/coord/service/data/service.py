# src/chess/coord/service/data/service.py

"""
Module: chess.coord.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import DataService, DeletionResult, InsertionResult, id_emitter
from chess.coord import (
    Coord, CoordDataServiceException, CoordService, CoordContextService,
    PoppingEmtpyCoordDataServiceException
)


class CoordDataService(DataService[Coord]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching Coord collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Coords are put in the collection.
    4.  Assure updates do not break the integrity individual items in the collection or
        the collection itself.
    5.  Provide Coord stack data structure with no guarantee of uniqueness.
    6.  Search utility.

    # PARENT:
        *   DataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "CoordDataService"
    
    def service(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Coord] = List[Coord],
            service: CoordService = CoordService(),
            context_service: CoordContextService = CoordContextService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   items (List[Coord]): = List[Coord]
            *   service (CoordService): = CoordService()
            *   context_service (CoordContextService): = CoordContextService()

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
    def coord_service(self) -> CoordService:
        """Get CoordService instance."""
        return cast(CoordService, self.entity_service)
    
    @property
    def coord_context_service(self) -> CoordContextService:
        """Get CoordContextService."""
        return cast(CoordContextService, self.context_service)
    
    def add_coord(self, coord: Coord) -> InsertionResult[Coord]:
        """
        # ACTION:
            1.  If the coord fails validation send the exception in the InsertionResult. Else, call the super class
                push_item method.
            2.  If the super class push failed encapsulate the super class exception and send in the InsertionResult.
                Else, forward the super().push_item() result to the caller.
        # PARAMETERS:
            *   coord (Coord)
        # RETURN:
            *   InsertionResult[Coord] containing either:
                - On failure: Exception
                - On success: Coord in the payload.
        # RAISES:
            *   CoordDataServiceException
        """
        method = "CoordDataService.add_coord"
        # Handle the case that coord validation fails.
        validation = self.coord_service.validator.validate(candidate=coord)
        if validation.is_failure:
            # Return the exception chain.
            return InsertionResult(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        # Handle the case that super class push fails.
        insertion_result = self.push_item(item=coord)
        if insertion_result.is_failure:
            return InsertionResult(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.DEFAULT_MESSAGE}",
                    ex=insertion_result.exception
                )
            )
        # Otherwise the insertion_result is a success which can be forwarded to the caller.
        return insertion_result
    
    def pop_coord(self) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the list is empty send the exception in the DeletionResult. Else, call the super class undo_push
            2.  If the super class undo_push failed encapsulate the super class exception and send in the
                DeletionResult, Else, forward the super().push_item() result to the caller.
        # PARAMETERS:
            None
        # RETURN:
            *   DeletionResult[Coord] containing either:
                - On failure: Exception
                - On success: Coord in the payload.
        # RAISES:
            *   CoordDataServiceException
            *   PoppingEmtpyCoordDataServiceException
        """
        method = "CoordDataService.pop_coord"
        # Handle the case that the list is empty
        if self.is_empty:
            # Return the exception chain.
            return DeletionResult(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {CoordDataServiceException.ERROR_CODE}",
                    ex=PoppingEmtpyCoordDataServiceException(f"{method}: {CoordDataServiceException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the super class undo_push fails.
        deletion_result = self.undo_item_push()
        if deletion_result.is_failure:
            # Return the exception chain.
            return DeletionResult(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        # Otherwise the deletion_result is a success which can be forwarded to the caller.
        return deletion_result
        
        
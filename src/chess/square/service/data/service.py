# src/chess/square/service/data/service_.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.system import (
    DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    SearchResult, id_emitter
)
from chess.square import (
    Square, SquareContext, SquareDataServiceException, SquareDoesNotExistForRemovalException,
    SquareService, SquareContextService, SquareDeletionFailedException, SquareInsertionFailedException
)

class SquareDataService(DataService[Square]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Square objects and their lifecycles.
    3.  Ensure integrity of Square data stack
    4.  Stack data structure for Square objects with no guarantee of uniqueness.

    # PARENT:
        *   DataService[Square]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "SquareDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            service: SquareService = SquareService(),
            context_service: SquareContextService = SquareContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "SquareService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def square_service(self) -> SquareService:
        return cast(SquareService, self.entity_service)
    
    @property
    def square_context_service(self) -> SquareContextService:
        return cast(SquareContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def add_square(self, square: Square) -> InsertionResult[Square]:
        """
        # ACTION:
            1.  If the square is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   square (Square)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareDataServiceException
        """
        method = "SquareDataService.add_square"
        
        # Handle the case that the square is unsafe.
        validation = self.square_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        
        push_result = self.push_item(item=square)
        # Handle the case that super().push_item fails
        if push_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=push_result.exception
                    )
                )
            )
        # On success cast the payload and return to the caller in an insertion result.
        return push_result
    
    @LoggingLevelRouter.monitor
    def delete_square_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[
        Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_squares_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_squares_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareDataServiceException
        """
        method = "SquareDataService.remove_square_by_id"
        
        # Handle the case of an unsafe id.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareDeletionFailedException(
                        message=f"{method}: {SquareDeletionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        for item in self.items:
            if item.id == id:
                square = cast(Square, item)
                self.items.remove(square)
                return DeletionResult.success(payload=square)
        return DeletionResult.nothing()
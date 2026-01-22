# src/chess/square/service/data/service_.py

"""
Module: chess.square.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import (
    NUMBER_OF_COLUMNS, DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, ROW_SIZE,
    id_emitter
)
from chess.square import (
    AppendingSquareDirectlyIntoItemsFailedException, PoppingEmptySquareStackException, Square, SquareContext,
    SquareDataServiceException, SquareDoesNotExistForRemovalException, SquareService, SquareContextService,
    SquareDeletionFailedException, SquareInsertionFailedException, SquareServiceCapacityException
)

class SquareDataService(DataService[Square]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

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
    _capacity: int
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            capacity: int = ROW_SIZE * NUMBER_OF_COLUMNS,
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
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return len(self.items) >= self.capacity
    
    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    @property
    def square_service(self) -> SquareService:
        return cast(SquareService, self.entity_service)
    
    @property
    def square_context_service(self) -> SquareContextService:
        return cast(SquareContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_square(self, square: Square) -> InsertionResult[Square]:
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
        
        # Handle the case that the list is full
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=SquareServiceCapacityException(
                            f"{method}: {SquareServiceCapacityException.DEFAULT_MESSAGE}")
                    )
                )
            )
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
        # --- Check if an item in the list shares the square's coord. ---#
        search_result = self.square_context_service.finder.find(
            dataset=self.items,
            context=SquareContext(coord=square.coord)
        )
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that a square in collection has the same coord.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=SquareDoesNotExistForRemovalException(
                            f"{method}: {SquareDoesNotExistForRemovalException.ERROR_CODE}"
                        )
                    )
                )
            )
        # --- Square order is not required. Direct insertion into the dataset is simpler that a push. ---#
        self.items.append(square)
        
        # Handle the case that the square was not appended to the dataset.
        if square not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=AppendingSquareDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingSquareDirectlyIntoItemsFailedException.ERROR_CODE}"
                        )
                    )
                )
            )
        # On success return the square in the InsertionResult
        return InsertionResult.success(payload=square)
    
    @LoggingLevelRouter.monitor
    def delete_square_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
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
        method = "SquareDataService.delete_square_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                    ex=SquareDeletionFailedException(
                        message=f"{method}: {SquareDeletionFailedException.ERROR_CODE}",
                        ex=PoppingEmptySquareStackException(
                            f"{method}: {PoppingEmptySquareStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the id is not certified safe.
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
        # --- Search the list for a square with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Square):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        SquareDataServiceException(
                            message=f"ServiceId:{self.id}, {method}: {SquareDataServiceException.ERROR_CODE}",
                            ex=SquareDeletionFailedException(
                                message=f"{method}: {SquareDeletionFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Square, got {type(item).__name__} "
                                    f"instead of a Square."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted square in the DeletionResult. ---#
                square = cast(Square, item)
                self.items.remove(square)
                return DeletionResult.success(payload=square)
            
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.empty()
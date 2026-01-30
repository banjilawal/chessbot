# src/chess/square/database/core/service_.py

"""
Module: chess.square.database.core.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import (
    NUMBER_OF_COLUMNS, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    NUMBER_OF_ROWS,
    SearchResult, id_emitter
)
from chess.square import (
    SquareNameAlreadyInUseException, SquareCoordAlreadyInUseException, SquareIdAlreadyInUseException,
    PoppingEmptySquareStackException, Square, SquareStackServiceException, SquareService, SquareContextService,
    PoppingSquareStackFailedException, SquareInsertionFailedException, FullSquareStackException
)


class SquareStackService(StackService[Square]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Square objects and their lifecycles.
    3.  Ensure integrity of Square data stack
    4.  Stack data structure for Square objects with no guarantee of uniqueness.

    # PARENT:
        *   StackService[Square]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "SquareStackService"
    _capacity: int
    _stack: List[Square]
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Square] = List[Square],
            service: SquareService = SquareService(),
            capacity: int = NUMBER_OF_ROWS * NUMBER_OF_COLUMNS,
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
        self._stack = items
        self._capacity = capacity
    
    def pop(self) -> DeletionResult[D]:
        pass
        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return self.size == self._capacity
    
    @property
    def remaining_slots(self) -> int:
        return self.capacity - self.size
    
    @property
    def square_service(self) -> SquareService:
        return cast(SquareService, self.entity_service)
    
    @property
    def square_context_service(self) -> SquareContextService:
        return cast(SquareContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def push_square(self, item: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Square)
        # RETURNS:
            *   InsertionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Square in the payload.
        # RAISES:
            *   SquareStackServiceException
        """
        method = "SquareStackService.add_square"
        
        # Handle the case that the list is full
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=FullSquareStackException(f"{method}: {FullSquareStackException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that the item is unsafe.
        validation = self.square_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if any of the item's attributes are already in use. ---#
        collision_detection = self._attribute_collision_detector(target=item)
        if collision_detection.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                    ex=SquareInsertionFailedException(
                        message=f"{method}: {SquareInsertionFailedException.ERROR_CODE}",
                        ex=collision_detection.exception
                    )
                )
            )
        # --- Square order is not required. Direct insertion into the stack is simpler that a push. ---#
        
        # On success return the item in the InsertionResult
        self.items.append(item)
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
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
            *   SquareStackServiceException
        """
        method = "SquareStackService.delete_square_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                    ex=PoppingSquareStackFailedException(
                        message=f"{method}: {PoppingSquareStackFailedException.ERROR_CODE}",
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
                SquareStackServiceException(
                    message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                    ex=PoppingSquareStackFailedException(
                        message=f"{method}: {PoppingSquareStackFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Square):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        SquareStackServiceException(
                            message=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERROR_CODE}",
                            ex=PoppingSquareStackFailedException(
                                message=f"{method}: {PoppingSquareStackFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Square, got {type(item).__name__} "
                                    f"instead of a Square."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted item in the DeletionResult. ---#
                square = cast(Square, item)
                self.items.remove(square)
                return DeletionResult.success(payload=square)
            
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.nothing_to_delete()
    
    
    def _attribute_collision_detector(self, target) -> SearchResult[Square]:
        method = "SquareStackService.attribute_collision_detector"
        
        for square in self._stack:
            if square.id == target.id:
                return SearchResult.failure(
                    SquareIdAlreadyInUseException(
                        f"{method}: {SquareIdAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            if square.coord == target.coord:
                return SearchResult.failure(
                    SquareCoordAlreadyInUseException(
                        f"{method}: {SquareCoordAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            if square.name.upper() == target.name.upper():
                return SearchResult.failure(
                    SquareNameAlreadyInUseException(
                        f"{method}: {SquareNameAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
        return SearchResult.empty()
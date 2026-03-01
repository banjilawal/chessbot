# src/logic/square/database/core/stack.py

"""
Module: logic.square.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional

from logic.system import (
    IdFactory, NUMBER_OF_COLUMNS, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    NUMBER_OF_ROWS, SearchResult
)
from logic.square import (
    SquareContext, SquareStackPopException, SquareStackPushException, SquareStackUtil, SquareService,
    SquareContextService,PoppingEmptySquareStackException, Square,  SquareStackServiceException,
)

class SquareStackService(StackService[Square]):
    """
    # ROLE: Data Structure, Services:(Integrity, Build, Validation, Search) Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice for managing Square objects and their lifecycles.
    2.  Guarantee all Square instances in stack are unique.

    # PARENT:
        *   StackService

    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   capacity (int)
        *   stack (List[Square])
        *   util (SquareStackUtil)
        *   service (SquareService)
        *   context_service (SquareContextService)
    
    # INHERITED ATTRIBUTES:
        *   See StackService for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   id (int)
            *   name (str)
            *   capacity (int)
            *   util (SquareStackUtil)
            *   service (SquareService)
            *   context_service (SquareContextService)

        Inherited:
        None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
        
    # LOCAL METHODS:

        *   pop() -> DeletionResult[Square]
        *   push(item: Square) -> InsertionResult[bool]
        *   query(context: SquareContext) -> SearchResult[List[Square]]
        *   delete_by_id(id: int, identity_service: IdentityService) -> DeletionResult[Square]

    # INHERITED METHODS:
        *   See StackService class for inherited methods.
    """
    SERVICE_NAME = "SquareStackService"
    _capacity: int
    _stack: List[Square]
    _util: SquareStackUtil
    _service: SquareService
    _context_service: SquareContextService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: SquareService = SquareService(),
            util: SquareStackUtil = SquareStackUtil(),
            capacity: int = NUMBER_OF_ROWS * NUMBER_OF_COLUMNS,
            id: int = IdFactory.next_id(class_name="SquareStackService"),
            context_service: SquareContextService = SquareContextService(),
    ):
        method = "SquareService.__init__"
        super().__init__(id=id,name=name,)
        self._util = util
        self._service = service
        self._context_service = context_service
        
        self._stack = []
        self._capacity = capacity
    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return self.size == self._capacity
    
    @property
    def util(self) -> SquareStackUtil:
        return self._util
    
    @property
    def current_item(self) -> Optional[Square]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> SquareService:
        return self._service
    
    @property
    def context_service(self) -> SquareContextService:
        return self._context_service
    
    @LoggingLevelRouter.monitor
    def push(self, item: Square) -> InsertionResult[bool]:
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
        
        # Handle the case that, there is no capacity for adding another square.
        available_capacity_computation_result = self._util.stats_analyzer.available_capacity(stack=self)
        if available_capacity_computation_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=SquareStackPushException(
                        msg=f"{method}: {SquareStackPushException.ERR_CODE}",
                        ex=available_capacity_computation_result.exception
                    )
                )
            )
        # Handle the case that, the square is not safe, or its id, name, or coord are in use.
        collision_report = self.integrity_service.collision_detector.detect(
            target=item,
            dataset=self._stack,
        )
        if collision_report.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=SquareStackPushException(
                        msg=f"{method}: {SquareStackPushException.ERR_CODE}",
                        ex=collision_report.exception
                    )
                )
            )
        # --- Append the square and send the successful InsertionResult. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                square at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Square] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   SquareStackServiceException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStackService.pop"
        
        # Handle the case that, there are no tokens in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=SquareStackPopException(
                        msg=f"{method}: {SquareStackPopException.ERR_CODE}",
                        ex=PoppingEmptySquareStackException(
                            f"{method}: {PoppingEmptySquareStackException.MSG}"
                        )
                    )
                )
            )
        # --- Pop the non-empty token stack. ---#
        square = self._stack.pop(-1)
        # --- Send the success result to the caller. ---#
        DeletionResult.success(square)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        """
        # ACTION:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a square before it's deleted.
            3.  Iterate through the squares.
                    *   If a square's id matches the target record the square in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Square]
        # RAISES:
            *   SquareStackServiceException
            *   SquareStackPopException
            *   PoppingEmptySquareStackException
        """
        method = "SquareStackService.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=SquareStackPopException(
                        msg=f"{method}: {SquareStackPopException.ERR_CODE}",
                        ex=PoppingEmptySquareStackException(
                            f"{method}: {PoppingEmptySquareStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=SquareStackPopException(
                        msg=f"{method}: {SquareStackPopException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for square in self._stack:
            if square.id == id:
                # Record a hit before pulling it from the stack.
                target = square
                self._stack.remove(square)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # At least one edge was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no edges were removed.
        return DeletionResult.nothing_to_delete()
      
    @LoggingLevelRouter.monitor
    def query(self, context: SquareContext) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a SquareStackServiceException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (SquareContext)
        # RETURN:
            *   SearchResult[List[Square] containing either:
                    - On failure: An exception.
                    - On success: List[Square] in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   SquareStackServiceException
        """
        method = "SquareStackService.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareStackServiceException(
                    msg=f"ServiceID:{self.id} {method}: {SquareStackServiceException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
# src/chess/edge/stack/stack.py

"""
Module: chess.edge.stack.stack
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.edge import (
    AddingDuplicateEdgeException, Edge, EdgeContextService, EdgePopException, EdgePushException, EdgeService,
    EdgeStackException, PoppingEmptyEdgeStackException
)
from chess.system import DeletionResult, IdFactory, InsertionResult, LoggingLevelRouter, StackService


class EdgeStack(StackService[Edge]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Ensure integrity of Edge stack.
    3.  Ensure uniqueness of edges in the stack.
    4.  Interface for CRUD operations on Edge collections.
    5.  Microservice for managing integrity of Edge objects throughout their lifecycles

    # PARENT:
        *   StackService[Edge]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "EdgeStackService"
    
    _id: int
    _stack: List[Edge]
    _service: EdgeService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            items: List[Edge] = List[Edge],
            service: EdgeService = EdgeService(),
            id: int = IdFactory.next_id(class_name="EdgeStack"),
            context_service: EdgeContextService = EdgeContextService(),
    ):
        super().__init__(
            id=id,
            name=name,
            items=[],
            entity_service=service,
            context_service=context_service,
        )
        self._stack = items
        self._service = service
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def integrity_service(self) -> EdgeService:
        return self._service
    
    @property
    def context_service(self) -> EdgeContextService:
        return cast(EdgeContextService, self.context_service)
    
    @property
    def current_edge(self) -> Optional[Edge]:
        return self._stack[-1] if self._stack else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If the item is not validated or, it already exists in the stack send an exception chain in the
                InsertionResult. Else, append the edge to the stack and send the success result.
        # PARAMETERS:
            *   item (Edge)
        # RETURNS:
            *   InsertionResult[Edge] containing either:
                    - On failure: Exception.
                    - On success: Edge in the payload.
        # RAISES:
            *   EdgeStackException
            *   EdgePushException
            *   AddingDuplicateEdgeException
        """
        method = "EdgeStack.push"
        
        # Handle the case that the item is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                EdgeStackException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERROR_CODE}",
                    ex=EdgePushException(
                        message=f"{method}: {EdgePushException.ERROR_CODE}", 
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the edge is already in the list.
        if item in self._stack:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                EdgeStackException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERROR_CODE}",
                    ex=EdgePushException(
                        message=f"{method}: {EdgePushException.ERROR_CODE}",
                        ex=AddingDuplicateEdgeException(f"{method}: {AddingDuplicateEdgeException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Append the edge and send the successful InsertionResult. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Edge]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                edge at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Edge] containing either:
                    - On failure: Exception.
                    - On success: Edge in the payload.
        # RAISES:
            *   EdgeStackException
            *   EdgePopException 
            *   PoppingEmptyEdgeStackException
        """
        method = "EdgeStack.pop"
        
        # Handle the case that there are no edges in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                EdgeStackException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERROR_CODE}",
                    ex=EdgePopException(
                        message=f"{method}: {EdgePopException.ERROR_CODE}",
                        ex=PoppingEmptyEdgeStackException(
                            f"{method}: {PoppingEmptyEdgeStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Pop the current edge of the non-empty stack and return in the DeletionResult. ---#
        edge = self._stack.pop(-1)
        DeletionResult.success(edge)
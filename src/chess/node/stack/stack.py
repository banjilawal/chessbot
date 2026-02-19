# src/chess/node/stack/stack.py

"""
Module: chess.node.stack.stack
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.node import (
    AddingDuplicateNodeException, Node, NodeContextService, NodePopException, NodePushException, NodeService,
    NodeStackException, PoppingEmptyNodeStackException
)
from chess.system import DeletionResult, IdFactory, InsertionResult, LoggingLevelRouter, StackService


class NodeStack(StackService[Node]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Ensure integrity of Node stack.
    3.  Ensure uniqueness of nodes in the stack.
    4.  Interface for CRUD operations on Node collections.
    5.  Microservice for managing integrity of Node objects throughout their lifecycles

    # PARENT:
        *   StackService[Node]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "NodeStackService"
    
    _id: int
    _stack: List[Node]
    _service: NodeService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            items: List[Node] = List[Node],
            service: NodeService = NodeService(),
            id: int = IdFactory.next_id(class_name="NodeStack"),
            context_service: NodeContextService = NodeContextService(),
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
    def integrity_service(self) -> NodeService:
        return self._service
    
    @property
    def context_service(self) -> NodeContextService:
        return cast(NodeContextService, self.context_service)
    
    @property
    def current_node(self) -> Optional[Node]:
        return self._stack[-1] if self._stack else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Node) -> InsertionResult:
        """
        # ACTION:
            1.  If the item is not validated or, it already exists in the stack send an exception chain in the
                InsertionResult. Else, append the node to the stack and send the success result.
        # PARAMETERS:
            *   item (Node)
        # RETURNS:
            *   InsertionResult[Node] containing either:
                    - On failure: Exception.
                    - On success: Node in the payload.
        # RAISES:
            *   NodeStackException
            *   NodePushException
            *   AddingDuplicateNodeException
        """
        method = "NodeStack.push"
        
        # Handle the case that the item is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeStackException(
                    message=f"ServiceId:{self.id}, {method}: {NodeStackException.ERROR_CODE}",
                    ex=NodePushException(
                        message=f"{method}: {NodePushException.ERROR_CODE}", 
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the node is already in the list.
        if item in self._stack:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeStackException(
                    message=f"ServiceId:{self.id}, {method}: {NodeStackException.ERROR_CODE}",
                    ex=NodePushException(
                        message=f"{method}: {NodePushException.ERROR_CODE}",
                        ex=AddingDuplicateNodeException(f"{method}: {AddingDuplicateNodeException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Append the node and send the successful InsertionResult. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Node]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                node at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Node] containing either:
                    - On failure: Exception.
                    - On success: Node in the payload.
        # RAISES:
            *   NodeStackException
            *   NodePopException 
            *   PoppingEmptyNodeStackException
        """
        method = "NodeStack.pop"
        
        # Handle the case that there are no nodes in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                NodeStackException(
                    message=f"ServiceId:{self.id}, {method}: {NodeStackException.ERROR_CODE}",
                    ex=NodePopException(
                        message=f"{method}: {NodePopException.ERROR_CODE}",
                        ex=PoppingEmptyNodeStackException(
                            f"{method}: {PoppingEmptyNodeStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Pop the current node of the non-empty stack and return in the DeletionResult. ---#
        node = self._stack.pop(-1)
        DeletionResult.success(node)
# src/stack/edge/py

"""
Module: stack.edge.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



class EdgeStackService(StackService[Edge]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Ensure integrity of Edge schema.
    3.  Ensure uniqueness of edges in the schema.
    4.  Interface for CRUD controller on Edge collections.
    5.  Microservice for managing integrity of Edge objects throughout their lifecycles

    Super Class:
        *   StackService[Edge]

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    
    @property
    def items(self) -> List[Edge]:
        pass
    
    def delete_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[T]:
        pass
    
    SERVICE_NAME = "EdgeStack"
    
    _stack: List[Edge]
    _service: EdgeService
    _context_service: EdgeQueryService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: EdgeService = EdgeService(),
            id: int = IdFactory.next_id(class_name="EdgeStack"),
            context_service: EdgeQueryService = EdgeQueryService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   service (EdgeService)
            *   context_service (EdgeQueryService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name,)
        self._stack = []
        self._service = service
        self._context_service = context_service
    
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
    def context_service(self) -> EdgeQueryService:
        return self._context_service
    
    @property
    def current_item(self) -> Optional[Edge]:
        return self._stack[-1] if self._stack else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Edge) -> InsertionResult:
        """
        # ACTION:
            1.  If the item is not validated or, it already exists in the schema send an exception chain in the
                InsertionResult. Else, append the edge to the schema and send the success result.
        # PARAMETERS:
            *   item (Edge)
        # RETURNS:
            *   InsertionResult[bool] containing either:
                    - On failure: Exception and bool(False).
                    - On success: bool(True) only
        Raises:
            *   EdgeStackException
            *   PushingEdgeException
            *   AddingDuplicateEdgeException
        """
        method = "EdgeStack.push"
        
        # Handle the case that, the item is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                EdgeStackException(
                    msg=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERR_CODE}",
                    ex=PushingEdgeException(
                        msg=f"{method}: {PushingEdgeException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the edge is already in the list.
        if item in self._stack:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                EdgeStackException(
                    msg=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERR_CODE}",
                    ex=PushingEdgeException(
                        msg=f"{method}: {PushingEdgeException.ERR_CODE}",
                        ex=AddingDuplicateEdgeException(f"{method}: {AddingDuplicateEdgeException.MSG}")
                    )
                )
            )
        # --- Append the edge and send the success result. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Edge]:
        """
        # ACTION:
            1.  If the schema is empty send an exception in the DeletionResult. Else remove the
                edge at the top of the schema and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Edge] containing either:
                    - On failure: Exception.
                    - On success: Edge.
        Raises:
            *   EdgeStackException
            *   PoppingEdgeException
            *   PoppingEmptyEdgeStackException
        """
        method = "EdgeStack.pop"
        
        # Handle the case that, there are no edges in the schema.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                EdgeStackException(
                    msg=f"ServiceId:{self.id}, {method}: {EdgeStackException.ERR_CODE}",
                    ex=PoppingEdgeException(
                        msg=f"{method}: {PoppingEdgeException.ERR_CODE}",
                        ex=PoppingEmptyEdgeStackException(
                            f"{method}: {PoppingEmptyEdgeStackException.MSG}"
                        )
                    )
                )
            )
        # --- Remove the top edge in the schema and return in the DeletionResult. ---#
        edge = self._stack.pop(-1)
        DeletionResult.success(edge)
    
    @LoggingLevelRouter.monitor
    def delete_by_label(
            self,
            label: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Edge]:
        """
        # ACTION:
            1.  If the labelis not safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a edge before it's deleted.
            3.  Iterate through the edges.
                    *   If a edge's id matches the target record the edge in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   label (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Edge]
        Raises:
            *   EdgeStackException
            *   PoppingEdgeException
            *   PoppingEmptyEdgeStackException
        """
        method = "EdgeStack.delete_by_label"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                EdgeStackException(
                    msg=f"StackId:{self.id}, {method}: {EdgeStackException.ERR_CODE}",
                    ex=PoppingEdgeException(
                        msg=f"{method}: {PoppingEdgeException.ERR_CODE}",
                        ex=PoppingEmptyEdgeStackException(
                            f"{method}: {PoppingEmptyEdgeStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the labelis not safe.
        validation = identity_service.validate_id(candidate=label)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                EdgeStackException(
                    msg=f"StackId:{self.id}, {method}: {EdgeStackException.ERR_CODE}",
                    ex=PoppingEdgeException(
                        msg=f"{method}: {PoppingEdgeException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for edge in self._stack:
            if edge.label == label:
                # Record a hit before pulling it from the schema.
                target = edge
                self._stack.remove(edge)
        # --- After the purging loop finished handle the possible return cases. ---#
        
        # At least one edge was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no edges were removed.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def search(self, context: EdgeContext) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in search lifecycle.
            2.  Any failures context_service will be encapsulated inside a EdgeStackException  which is sent inside a
                SearchResult.
            3.  If the search completes successfully return the result directly because its a SearchResult instance.
        # PARAMETERS:
            *   context (EdgeContext)
        # RETURN:
            *   SearchResult[List[Edge]] containing either:
                    - On failure: An exception.
                    - On success: List[Edge].
                    - On Empty: payload null, exception null.
        Raises:
            *   EdgeStackException
        """
        method = "EdgeStack.context"
        
        # --- Handoff the search responsibility to _context_service. ---#
        query_result = self._context_service.finder.route(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                EdgeStackException(
                    msg=f"ServiceID:{self.id} {method}: {EdgeStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
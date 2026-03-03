# src/command/pipeline/database/core/stack.py

"""
Module: command.pipeline.database.core.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from logic.system import (
    DeletionResult, IdFactory, IdentityService, InsertionResult, LoggingLevelRouter, NUMBER_OF_COLUMNS, NUMBER_OF_ROWS,
    SearchResult, StackService,
    id_emitter
)
from logic.pipeline import (
    AddingDuplicatePipelineException, PoppingEmptyPipelineStackException, PoppingPipelineStackFailedException,
    PushingPipelineFailedException, Pipeline, PipelineContext, PipelineContextService, PipelineService, PipelineStackException
)


class PipelineStack(StackService[Pipeline]):
    """
    # ROLE: Data Stack, Search AbstractService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing pipeline objects and their lifecycles.
    3.  Ensure integrity of pipeline data stack
    4.  Stack data structure for Pipeline objects with no guarantee of uniqueness.
    
    # PARENT:
        *   StackService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "PipelineStack"
    
    _pipelines: List[Pipeline]
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: PipelineService = PipelineService(),
            id: int = IdFactory.next_id(class_name="PipelineStack"),
            context_service: PipelineContextService = PipelineContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   service (PipelineService)
            *   context_service (PipelineContextService)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "TokenStack.__init__"
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
    def integrity_service(self) -> PipelineService:
        return self._service
    
    @property
    def context_service(self) -> PipelineContextService:
        return self.context_service
    
    @property
    def current_item(self) -> Pipeline:
        return self._stack[-1] if self.is_empty else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Pipeline) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Pipeline)
        # RETURNS:
            *   InsertionResult[Pipeline] containing either:
                    - On failure: Exception.
                    - On success: Pipeline in the payload.
        Raises:
            *   PipelineStackException
        """
        method = "PipelineStack.push"
        
        # Handle the case that, the pipeline is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PipelineStackException(
                    msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                    ex=PushingPipelineFailedException(
                        msg=f"{method}: {PushingPipelineFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the pipeline is already present in the stack.
        if item in self._stack:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                PipelineStackException(
                    msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                    ex=PushingPipelineFailedException(
                        msg=f"{method}: {PushingPipelineFailedException.ERR_CODE}",
                        ex=AddingDuplicatePipelineException(
                            f"{method}: {AddingDuplicatePipelineException.MSG}"
                        )
                    )
                )
            )
        # --- Pipeline order is not required. Direct insertion into the stack is simpler that a push. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Pipeline]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_Pipelines_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Pipelines_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Pipeline] containing either:
                    - On failure: Exception.
                    - On success: Pipeline in the payload.
        Raises:
            *   PipelineStackException
        """
        method = "PipelineStack.pop"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PipelineStackException(
                    msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                    ex=PoppingPipelineStackFailedException(
                        msg=f"{method}: {PoppingPipelineStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyPipelineStackException(
                            f"{method}: {PoppingEmptyPipelineStackException.MSG}"
                        )
                    )
                )
            )
        pipeline = self._stack.pop(-1)
        return DeletionResult.success(pipeline)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Pipeline]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_Pipelines_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Pipelines_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Pipeline] containing either:
                    - On failure: Exception.
                    - On success: Pipeline in the payload.
        Raises:
            *   PipelineStackException
        """
        method = "PipelineStack.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PipelineStackException(
                    msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                    ex=PoppingPipelineStackFailedException(
                        msg=f"{method}: {PoppingPipelineStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyPipelineStackException(
                            f"{method}: {PoppingEmptyPipelineStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                PipelineStackException(
                    msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                    ex=PoppingPipelineStackFailedException(
                        msg=f"{method}: {PoppingPipelineStackFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        for item in self._stack:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Pipeline):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        PipelineStackException(
                            msg=f"StackId:{self.id}, {method}: {PipelineStackException.ERR_CODE}",
                            ex=PoppingPipelineStackFailedException(
                                msg=f"{method}: {PoppingPipelineStackFailedException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Pipeline, got {type(item).__name__} "
                                    f"instead of a Pipeline."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted item in the DeletionResult. ---#
                pipeline = cast(Pipeline, item)
                self._stack.remove(pipeline)
                return DeletionResult.success(payload=pipeline)
        
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def query(self, context: PipelineContext) -> SearchResult[List[Pipeline]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a PipelineStackException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (PipelineContext)
        # RETURN:
            *   SearchResult[List[Pipeline] containing either:
                    - On failure: An exception.
                    - On success: List[Pipeline] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   PipelineStackException
        """
        method = "PipelineStack.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                PipelineStackException(
                    msg=f"ServiceID:{self.id} {method}: {PipelineStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    
    @LoggingLevelRouter.monitor
    def query(self, context: PipelineContext) -> SearchResult[List[Pipeline]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a PipelineStackException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (PipelineContext)
        # RETURN:
            *   SearchResult[List[Pipeline] containing either:
                    - On failure: An exception.
                    - On success: List[Pipeline] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   PipelineStackException
        """
        method = "PipelineStack.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                PipelineStackException(
                    msg=f"ServiceID:{self.id} {method}: {PipelineStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    

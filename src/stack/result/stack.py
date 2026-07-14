# src/stack/result/stack.py

"""
Module: stack.result.stack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from microservice import ResultService
from model import Result
from stack import StackService


class ResultStackService(StackService[Result]):
    """
    Role:Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing result objects and their lifecycles.
    3.  Ensure integrity of result data schema
    4.  Stack data structure for Result objects with no guarantee of uniqueness.
    
    Super Class:
        *   StackService

    Provides:

    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "ResultStack"
    
    _stack: List[Result]
    _microservice: ResultService
    _context_service: ResultQueryService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            microservice: ResultService = ResultService(),
            id: int = IdFactory.next_id(class_name="ResultStack"),
            context_microservice: ResultQueryService = ResultQueryService(),
    ):
        """
        Args:
            id: int
            name: str
            microservice: ResultService
        """
        method = "TokenStackService.__init__"
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
    def integrity_service(self) -> Resultmicroservice:
        return self._service
    
    @property
    def context_service(self) -> ResultQuerymicroservice:
        return self.context_service
    
    @property
    def current_item(self) -> Result:
        return self._stack[-1] if self.is_empty else None
    
    @LoggingLevelRouter.monitor
    def push(self, item: Result) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   item (Result)
        # RETURNS:
            *   InsertionResult[Result] containing either:
                    - On failure: Exception.
                    - On success: Result in the payload.
        Raises:
            *   ResultStackException
        """
        method = "ResultStack.push"
        
        # Handle the case that, the result is unsafe.
        validation = self.integrity_service.run.execute(candidate=item)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ResultStackException(
                    msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                    ex=PushingResultFailedException(
                        msg=f"{method}: {PushingResultFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the result is already present in the schema.
        if item in self._stack:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ResultStackException(
                    msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                    ex=PushingResultFailedException(
                        msg=f"{method}: {PushingResultFailedException.ERR_CODE}",
                        ex=AddingDuplicateResultException(
                            f"{method}: {AddingDuplicateResultException.MSG}"
                        )
                    )
                )
            )
        # --- Result order is not required. Direct insertion into the schema is simpler that a push. ---#
        self._stack.append(item)
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Result]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_Results_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Results_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Result] containing either:
                    - On failure: Exception.
                    - On success: Result in the payload.
        Raises:
            *   ResultStackException
        """
        method = "ResultStack.pop"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ResultStackException(
                    msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                    ex=PoppingResultStackFailedException(
                        msg=f"{method}: {PoppingResultStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyResultStackException(
                            f"{method}: {PoppingEmptyResultStackException.MSG}"
                        )
                    )
                )
            )
        result = self._stack.pop(-1)
        return DeletionResult.success(result)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_microservice: IdentityService = IdentityService()
    ) -> DeletionResult[Result]:
        """
        # ACTION:
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_Results_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_Results_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Result] containing either:
                    - On failure: Exception.
                    - On success: Result in the payload.
        Raises:
            *   ResultStackException
        """
        method = "ResultStack.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ResultStackException(
                    msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                    ex=PoppingResultStackFailedException(
                        msg=f"{method}: {PoppingResultStackFailedException.ERR_CODE}",
                        ex=PoppingEmptyResultStackException(
                            f"{method}: {PoppingEmptyResultStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ResultStackException(
                    msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                    ex=PoppingResultStackFailedException(
                        msg=f"{method}: {PoppingResultStackFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for an item with target id. ---#
        for item in self._stack:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Result):
                    # Send the exception chain on failure.
                    return DeletionResult.failure(
                        ResultStackException(
                            msg=f"StackId:{self.id}, {method}: {ResultStackException.ERR_CODE}",
                            ex=PoppingResultStackFailedException(
                                msg=f"{method}: {PoppingResultStackFailedException.ERR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Result, got {type(item).__name__} "
                                    f"instead of a Result."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted item in the DeletionResult. ---#
                result = cast(Result, item)
                self._stack.remove(result)
                return DeletionResult.success(payload=result)
        
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def search(self, context: ResultContext) -> SearchResult[List[Result]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a ResultStackException 
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (ResultContext)
        # RETURN:
            *   SearchResult[List[Result] containing either:
                    - On failure: An exception.
                    - On success: List[Result] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   ResultStackException
        """
        method = "ResultStack.context"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                ResultStackException(
                    msg=f"ServiceID:{self.id} {method}: {ResultStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    
    @LoggingLevelRouter.monitor
    def query(self, context: ResultContext) -> SearchResult[List[Result]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a ResultStackException 
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (ResultContext)
        # RETURN:
            *   SearchResult[List[Result] containing either:
                    - On failure: An exception.
                    - On success: List[Result] in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   ResultStackException
        """
        method = "ResultStack.context"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                ResultStackException(
                    msg=f"ServiceID:{self.id} {method}: {ResultStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
    

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
    NUMBER_OF_ROWS, SearchResult, UpdateResult
)
from logic.square import (
    SquareContext, SquareStackCrudHandler, SquareStackUtil, SquareService,
    SquareContextService, Square,
)
from logic.token import Token


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

    Attributes:
            SERVICE_NAME: str
            capacity: int
            stack: List[Square]
            util: SquareStackHandler
            service: SquareService:
            context_service: SquareContextService
    
    # INHERITED ATTRIBUTES:
        *   See StackService for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   id (int)
            *   name (str)
            *   capacity (int)
            *   util (SquareStackHandler)
            *   service (SquareService)
            *   context_service (SquareContextService)

        Inherited:
        None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
        
    Methods:
    - pop(): Return DeletionResult[Square]
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
    def items(self) -> List[Square]:
        return self._stack
    
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
        return self.util.crud.push(self, item)
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Square]:
        return self.util.crud.pop(self)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        return self.util.crud.delete_by_id(stack=self, id=id, identity_service=identity_service)
      
    @LoggingLevelRouter.monitor
    def query(self, context: SquareContext) -> SearchResult[List[Square]]:
        return self._util.crud.query(context=context, stack=self)
    
    def vist_square(self, square: Square, token: Token) -> UpdateResult[Square]:
        return self.util.occupation_service.occupy_stack_square(
            square=square,
            token=token,
            square_list=self._stack
        )
    
    def leave_square(self, token: Token) ->DeletionResult[Token]:
        return self._util.occupation_service.remove_occupant_from_stack(
            occupant=token,
            square_list=self._stack
        )
    
    @LoggingLevelRouter.monitor
    def query(
            self,
            context: SquareContext,
            square_stack: SquareStackService
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a SquareCrudHandlerException
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
        Raises:
            *   SquareCrudHandlerException
        """
        method = "SquareStackService.query"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = square_stack.context_service.finder.find(
            context=context,
            dataset=square_stack.items,
        )
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackServiceException.ERR_CODE,
                    msg=SquareStackServiceException.MSG,
                    ex=query_result.exception,
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
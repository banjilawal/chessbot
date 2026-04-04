# src/logic/square/database/kernel/schema.py

"""
Module: logic.square.database.kernel.schema
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
    SquareContext, SquareStackException, SquareStackOpsController, SquareService,
    SquareQueryService, Square, SquareStackOpsController,
)
from model.token import Token, TokenService


class SquareStackService(StackService[Square]):
    """
    Role:Data Structure, Services:(Integrity, Build, Validation, Search) Encapsulation, API layer.

    Responsibilities:
    1.  Microservice for managing Square objects and their lifecycles.
    2.  Guarantee all Square instances in schema are unique.

    Super Class:
        *   StackService

    Provides:

    Attributes:
            SERVICE_NAME: str
            capacity: int
            schema: List[Square]
            controller: SquareStackOpsController
            service: SquareService:
            context_service: SquareQueryService
    
    # INHERITED ATTRIBUTES:
        *   See StackService for inherited attributes.

    Attributes:
        Local:
            *   id (int)
            *   schema (str)
            *   capacity (int)
            *   controller (SquareStackOpsController)
            *   service (SquareService)
            *   context_service (SquareQueryService)

        Inherited:
        None


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
        
    Methods:
    - pop(): Return DeletionResult[Square]
        *   push(item: Square) -> InsertionResult[bool]
        *   context(context: SquareContext) -> SearchResult[List[Square]]
        *   delete_by_id(id: int, identity_service: IdentityService) -> DeletionResult[Square]

    # INHERITED METHODS:
        *   See StackService class for inherited methods.
    """
    SERVICE_NAME = "SquareStackService"
    _capacity: int
    _stack: List[Square]
    _controller: SquareStackOpsController
    _service: SquareService
    _controller: SquareStackOpsController
    _context_service: SquareQueryService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            service: SquareService = SquareService(),
            controller: SquareStackOpsController = SquareStackOpsController(),
            capacity: int = NUMBER_OF_ROWS * NUMBER_OF_COLUMNS,
            id: int = IdFactory.next_id(class_name="SquareStackService"),
            context_service: SquareQueryService = SquareQueryService(),
    ):
        """
        Args:
            id: int
            name: str
            capacity: int
            service: SquareService
            context_service: SquareQueryService
        """
        method = "SquareService.__init__"
        super().__init__(id=id,name=name,)
        self._controller = controller
        self._service = service
        self._capacity = capacity
        self._context_service = context_service
        self._stack = []
        
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
    def current_item(self) -> Optional[Square]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> SquareService:
        return self._service
    
    @property
    def context_service(self) -> SquareQueryService:
        return self._context_service
    
    @property
    def controller(self) -> SquareStackOpsController:
        return self._controller
    
    @LoggingLevelRouter.monitor
    def push(self, item: Square) -> InsertionResult[bool]:
        """
        Args:
            item: Square
        """
        method = "SquareStackService.push"
        
        # --- Handoff the push responsibility to _controller ---#
        insertion_result = self._controller.crud.pusher.execute(stack=self, item=item)
    
        # Handle the case that, the search is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=insertion_result.exception,
                )
            )
        # --- Send the success result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Square]:
        method = "SquareStackService.pop"
        
        # --- Handoff the push responsibility to _controller ---#
        deletion_result = self._controller.crud.pop()
        
        # Handle the case that, the search is not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=deletion_result.exception,
                )
            )
        # --- Send the success result to the caller. ---#
        return deletion_result
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService(),
    ) -> DeletionResult[Square]:
        method = "SquareStackService.delete_by_id"
        
        # --- Handoff the delete_by_id responsibility to _controller ---#
        deletion_result =self._controller.crud.delete_by_id(
            id=id,
            square_stack=self,
            identity_service=identity_service
        )
        # Handle the case that, the deletion is not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=deletion_result.exception,
                )
            )
        # --- Send the success result to the caller. ---#
        return deletion_result
    
    def start_square_visit(
            self,
            token: Token,
            square: Square,
            token_service: TokenService = TokenService(),
) -> UpdateResult[Square]:
        method = "SquareStackService.start_square_visit"
        
        # --- Handoff the visit management responsibility to _controller ---#
        visitation_result = self._controller.token.occupy_stack_square(
            token=token,
            square=square,
            square_stack=self,
            token_service=token_service,
        )
        # Handle the case that the visit is not accomplished
        if visitation_result.is_failure:
            return UpdateResult.update_failure(
                original=square,
                exception=SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=visitation_result.exception,
                )
            )
        # --- Send the success result directly forward to the caller. ---#
        return visitation_result
    
    def end_square_visit(
            self,
            token: Token,
            token_service: TokenService = TokenService(),
    ) -> DeletionResult[Token]:
        method = "SquareStackService.end_square_visit"
        
        # --- Handoff the visit management responsibility to _controller ---#
        visitation_result = self._controller.token.remove_occupant_from_stack(
            occupant=token,
            square_stack=self,
            token_service=token_service,
        )
        # Handle the case that the visit is not accomplished
        if visitation_result.is_failure:
            return DeletionResult.failure(
                SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=visitation_result.exception,
                )
            )
        # --- Send the success result directly forward to the caller. ---#
        return visitation_result

    @LoggingLevelRouter.monitor
    def search(
            self,
            context: SquareContext,
    ) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a SquareCrudControllerException
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
            *   SquareCrudControllerException
        """
        method = "SquareStackService.context"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        query_result = self._context_service.finder.route(
            context=context,
            dataset=self._stack,
        )
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareStackException(
                    cls_mthd=method,
                    cls_name=self.__name__,
                    err_code=SquareStackException.ERR_CODE,
                    msg=SquareStackException.MSG,
                    ex=query_result.exception,
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
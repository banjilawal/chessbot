# src/logic/token/database/kernel/stack.py

"""
Module: logic.token.database.kernel.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional

from logic.board import Board
from logic.system import (
     SearchResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, IdFactory
)
from logic.token import (
    Token, TokenContext, TokenContextService, TokenService, TokenStackOpsController, TokenStackServiceException,
    TokenStackState
)


class TokenStackService(StackService[Token]):
    """
    Role:
        -   Data layer
        -   CRUD controller.
        -   ACID compliance.
        -   Microservice API
        -   Interface

    Responsibilities:
        1.  Preserve consistency during updates and deletes.
        2.  Stateful, scalable integrity management of Tokens.
        3.  Grant read access to tokens.

    Attributes:
        CAPACITY = 16
        SERVICE_NAME = TokenStackService
 
        capacity: int
        stack: List[Token]
        service: TokenService
        state: TokenStackState
        dispatcher: TokenStackOpsController
        context_service: TokenContextService

    Provides:
        -   id: int
        -   name: str
        -   items() -> List[T]
        -   size() -> int
        -   iterator() -> Iterator[T]
        -   is_empty() -> bool
        -   current_item(self) -> T
        -   integrity_service() -> IntegrityService[T]
        -   context_service(self) -> ContextService[T]
        -   push(item: T) -> InsertionResult
        -   pop() -> DeletionResult[T]
        -   delete_by_id(id: int) -> DeletionResult[T]
        -   query(collider_candidates: List[T], context: Context[T]) -> SearchResult[List[T]]
        -   operation() -> TokenStackOpsController
        -   is_getting_ready_for_deployment() -> bool
        -   is_ready_for_deployment() -> bool
        -   is_being_deployed() -> bool
        -   is_deployed_on_board() -> bool
        -   stack_state(self) -> TokenStackState

    Super:
    """
    DEFAULT_CAPACITY: int = 16
    SERVICE_NAME: str = "TokenStackService"
    
    _capacity: int
    _stack: List[Token]
    _service: TokenService
    _state: TokenStackState
    _dispatcher: TokenStackOpsController
    _context_service: TokenContextService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            capacity: int = DEFAULT_CAPACITY,
            service: TokenService = TokenService(),
            id: int = IdFactory.next_id(class_name="TokenStackService"),
            context_service: TokenContextService = TokenContextService(),
            dispatcher: TokenStackOpsController = TokenStackOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            capacity: int
            service: TokenService
            dispatcher: TokenStackOpsController
            context_service: TokenContextService
        """
        super().__init__(id=id, name=name,)
        self._stack = []
        self._service = service
        self._capacity = capacity
        self._dispatcher = dispatcher
        self._context_service = context_service
        self._state = TokenStackState.NOT_READY_FORD_DEPLOYMENT


    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def current_token(self) -> Optional[Token]:
        return self._stack[-1] if self._stack else None

    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_partially_full(self) -> bool:
        return 0 < self.size < self._capacity
    
    @property
    def is_full(self) -> bool:
        return self.size == self._capacity
    
    @property
    def current_item(self) -> Optional[Token]:
        return self._stack[-1] if self._stack else None
    
    @property
    def items(self) -> List[Token]:
        return self._stack
    
    @property
    def integrity_service(self) -> TokenService:
        return self._service
    
    @property
    def context_service(self) -> TokenContextService:
        return self._context_service
    
    @property
    def operation(self) -> TokenStackOpsController:
        return self._dispatcher
    
    @property
    def is_getting_ready_for_deployment(self) -> bool:
        return not self.is_full and self._state == TokenStackState.NOT_READY_FORD_DEPLOYMENT
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return self.is_full and self._state == TokenStackState.READY_FOR_DEPLOYMENT
    
    @property
    def is_being_deployed(self) -> bool:
        return self.is_partially_full and self._state == TokenStackState.BEING_DEPLOYED
    
    @property
    def is_deployed_on_board(self) -> bool:
        return self.is_empty and self._state == TokenStackState.DEPLOYED_ON_BOARD
    
    @property
    def stack_state(self) -> TokenStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: TokenStackState):
        self._state = state
        
    @property
    def iterator(self) -> iter:
        return iter(self._stack)
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Token]:
        """
        Remove the last token put on the stack.

        Action:
            If the pop fails, send an exception chain. Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # --- Forward the request to the dispatcher. ---#
        pop_result = self._dispatcher.crud.popper.pop()
        
        # Handle the case that, the request was not completed.
        if pop_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=pop_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return pop_result
    
    @LoggingLevelRouter.monitor
    def push(self, item: Token) -> InsertionResult[bool]:
        """
        Put the token onto the stack.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send
            the success result.
        Args:
            item: Token
        Returns:
            InsertionResult[bool]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.push"
        
        # --- Forward the request to the dispatcher. ---#
        insertion_result = self._dispatcher.crud.pusher.execute(
            token=item,
            token_stack=self,
            rank_quota_analyzer=self._dispatcher.rank_quota_analyzer,
            token_collision_detector=self._dispatcher.collision_detector
        )
        # Handle the case that, the request was not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        """
        Delete any token which has that id.
        
        Action:
            If the operation gets interrupted send an exception chain. Otherwise,
            send the success result.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.delete_by_id"
        
        # --- Forward the request to the dispatcher. ---#
        delete_by_id_result = self._dispatcher.crud.popper.delete_by_id(
            id=id,
            identity_service=identity_service
        )
        # Handle the case that, the request was not completed
        if delete_by_id_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=delete_by_id_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return delete_by_id_result
    
    @LoggingLevelRouter.monitor
    def query(self, context: TokenContext) -> SearchResult[List[Token]]:
        """
        Find tokens whose attribute value fits the context.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: TokenContext
        Returns:
            SearchResult[List[Token]]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.query"
        
        # --- Forward the request to the context_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the request was not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=query_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return query_result
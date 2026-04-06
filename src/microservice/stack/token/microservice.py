# src/microservice/stack/token/microservice.py

"""
Module: microservice.stack.token.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class TokenStackService(StackService[Token]):
    """
    Role:
        -   API
        -   ACID compliance
        -   Stateful microservice
        -   Stateful CRUD Controller
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Token collections.
        2.  Preserve consistency during updates and deletes.
        3.  Stateful, scalable integrity management of Tokens.
        4.  Token search and retrieval.

    Attributes:
        CAPACITY = 16
        SERVICE_NAME = TokenStackService
 
        id: int
        schema: str
        size: int
        capacity: int
        items: List[Token]
        iterator: Iterator[Token]
        stack_state: TokenStackState
        current_item: Optional[Token]
        integrity_service: TokenService
        ops_controller: TokenStackOpsController

    Provides:
        -   is_empty() -> bool
        -   is_being_deployed() -> bool
        -   is_deployed_on_board() -> bool
        -   pop() -> DeletionResult[Token]
        -   push(item: Token) -> InsertionResult
        -   is_ready_for_deployment() -> bool
        -   is_getting_ready_for_deployment() -> bool
        -   delete_by_id(id: int) -> DeletionResult[Token]
        -   context(context: Context[Token]) -> SearchResult[List[Token]]

    Super Class:
        StackService
    """
    DEFAULT_CAPACITY: int = 16
    SERVICE_NAME: str = "TokenStackService"
    
    _capacity: int
    _stack: List[Token]
    _state: TokenStackState
    _ops_controller: TokenStackOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            capacity: int = DEFAULT_CAPACITY,
            id: int = IdFactory.next_id(class_name="TokenStackService"),
            ops_controller: TokenStackOpsController = TokenStackOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            capacity: int
            ops_controller: TokenStackOpsController
        """
        super().__init__(id=id, name=name,)
        self._stack = []
        self._capacity = capacity
        self._ops_controller = ops_controller
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
    def iterator(self) -> Iterator[Token]:
        return iter(self._stack)
    
    @property
    def request(self) -> TokenStackOpsController:
        return self._ops_controller
    
    @property
    def integrity_service(self) -> TokenService:
        return self._ops_controller.service
    
    @property
    def is_getting_ready_for_deployment(self) -> bool:
        return not (
                self.is_full and
                self._state == TokenStackState.NOT_READY_FORD_DEPLOYMENT
        )
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return (
                self.is_full and
                self._state == TokenStackState.READY_FOR_DEPLOYMENT
        )
    
    @property
    def is_being_deployed(self) -> bool:
        return self.is_partially_full and self._state == TokenStackState.BEING_DEPLOYED
    
    @property
    def is_deployed_on_board(self) -> bool:
        return (
                self.is_empty and
                self._state == TokenStackState.DEPLOYED_ON_BOARD
        )
    
    @property
    def stack_state(self) -> TokenStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: TokenStackState):
        self._state = state
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Token]:
        """
        Remove the last token put on the schema.

        Action:
            If the pop fails, send an exception chain. Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.analyze()
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def push(self, item: Token) -> InsertionResult[bool]:
        """
        Put the token onto the schema.

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
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.push.analyze(
            token=item,
            token_stack=self,
            rank_quota_analyzer=self._ops_controller.rank_quota_analyzer,
            token_collision_detector=self._ops_controller.collision_detector
        )
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=request_result.exception,
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
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.delete_by_id(
            id=id,
            identity_service=identity_service
        )
        # Handle the case that, the request was not completed
        if request_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: TokenContext) -> SearchResult[List[Token]]:
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
        method = f"{self.__class__.__name__}.context"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.query.search(context=context)
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackServiceException.MSG,
                    err_code=TokenStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
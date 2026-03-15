# src/logic/token/database/core/stack.py

"""
Module: logic.token.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional

from logic.system import (
     SearchResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, IdFactory
)
from logic.token import (
    PoppingEmptyTokenStackException, Token, TokenContext, TokenService, TokenServiceException, TokenStackException,
    TokenContextService,
    PoppingTokenException, PushingTokenException, TokenStackFullException, TokenStackState, TokenStackHandler,
)


class TokenStackService(StackService[Token]):
    """
    # ROLE: Data Stack, SearchWorker IntegrityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Token objects and their lifecycles.
    3.  Ensure integrity of Token data stack
    4.  Stack data structure for Token objects with no guarantee of uniqueness.
    
    # PARENT:
        *   StackService[Token]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    DEFAULT_CAPACITY: int = 16
    SERVICE_NAME: str = "TokenStackService"
    
    _capacity: int
    _stack: List[Token]
    _service: TokenService
    _state: TokenStackState
    _handler: TokenStackHandler
    _context_service: TokenContextService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            capacity: int = DEFAULT_CAPACITY,
            service: TokenService = TokenService(),
            handler: TokenStackHandler = TokenStackHandler(),
            id: int = IdFactory.next_id(class_name="TokenStackService"),
            context_service: TokenContextService = TokenContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   service (TokenService)
            *   context_service (TokenContextService)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "TokenService.__init__"
        super().__init__(id=id, name=name,)
        self._stack = []
        self._capacity = capacity
        self._handler = handler
        self._service = service
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
    def handler(self) -> TokenStackHandler:
        return self._handler
        
    @property
    def integrity_service(self) -> TokenService:
        return self._service
    
    @property
    def context_service(self) -> TokenContextService:
        return self._context_service
    
    @property
    def stack_state(self) -> TokenStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: TokenStackState):
        self._state = state
    
    @LoggingLevelRouter.monitor
    def push(self, item: Token) -> InsertionResult[bool]:
        """
        Action:
            1.  Insert a token into the TokenStackService.
            
        Args:
            item: Token
            
        Returns:
            InsertionResult[bool]
            
        Raises:
            *   TokenStackException
        """
        method = f"{self.__class__.__name__}.push"
        
        insertion_result = self._handler.crud.push(
            token=item,
            token_stack=self,
            rank_quota_analyzer=self._handler.rank_quota_analyzer,
            token_collision_detector=self._handler.collision_detector
        )
        # Handle the case that, the insertion is not successful
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackException.MSG,
                    err_code=TokenStackException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # --- Send the success result to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Token]:
        """
        Action:
            Remove the item at the top of the stack if it's not empty.
            
        Args:
        
        Returns:
            DeletionResult[Token]
            
        Raises:
            TokenStackException
        """
        method = f"{self.__class__.__name__}.pop"
    
        # --- Handoff pop responsibility. ---#
        pop_result = self._handler.crud.pop()
        
        # Handle the case that, that the pop is not completed.
        if pop_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackException.MSG,
                    err_code=TokenStackException.ERR_CODE,
                    ex=pop_result.exception,
                )
            )
        # --- On success forward to the client. ---#
        return pop_result
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the id is not certified safe send an exception in the DeletionResult.
            2.  Create a temp variable for storing a token before it's deleted.
            3.  Iterate through the tokens.
                    *   If a token's id matches the target record the token in a temp variable before deleting
                        it from the list.
            4.  After the loop is finishes, if the temp variable is not None send it in the deletion success result.
                Else, send the nothing to delete result instead.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   DeletionResult[Token]
        Raises:
            *   TokenStackException
            *   PoppingTokenException
            *   PoppingEmptyTokenStackException
        """
        method = "TokenStackService.delete_by_id"
        
        # Handle the case that, there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    msg=f"StackId:{self.id}, {method}: {TokenStackException.ERR_CODE}",
                    ex=PoppingTokenException(
                        msg=f"{method}: {PoppingTokenException.ERR_CODE}",
                        ex=PoppingEmptyTokenStackException(
                            f"{method}: {PoppingEmptyTokenStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    msg=f"StackId:{self.id}, {method}: {TokenStackException.ERR_CODE}",
                    ex=PoppingTokenException(
                        msg=f"{method}: {PoppingTokenException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for token in self._stack:
            if token.id == id:
                # Record a hit before pulling it from the stack.
                target = token
                self._stack.remove(token)
        # --- Perform cleanup and integrity maintenance tasks after the purging loop finishes. ---#
        if self.is_empty:
            self._state = TokenStackState.EMPTY
        # --- Handle the possible return cases. ---#
        
        # At least one token was removed.
        if target is not None:
            return DeletionResult.success(payload=target)
        # Default case: no tokens were removed.
        return DeletionResult.nothing_to_delete()
    
    @LoggingLevelRouter.monitor
    def query(self, context: TokenContext) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Pass the context param to context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures context_service will be encapsulated inside a TokenStackException which is
                sent inside a SearchResult.
            3.  If the search completes successfully return the result directly because its a SearchResult instance.
        # PARAMETERS:
            *   context (TokenContext)
        # RETURN:
            *   SearchResult[List[Token]] containing either:
                    - On failure: An exception.
                    - On success: List[Token].
                    - On Empty: payload null, exception null.
        Raises:
            *   TokenStackException
        """
        method = "TokenStackService.query"
        
        # --- Handoff the search responsibility to _context_service. ---#
        query_result = self._context_service.finder.find(dataset=self._stack, context=context)
        
        # Handle the case that, the search is not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenStackException(
                    msg=f"ServiceID:{self.id} {method}: {TokenStackException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return query_result
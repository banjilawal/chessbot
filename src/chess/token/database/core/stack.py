# src/chess/token/database/core/stack.py

"""
Module: chess.token.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional, cast

from chess.board import Board
from chess.formation import FormationService
from chess.rank import Rank, RankService
from chess.square import SquareContext
from chess.system import (
    ComputationResult, RollbackException, SearchResult, StackService, DeletionResult, IdentityService, InsertionResult,
    LoggingLevelRouter,
    id_emitter
)
from chess.system.transfer import TransferResult
from chess.token import (
    AddingDuplicateTokenException, AppendingTokenDirectlyIntoItemsFailedException, NoRankOpeningsException,
    PoppingEmptyTokenStackException,
    RankQuotaManager, Token,
    TokenBoardState, TokenContext, TokenDesignationAlreadyInUseException, TokenIdAlreadyInUseException,
    TokenOpeningSquareAlreadyInUseException, TokenService,
    TokenStackException, TokenDoesNotExistForRemovalException, TokenContextService, TokenDeletionFailedException,
    TokenPushFailedException, RankQuotaComputationFailedException, TokenServiceCapacityException,
)
from chess.token.database.core.state import TokenStackState


class TokenStack(StackService[Token]):
    """
    # ROLE: Data Stack, AbstractSearcher EntityService, CRUD Operations, Encapsulation, API layer.

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
    SERVICE_NAME: str = "TokenStack"
    
    _capacity: int
    _stack_state: TokenStackState
    _stack: List[Token]
    _formation_service: FormationService
    _rank_quota_manager: RankQuotaManager
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Token] = List[Token],
            capacity: int = DEFAULT_CAPACITY,
            token_service: TokenService = TokenService(),
            formation_service: FormationService = FormationService(),
            rank_quota_manager: RankQuotaManager = RankQuotaManager(),
            token_context_service: TokenContextService = TokenContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   bag (List[Token])
            *   token_service (TokenService)
            *   formation_service (FormationService)
            *   token_context_service (TokenContextService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "TokenService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=token_service,
            context_service=token_context_service,
        )
        self._capacity = capacity
        self._formation_service = formation_service
        self._rank_quota_manager = rank_quota_manager
        self._stack_state = TokenStackState.EMPTY
        self._stack = items
        
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
    def is_full(self) -> bool:
        return (
                self.size == self._capacity and
                self._stack_state == TokenStackState.FILLED_READY_TO_DEPLOY
        )
    
    @property
    def is_empty(self) -> bool:
        return (
                self.size == 0 and
                self._stack_state == TokenStackState.EMPTY
        )
    
    @property
    def is_deployed_on_board(self) -> bool:
        return (
                self.size == 0 and
                self._stack_state == TokenStackState.DEPLOYED_ON_BOARD
        )
        
    @property
    def integrity_service(self) -> TokenService:
        return cast(TokenService, self.entity_service)
    
    @property
    def context_service(self) -> TokenContextService:
        return cast(TokenContextService, self.context_service)
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def rank_quota_manager(self) -> RankQuotaManager:
        return self._rank_quota_manager
    
    @property
    def stack_state(self) -> TokenStackState:
        return self._stack_state
    
    @stack_state.setter
    def stack_state(self, state: TokenStackState):
        self._stack_state = state
    
    @LoggingLevelRouter.monitor
    def push(self, item: Token) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the occupant is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   occupant (Token)
        # RETURNS:
            *   InsertionResult[Token] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenStackException
        """
        method = "TokenStack.add_token"
        
        # Handle the case that the list is full.
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=TokenServiceCapacityException(f"{method}: {TokenServiceCapacityException.ERROR_CODE}")
                    )
                )
            )
        # Handle the case that the occupant is unsafe.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that either the id, designation or opening square are already used.
        colliding_tokens_search_result = self._find_colliding_tokens(target=item)
        if not colliding_tokens_search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=colliding_tokens_search_result.exception
                    )
                )
            )
        # --- Find out if there are open slots for the token's rank ---#
        rank_has_opening_result = self._rank_quota_manager.has_rank_opening(rank=item.rank, token_stack=self)
        
        # Handle the case that the boolean query is not answered.
        if rank_has_opening_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=rank_has_opening_result.exception
                    )
                )
            )
        # Handle the case that the token's rank is full.
        rank_has_opening = rank_has_opening_result.payload
        if not rank_has_opening:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=NoRankOpeningsException(f"{method}: {NoRankOpeningsException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Push the token onto the stack. ---#
        self.items.append(item)
        
        # --- If the stack is full  update TokenStackState before sending the success result. ---#
        if self.size == self.capacity:
            self._stack_state = TokenStackState.FILLED_READY_TO_DEPLOY
        # Send the popped token to the caller.
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the stack is empty send an exception in the DeletionResult. Else remove the
                token at the top of the stack and send in the DeletionResult
        # PARAMETERS:
                    *   None
        # RETURNS:
            *   DeletionResult[Token] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenStackException
            *   PoppingEmptyTokenStackException
        """
        method = "TokenStack.dpop"
        
        # Handle the case that there are no tokens in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenDeletionFailedException(
                        message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                        ex=PoppingEmptyTokenStackException(
                            f"{method}: {PoppingEmptyTokenStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Pop the non-empty token stack. ---#
        token = self._stack.pop(-1)
        
        # --- If the stack is empty update TokenStackState before sending the success result. ---#
        if self.size == 0:
            self._stack_state = TokenStackState.EMPTY
        # Send the popped token to the caller.
        return DeletionResult.success(token)
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self, 
            id: int, 
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_tokens_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_tokens_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Token] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenStackException
        """
        method = "TokenStack.delete_token_by_id"
        
        # Handle the case that there are no tokens in the stack.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenDeletionFailedException(
                        message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                        ex=PoppingEmptyTokenStackException(
                            f"{method}: {PoppingEmptyTokenStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case of that the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenDeletionFailedException(
                        message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                        ex=TokenDoesNotExistForRemovalException(
                            f"{method}: {TokenDoesNotExistForRemovalException.ERROR_CODE}"
                        )
                    )
                )
            )
        # --- After validation checks do the deletion processing. ---#
        deletion_counter = 0
        deleted_token = None
        
        # Iterate through the list and to find id matches.
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Token):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        TokenStackException(
                            message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                            ex=TokenDeletionFailedException(
                                message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Token, got {type(item).__name__} "
                                    f"instead of a Token."
                                )
                            )
                        )
                    )
                # Store the item before removing it then, increment the deletion counter after the removal.
                deleted_token = item
                self.items.remove(item)
                deletion_counter += 1
            # --- If there was nothing to delete inform the caller. ---#
            if deletion_counter == 0:
                return DeletionResult.nothing_to_delete()
            
            # --- Otherwise update state before sending the success result. ---#
            if self.size == 0:
                self._stack_state = TokenStackState.EMPTY
            return DeletionResult.success(deleted_token)
        
    def form_tokens(self) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the stack is not full send an exception chain in the TransferResult.
            2.  For each token:
                i.      Look for its opening square in the board.
                ii.     If the search fails or the square is not found send an exception chain.
                iii.    Copy the token to transferred_tokens list before it occupies its square.
                iii.    If the occupation fails call _rollback_transfer to restore the stack and board to their
                        original states.
            3.  If the increase in board occupants does not match the stack's capacity send an exception chain
                in the TransferResult.
            4.  Set the TokenStackState to empty.
            5.  The transfer has been completed. Send the TokenStack and Board in the TransferResult.
        # PARAMETERS:
            None
        # RETURNS:
            *   TransferResult[TokenStack, Board] containing either:
                    - On failure: Exception.
                    - On success: TokenStack and Board in the TransferResult.
        # RAISES:
            *   TokenStackException
            *   TokenStackDeploymentFailedException
            *   EmptyTokenStackCannotDeployException
        """
        method = "TokenStack.place_tokens"
        
        # Handle the case that TokenStack is empty.
        if not self.is_empty:
            # Return the exception on failure.
            return InsertionResult.failure(
                TokenStackException(
                    f"ServiceId:{self.id}, {method}: {TokenStackException}",
                    ex=TokenStackDeploymentFailedException(
                        message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                        ex=EmptyTokenStackCannotDeployException(
                            f"{method}: {EmptyTokenStackDeploymentExceptionDEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that TokenStack is not full.
        if not self.is_full:
            # Return the exception on failure.
            return InsertionResult.failure(
                TokenStackException(
                    f"ServiceId:{self.id}, {method}: {TokenStackException}",
                    ex=TokenStackDeploymentFailedException(
                        message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                        ex=CannotDeployPartlyFullTokenStackException(
                            f"{method}: {CannotDeployPartlyFullTokenStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Start the transfer process. ---#
        transferred_tokens: [Token] = []
        board = self.current_token.team.board
        for token in self.items:
            formation_result = self.integrity_service.deploy_on_board(token=token)
            if formation_result.is_failure:
                # Return the exception on failure.
                return InsertionResult.failure(
                    TokenStackException(
                        f"ServiceId:{self.id}, {method}: {TokenStackException}",
                        ex=TokenStackDeploymentFailedException(
                            message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                            ex=formation_result.exception
                        )
                    )
                )
            # --- Copy the successful occupant into transferred tokens in case a rollback is needed. ---#
            clone_token = token
            transferred_tokens.append(clone_token)
        
        # --- Update the stack's state and send the success result. ---#
        self._stack_state = TokenStackState.EMPTY
        return InsertionResult.success()
    
    def _rollback_transfer(
            self,
            board: Board,
            recovery_targets: [Token],
            debug_exception: Exception,
    ) -> InsertionResult[bool]:
        method = "TokenStack.rollback_transfer"
        
        # If there are no recovery targets nothing needs to be rolled back.
        if len(recovery_targets) == 0:
            # Return the debug exception in a chain.
            return InsertionResult.failure(
                exception=TokenStackException(
                    f"ServiceId:{self.id}, {method}: {TokenStackException}",
                    ex=TokenStackDeploymentFailedException(
                        message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                        ex=debug_exception
                    )
                )
            )
        # --- Otherwise go through the board, removing the recovery targets. ---#
        for target in recovery_targets:
            # Handle the case that the removal crashes
            removal_result = board.squares.delete_occupant_by_search(occupant=target)
            if removal_result.is_failure:
                # Return the exception chain on failure.
                return InsertionResult.failure(
                    exception=TokenStackException(
                        f"ServiceId:{self.id}, {method}: {TokenStackException}",
                        ex=TokenStackDeploymentFailedException(
                            message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                            ex=RollbackException(
                                message=f"{method}: {RollbackException.ERROR_CODE}",
                                ex=removal_result.exception
                            )
                        )
                    )
                )
            # Handle the case that target is not found.
            if removal_result.nothing_to_delete:
                # Return the exception chain on failure.
                return InsertionResult.failure(
                    exception=TokenStackException(
                        f"ServiceId:{self.id}, {method}: {TokenStackException}",
                        ex=TokenStackDeploymentFailedException(
                            message=f"{method}: {TokenStackDeploymentFailedException.ERROR_CODE}",
                            ex=RollbackException(
                                message=f"{method}: {RollbackException.ERROR_CODE}",
                                ex=RecoveryTargetNotFoundException(
                                    f"{method}: {RecoveryTargetNotFoundException.DEFAULT_MESSAGE}"
                                )
                            )
                        )
                    )
                )
            # --- Restore the ejected token's pre-deployment state. ---#
            token = removal_result.payload
            token.positions.pop_coord()
            token.board_state = TokenBoardState.NEVER_BEEN_PLACED
            self.items.append(token)
    
                
        
   
    def _find_colliding_tokens(self, target: Token) -> SearchResult[Token]:
        """
        # ACTION:
            1.  If any stack members share either an id, designation or opening square with the target send and
                exception in the SearchResult. Those three properties must be unique within the game.
            2.  If no matches are found send an empty SearchResult indicating there were no collisions.
        # PARAMETERS:
                    *   target (Token)
        # RETURNS:
            *   SearchResult[List[Token]] containing either:
                    - On failure: Exception or non-empty list.
                    - On success: Empty search result.
        # RAISES:
            *  TokenIdAlreadyInUseException
            *  TokenDesignationAlreadyInUseException
            *   TokenOpeningSquareAlreadyInUseException
        """
        method = "TokenStack._find_colliding_tokens"
        
        # --- Loop through the stack to find matches. ---#
        for item in self.items:
            # Return an exception in the SearchResult if a stack member shares the target's id.
            if item.id == target.id:
                return SearchResult.failure(
                    TokenIdAlreadyInUseException(
                        f"{method}: {TokenIdAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            # Return an exception in the SearchResult if a stack member shares the target's designation.
            if item.designation.upper() == target.designation.upper():
                return SearchResult.failure(
                    TokenDesignationAlreadyInUseException(
                        f"{method}: {TokenDesignationAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            # Return an exception in the SearchResult if a stack member shares the target's opening square.
            if item.opening_square.upper() == target.opening_square.upper():
                return SearchResult.failure(
                    TokenOpeningSquareAlreadyInUseException(
                        f"{method}: {TokenOpeningSquareAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
        # --- At the happy path return an empty search result indication there are no collisions. ---#
        return SearchResult.empty()
# src/chess/token/database/core/stack.py

"""
Module: chess.token.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.formation import FormationService
from chess.rank import Rank, RankService
from chess.square import SquareContext
from chess.system import (
    ComputationResult, SearchResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    id_emitter
)
from chess.token import (
    AddingDuplicateTokenException, AppendingTokenDirectlyIntoItemsFailedException, NoRankOpeningsException,
    PoppingEmptyTokenStackException,
    RankQuotaManager, Token,
    TokenContext, TokenDesignationAlreadyInUseException, TokenIdAlreadyInUseException,
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
    _deployment_state: TokenStackState
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
        self._deployment_state = TokenStackState.EMPTY

        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return len(self.items) == self._capacity and self._deployment_state == TokenStackState.FILLED
    
    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0 and self._deployment_state == TokenStackState.EMPTY
    
    @property
    def is_deployed_on_board(self) -> bool:
        return len(self.items) == 0 and self._deployment_state == TokenStackState.DEPLOYED_ON_BOARD
        
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
    def deployment_state(self) -> TokenStackState:
        return self._deployment_state
    
    @deployment_state.setter
    def deployment_state(self, state: TokenStackState):
        self._deployment_state = state
    
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
        # Handle the case that at least one stack member already has the insertion target's
        # id, designation or square.
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
        # Handle the case that the token is already in the stack.
        if item in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Query if there are opening s ---#
        boolean_query = self._rank_quota_manager.has_rank_opening(rank=item.rank, token_stack=self)
        
        # Handle the case that the boolean query is not answered.
        if boolean_query.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=boolean_query.exception
                    )
                )
            )
        # Handle the case that the token's rank is full.
        has_openings = boolean_query.payload
        if not has_openings:
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

        # --- Append the token to the stack and send the success result. ---#
        self.items.append(item)
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
    
    @LoggingLevelRouter.monitor
    def delete_token_by_id(
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
        # --- Search the list for a occupant with target id. ---#
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
                # --- Cast the item before removal and return the deleted occupant in the DeletionResult. ---#
                token = cast(Token, item)
                self.items.remove(token)
                return DeletionResult.success(payload=token)
            
            # If none of the bag had that id return an empty DeletionResult.
            return DeletionResult.nothing_to_delete()
        
    def form_tokens(self) -> InsertionResult[bool]:
        method = "TokenStack.place_tokens"
        for token in self.items:
            square_search_result = token.team.board.squares.search_squares(
                context=SquareContext(token.opening_square)
            )
            
            # Handle the case that the search is not completed.
            if square_search_result.is_failure:
                # Return the exception on failure.
                return InsertionResult.failure(
                    TokenStackException(
                        f"{method}: {TokenStackException}",
                        ex=square_search_result.exception
                    )
                )
            # Handle the case the square is not found.
            if square_search_result.is_empty:
                # Return the exception on failure.
                return InsertionResult.failure(
                    TokenStackException(
                        f"{method}: {TokenStackException}",
                        ex=OpeningSquareNotFoundException(
                            f"{method}: {OpeningSquareNotFoundException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            occupation_result = token.team.board.squares.add_occupant_to_square(
                token=token,
                square=square_search_result.payload[0],
            )
            # Handle the case that occupying the opening square fails.
            if occupation_result.is_failure:
                # Return the exception on failure.
                return InsertionResult.failure(
                    TokenStackException(
                        f"{method}: {TokenStackException}",
                        ex=occupation_result.exception
                    )
                )
        self._deployment_state = TokenStackState.DEPLOYED_ON_BOARD
        return InsertionResult.success()
   
    def _find_colliding_tokens(self, target: Token) -> SearchResult[Token]:
        method = "TokenStack._attribute_collision_detector"
        
        for item in self.items:
            if item.id == target.id:
                return SearchResult.failure(
                    TokenIdAlreadyInUseException(
                        f"{method}: {TokenIdAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            if item.designation.upper() == target.designation.upper():
                return SearchResult.failure(
                    TokenDesignationAlreadyInUseException(
                        f"{method}: {TokenDesignationAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
            if item.opening_square == target.opening_square:
                return SearchResult.failure(
                    TokenOpeningSquareAlreadyInUseException(
                        f"{method}: {TokenOpeningSquareAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
        return SearchResult.empty()
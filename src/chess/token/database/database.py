# src/chess/token/database/database.py

"""
Module: chess.token.database.database
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List

from chess.rank import Rank
from chess.token import (
    RankQuotaManager, Token, TokenContext, TokenContextService, TokenStack, TokenService, TokenDatabaseException,
    TokenStackState
)
from chess.system import (
    ComputationResult, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult, Database,
    id_emitter
)


class TokenDatabase(Database[Token]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by TokenStack are unique.
    2.  Guarantee consistency of records in TokenStack.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "TokenDatabase"
    _token_stack: TokenStack
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            token_stack: TokenStack = TokenStack(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (TokenStack)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=token_stack)
        self._token_stack = token_stack
    
    @property
    def integrity_service(self) -> TokenService:
        return self._token_stack.integrity_service
    
    @property
    def context_service(self) -> TokenContextService:
        return self._token_stack.context_service
    
    @property
    def rank_quota_manager(self) -> RankQuotaManager:
        return self._token_stack.rank_quota_manager
    
    @property
    def size(self) -> int:
        return self._token_stack.size
    
    @property
    def is_full(self) -> bool:
        return self._token_stack.is_full
    
    @property
    def is_empty(self) -> bool:
        return self._token_stack.is_empty
    
    @property
    def is_deployed(self) -> bool:
        return self._token_stack.is_deployed_on_board
    
    @property
    def stack_state(self) -> TokenStackState:
        return self._token_stack.stack_state
    
    @stack_state.setter
    def stack_state(self, state: TokenStackState):
        self._token_stack.deployment_state = state
        
    @LoggingLevelRouter.monitor
    def deploy_tokens_on_board(self) -> InsertionResult[bool]:
        return self._token_stack.form_tokens()
    
    @LoggingLevelRouter.monitor
    def number_open_rank_slots(self, rank: Rank) -> ComputationResult[int]:
        method = "TokenDatabase.open_rank_slots"
        
        # Handle the case that the calculation was not completed.
        open_slots_count_result = self._token_stack.rank_quota_manager.number_of_rank_openings(
            rank=rank,
            token_stack=self._token_stack
        )
        # Return the exception chain on failure.
        if open_slots_count_result.is_failure:
            return ComputationResult.failure(
                TokenDatabaseException(
                    f"{method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=open_slots_count_result.exception,
                )
            )
        # --- For either a successful calculation result directly forward to the caller. ---#
        return open_slots_count_result
    
    @LoggingLevelRouter.monitor
    def rank_size(self, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.number_of_rank_members.
            2.  If the calculation fails wrap the exception chain and send in the ComputationResult.
                Else directly forward the ComputationResult to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenDatabaseException
        """
        method = "TokenDatabase.size"
        
        # Handle the case that the calculation was not completed.
        rank_size_result = self._token_stack.rank_quota_manager.rank_size(
            rank=rank,
            token_stack=self._token_stack
        )
        if rank_size_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenDatabaseException(
                    f"{method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=rank_size_result.exception,
                )
            )
        # --- For either a successful calculation result directly forward to the caller. ---#
        return rank_size_result
    
    @LoggingLevelRouter.monitor
    def can_accept_rank(self, rank: Rank) -> ComputationResult[bool]:
        method = "TokenDatabase.can_accept_rank"
        does_rank_have_opening_result = self._token_stack.rank_quota_manager.has_rank_opening(
            rank=rank,
            token_stack=self._token_stack
        )
        if does_rank_have_opening_result.is_failure:
            return ComputationResult.failure(
                TokenDatabaseException(
                    f"{method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=does_rank_have_opening_result.exception,
                )
            )
    
    @LoggingLevelRouter.monitor
    def delete_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TokenDatabaseException
            *   TokenDatabase
        """
        method = "TokenDatabase.remove_token"
        
        # --- Handoff the deletion responsibility to _token_database_core. ---#
        deletion_result = self._token_stack.delete_by_id(id=id, identity_service=identity_service)
        
        # Handle the case that the deletion was not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        # --- For either a successful or null deletion result directly forward to the caller. ---#
        return deletion_result
   
    @LoggingLevelRouter.monitor
    def insert(self, token: Token) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the item either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _token_database_core.insert_token fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   InsertionResult[Bool] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
        # RAISES:
            *   TokenDatabaseException
            *   TokenDatabaseInsertionException
            *   TokenDatabaseException
        """
        method = "TokenDatabase.insert_token"
        
        # --- Use _token_database_core.insert_token because order does not matter for the occupant access. ---#
        insertion_result = self._token_stack.push(item=token)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=insertion_result.exception
                    )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: TokenContext) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the result of calling _token_database_core.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   TokenDatabaseException
            *   TokenDatabase
        """
        method = "TokenDatabase.search_tokens"
        
        # --- Handoff the search responsibility to _token_database_core. ---#
        search_result = self._token_stack.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {TokenDatabaseException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
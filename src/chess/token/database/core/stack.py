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
from chess.system import (
    ComputationResult, SearchResult, StackService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    id_emitter
)
from chess.token import (
    AddingDuplicateTokenException, AppendingTokenDirectlyIntoItemsFailedException, NoRankOpeningsException,
    PoppingEmptyTokenStackException,
    RankQuotaManager, Token,
    TokenContext, TokenDesignationAlreadyInUseException, TokenIdAlreadyInUseException, TokenService,
    TokenStackException, TokenDoesNotExistForRemovalException, TokenContextService, TokenDeletionFailedException,
    TokenPushFailedException, RankQuotaComputationFailedException, TokenServiceCapacityException,
)

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
    _formation_service: FormationService
    _rank_quota_manager: RankQuotaManager

    _capacity: int
    
    
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

        
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_full(self) -> bool:
        return len(self.items) == self._capacity
    
    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0
        
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
    
    @LoggingLevelRouter.monitor
    def team_max_tokens_per_rank(self, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If formation_service fails to return a quota value, send the exception chain in the ComputationResult.
                Else, directly forward quota_result to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenStackException
        """
        method = "TokenStack.team_max_tokens_per_rank"
        
        # --- Handoff the rank validation and quote lookup to self._formation_service ---#
        
        # Handle the case that the quota lookup is not completed.
        quota_result = self._formation_service.persona_service.quota_per_rank(rank=rank)
        if quota_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=quota_result.exception
                )
            )
        # On success just forward the quota_result to the caller.
        return quota_result
    
    @LoggingLevelRouter.monitor
    def number_of_rank_members(self, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Build the search-by-rank TokenContext. If the build fails send the exception in the InsertionResult.
                Else run the search.
            2.  If the search fails send the exception in the InsertionResult. Else the calculation was successful.
                Return the number of hits in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenStackException
            *   RankQuotaComputationFailedException
        """
        method = "TokenStack.number_of_rank_members"
        
        # --- First step in getting rank count is building search-by-rank context. ---#
        build_result = self.context_service.builder.build(rank=rank)
        
        # Handle the case that the context build is not completed.
        if build_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.ERROR_CODE}",
                        ex=build_result.exception
                    )
                )
            )
        # --- Cast the context_build_result payload and run the search. ---#
        search_result = self.context_service.finder.find(context=cast(TokenContext, build_result.payload))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that no tokens hold the rank
        if search_result.is_empty:
            return ComputationResult.success(payload=0)
        # Handle the case that some hits were found
        return ComputationResult.success(payload=len(cast(List[Token], search_result.payload)))
    
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
        # Handle the case that one of the items unique attributes is already in use.
        collision_detection = self._find_colliding_tokens(target=item)
        if not collision_detection.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=TokenPushFailedException(
                        message=f"{method}: {TokenPushFailedException.ERROR_CODE}",
                        ex=collision_detection.exception
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
        
        # Handle the case that there are no bag in the list.
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
            return DeletionResult.empty()
        
    @LoggingLevelRouter.monitor
    def has_slot_for_rank(self, rank: Rank) -> ComputationResult[bool]:
        """
        # ACTION:
            1.  If self.count_rank_openings fails send the exception chain in the ComputationResult. Else,
                send open_slot_count > 0 in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
        # RETURN:
            *   CalculationReport[bool] containing either:
                    - On failure: Exception
                    - On success: bool
        # RAISES:
            *   TokenStackException
            *   RankQuotaComputationFailedException
        """
        method = "TokenStack.has_slot_for_rank"
        
        # Handle the case that the rank is not certified safe.
        openings_count = self.count_rank_openings(rank)
        if openings_count.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.ERROR_CODE}",
                        ex=openings_count.exception
                    )
                )
            )
    
        # --- Find if there are open slots for the rank. ---#
        has_opening = cast(int, openings_count.payload) > 0
        return ComputationResult.success(payload=has_opening)
    
    @LoggingLevelRouter.monitor
    def count_rank_openings(self, rank: Rank, rank_service: RankService = RankService()) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If the rank is not validated, send an exception chain in the ComputationResult.
            2.  If calculating the number of rank members fails send an exception chain in the ComputationResult.
                Else, send rank.team_quota - rank_members in the ComputationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
            *   rank_service (RankService
        # RETURN:
            *   CalculationReport[int] containing either:
                    - On failure: Exception
                    - On success: int
        # RAISES:
            *   TokenStackException
            *   RankQuotaComputationFailedException
        """
        method = "TokenStack.count_rank_openings"
        
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.ERROR_CODE}",
                        ex=rank_validation.exception
                    )
                )
            )
        # --- Find if there are open slots for the rank. ---#
        rank_count_result = self.number_of_rank_members(rank=rank)
        
        # Handle the case that the rank_count_result_computation was not completed.
        if rank_count_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                TokenStackException(
                    message=f"ServiceId:{self.id}, {method}: {TokenStackException.ERROR_CODE}",
                    ex=RankQuotaComputationFailedException(
                        message=f"{method}: {RankQuotaComputationFailedException.ERROR_CODE}",
                        ex=rank_count_result.exception
                    )
                )
            )
        # --- On success send the difference between the quota and rank_member_count in the ComputationResult. ---#
        rank_member_count = cast(int, rank_count_result.payload)
        return ComputationResult.success(payload=rank.team_quota - rank_member_count)
    
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
            if item.opening_square() == target.opening_square:
                return SearchResult.failure(
                    TokenOpeningSquareAlreadyInUseException(
                        f"{method}: {TokenOpeningSquareAlreadyInUseException.DEFAULT_MESSAGE}",
                    )
                )
        return SearchResult.empty()
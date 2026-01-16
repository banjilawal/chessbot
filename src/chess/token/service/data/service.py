# src/chess/token/service/data/service_.py

"""
Module: chess.token.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.formation import FormationService
from chess.rank import Rank, RankService
from chess.system import (
    CalculationResult, DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
)
from chess.token import (
    AppendingTokenDirectlyIntoItemsFailedException, PoppingEmptyTokenStackException, Token, TokenContext, TokenService,
    TokenDataServiceException, TokenDoesNotExistForRemovalException, TokenContextService, TokenDeletionFailedException,
    TokenInsertionFailedException, RankCountCalculationFailedException,
)

class TokenDataService(DataService[Token]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Token objects and their lifecycles.
    3.  Ensure integrity of Token data stack
    4.  Stack data structure for Token objects with no guarantee of uniqueness.
    
    # PARENT:
        *   DataService[Token]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "TokenDataService"
    _formation_service: FormationService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Token] = List[Token],
            token_service: TokenService = TokenService(),
            formation_service: FormationService = FormationService(),
            token_context_service: TokenContextService = TokenContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Token])
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
        self._formation_service = formation_service
        
    @property
    def token_service(self) -> TokenService:
        return cast(TokenService, self.entity_service)
    
    @property
    def token_context_service(self) -> TokenContextService:
        return cast(TokenContextService, self.context_service)
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @LoggingLevelRouter.monitor
    def team_max_tokens_per_rank(self, rank: Rank) -> CalculationResult[int]:
        """
        # ACTION:
            1.  If formation_service fails to return a quota value send the exception chain in the CalculationResult.
                Else, directly forward quota_result to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   CalculationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenDataServiceException
        """
        method = "TokenDataService.team_max_tokens_per_rank"
        
        # --- Handoff the rank validation and quote lookup to self._formation_service ---#
        
        # Handle the case that the quota lookup is not completed.
        quota_result = self._formation_service.persona_service.quota_per_rank(rank=rank)
        if quota_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=quota_result.exception
                )
            )
        # On success just forward the quota_result to the caller.
        return quota_result
    
    @LoggingLevelRouter.monitor
    def number_of_rank_members(self, rank: Rank) -> CalculationResult[int]:
        """
        # ACTION:
            1.  Build the search-by-rank TokenContext. If the build fails send the exception in the InsertionResult.
                Else run the search.
            2.  If the search fails send the exception in the InsertionResult. Else the calculation was successful.
                Return the number of hits in the CalculationResult's payload.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   CalculationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   TokenDataServiceException
            *   RankCountCalculationFailedException
        """
        method = "TokenDataService.number_of_rank_members"
        
        # --- First step in getting rank count is building search-by-rank context. ---#
        build_result = self.token_context_service.builder.build(rank=rank)
        
        # Handle the case that the context build is not completed.
        if build_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=build_result.exception
                    )
                )
            )
        # --- Cast the context_build_result payload and run the search. ---#
        search_result = self.token_context_service.finder.find(context=cast(TokenContext, build_result.payload))
        
        # Handle the case that the search was not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=RankCountCalculationFailedException(
                        message=f"{method}: {RankCountCalculationFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that no tokens hold the rank
        if search_result.is_empty:
            return CalculationResult.success(payload=0)
        # Handle the case that some hits were found
        return CalculationResult.success(payload=len(cast(List[Token], search_result.payload)))
    
    @LoggingLevelRouter.monitor
    def insert_token(self, token: Token) -> InsertionResult[Token]:
        """
        # ACTION:
            1.  If the token is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   token (Token)
        # RETURNS:
            *   InsertionResult[Token] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenDataServiceException
        """
        method = "TokenDataService.add_token"
        
        # Handle the case that the token is unsafe.
        validation = self.token_service.validator.validate(candidate=token)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=TokenInsertionFailedException(
                        message=f"{method}: {TokenInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Token order is not required. Direct insertion into the dataset is simpler that a push. ---#
        self.items.append(token)
        
        # Handle the case that the token was not appended to the dataset.
        if token not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=TokenInsertionFailedException(
                        message=f"{method}: {TokenInsertionFailedException.ERROR_CODE}",
                        ex=AppendingTokenDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingTokenDirectlyIntoItemsFailedException.ERROR_CODE}"
                        )
                    )
                )
            )
        # On success return the token in the InsertionResult
        return InsertionResult.success(payload=token)
    
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
            *   TokenDataServiceException
        """
        method = "TokenDataService.delete_token_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
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
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=TokenDeletionFailedException(
                        message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                        ex=TokenDoesNotExistForRemovalException(
                            f"{method}: {TokenDoesNotExistForRemovalException.ERROR_CODE}"
                        )
                    )
                )
            )
        # --- Search the list for a token with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Token):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        TokenDataServiceException(
                            message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                            ex=TokenDeletionFailedException(
                                message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Token, got {type(item).__name__} "
                                    f"instead of a Token."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted token in the DeletionResult. ---#
                token = cast(Token, item)
                self.items.remove(token)
                return DeletionResult.success(payload=token)
            
            # If none of the items had that id return an empty DeletionResult.
            return DeletionResult.empty()
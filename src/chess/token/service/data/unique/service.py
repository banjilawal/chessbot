# src/chess/occupant/service/data/unique/service.py

"""
Module: chess.occupant.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List

from chess.rank import Rank
from chess.system.data.result import ComputationResult
from chess.token import (
    AddingDuplicateTokenException, ExhaustiveTokenDeletionFailedException, Token, TokenContext, TokenContextService,
    TokenDataService, TokenService, UniqueTokenDataServiceException, UniqueTokenInsertionFailedException,
    UniqueTokenSearchFailedException
)
from chess.system import (
    DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, SearchResult, UniqueDataService, id_emitter
)


class UniqueTokenDataService(UniqueDataService[Token]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items in managed by TokenDataService are unique.
    2.  Guarantee consistency of records in TokenDataService.

    # PARENT:
        *   UniqueDataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    SERVICE_NAME = "UniqueTokenDataService"
    _token_data_service: TokenDataService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: TokenDataService = TokenDataService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (TokenDataService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._token_data_service = data_service
    
    @property
    def integrity_service(self) -> TokenService:
        return self._token_data_service.token_service
    
    @property
    def context_service(self) -> TokenContextService:
        return self._token_data_service.context_service
    
    @property
    def size(self) -> int:
        return self._token_data_service.size
    
    @property
    def is_full(self) -> bool:
        return self._token_data_service.is_full
    
    @property
    def is_empty(self) -> bool:
        return self._token_data_service.is_empty
    
    @LoggingLevelRouter
    def open_rank_slots(self, rank: Rank) -> ComputationResult[int]:
        lookup_result = self._token_data_service.count_rank_openings(rank=rank)
        if lookup_result.is_failure:
            return ComputationResult.failure(lookup_result.exception)
        return lookup_result.payload
    
    @LoggingLevelRouter.monitor
    def rank_has_openings(self, rank: Rank) -> ComputationResult[bool]:
        answer = self._token_data_service.count_rank_openings(rank=rank)
        if answer.is_failure:
            return ComputationResult.failure(answer.exception)
        return answer
    
    @LoggingLevelRouter.monitor
    def lookup_team_rank_quote(self, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  If the rank fails its integrity checks send an exception in the ComputationResult..
            2.  If the calculation fails wrap the exception chain and send in the ComputationResult.
                Else directly forward the ComputationResult to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   UniqueTokenDataServiceException
        """
        method = "UniqueTokenDataService.token_rank_quota"
        
        # --- Handoff the calculation responsibility to _token_data_service. ---#
        quota_result = self._token_data_service.team_max_tokens_per_rank(rank)
        
        
        # Handle the case that the quota lookup was not completed.
        if quota_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=quota_result.exception
                )
            )
        # --- Forward the quota_result to the caller on success. ---#
        return quota_result
        
    
    @LoggingLevelRouter.monitor
    def rank_count(self, rank: Rank) -> ComputationResult[int]:
        """
        # ACTION:
            1.  Get the result of calling _token_data_service.number_of_rank_members.
            2.  If the calculation fails wrap the exception chain and send in the ComputationResult.
                Else directly forward the ComputationResult to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   ComputationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   UniqueTokenDataServiceException
        """
        method = "UniqueTokenDataService.rank_count"
    
        # --- Handoff the calculation responsibility to _token_data_service. ---#
        calculation_result = self._token_data_service.number_of_rank_members(rank=rank)
        
        # Handle the case that the calculation was not completed.
        if calculation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        # --- For either a successful calculation result directly forward to the caller. ---#
        return calculation_result
        
    
    @LoggingLevelRouter.monitor
    def remove_token(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  Get the result of calling _token_data_service.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate UniqueDataService exceptions and send the exception chain
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
            *   UniqueTokenDataServiceException
            *   ExhaustiveTokenDeletionFailedException
        """
        method = "UniqueTokenDataService.remove_token"
        
        # --- Handoff the deletion responsibility to _token_data_service. ---#
        deletion_result = self._token_data_service.delete_token_by_id(id=id, identity_service=identity_service)
        
        # Handle the case that the deletion was not completed.
        if deletion_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=ExhaustiveTokenDeletionFailedException(
                        message=f"{method}: {ExhaustiveTokenDeletionFailedException.ERROR_CODE}",
                        ex=deletion_result.exception)
                )
            )
        # --- For either a successful or null deletion result directly forward to the caller. ---#
        return deletion_result
   
    @LoggingLevelRouter.monitor
    def add_unique_token(self, token: Token) -> InsertionResult[Token]:
        """
        # ACTION:
            1.  If the square fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the square either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _token_data_service.insert_token fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   InsertionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
        # RAISES:
            *   UniqueTokenDataServiceException
            *   UniqueTokenInsertionFailedException
            *   UniqueTokenDataServiceException
        """
        method = "UniqueTokenDataService.add_unique_token"
        
        # --- To assure uniqueness the member_service has to conduct a search. The occupant should be validated first. ---#
        
        # Handle the case that the occupant is not certified safe.
        validation = self.integrity_service.validator.validate(candidate=token)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=UniqueTokenInsertionFailedException(
                        message=f"{method}: {UniqueTokenInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the occupant is already in the dataset.
        if token in self._token_data_service.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=UniqueTokenInsertionFailedException(
                        message=f"{method}: {UniqueTokenInsertionFailedException.ERROR_CODE}",
                        ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Use _token_data_service.insert_token because order does not matter for the occupant access. ---#
        insertion_result = self._token_data_service.insert_token(token=token)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=UniqueTokenInsertionFailedException(
                        message=f"{method}: {UniqueTokenInsertionFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_tokens(self, context: TokenContext) -> SearchResult[List[Token]]:
        """
        # ACTION:
            1.  Get the result of calling _token_data_service.delete_token_by_id for method. If the deletion failed
                wrap the exception inside the appropriate UniqueDataService exceptions and send the exception chain
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
            *   UniqueTokenDataServiceException
            *   ExhaustiveTokenDeletionFailedException
        """
        method = "UniqueTokenDataService.search_tokens"
        
        # --- Handoff the search responsibility to _token_data_service. ---#
        search_result = self._token_data_service.token_context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=UniqueTokenSearchFailedException(
                        message=f"{method}: {UniqueTokenSearchFailedException.ERROR_CODE}",
                        ex=search_result.exception)
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
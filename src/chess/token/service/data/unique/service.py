# src/chess/token/service/data/unique/service.py

"""
Module: chess.token.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List

from chess.rank import Rank, RankService
from chess.system.data.result.calculation import CalculationResult
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
    def is_empty(self) -> bool:
        return self._token_data_service.is_empty
    
    @LoggingLevelRouter.monitor
    def token_rank_quota(self, rank: Rank, rank_service: RankService = RankService()) -> CalculationResult[int]:
        """
        # ACTION:
            1.  If the rank fails its integrity checks send an exception in the CalculationResult..
            2.  If the calculation fails wrap the exception chain and send in the CalculationResult.
                Else directly forward the CalculationResult to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   CalculationResult[int] containing either:
                    - On failure: Exception.
                    - On success: int in the payload.
        # RAISES:
            *   UniqueTokenDataServiceException
        """
        method = "UniqueTokenDataService.token_rank_quota"
    
        # Handle the case that the rank is not certified safe.
        validation_result = rank_service.validator.validate(candidate=rank)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return CalculationResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=calculation_result.exception
                )
            )
        
    
    @LoggingLevelRouter.monitor
    def rank_count(self, rank: Rank) -> CalculationResult[int]:
        """
        # ACTION:
            1.  Get the result of calling _token_data_service.number_of_rank_members.
            2.  If the calculation fails wrap the exception chain and send in the CalculationResult.
                Else directly forward the CalculationResult to the caller.
        # PARAMETERS:
            *   rank (Rank)
        # RETURNS:
            *   CalculationResult[int] containing either:
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
            return CalculationResult.failure(
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
            *   token (Token)
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
        
        # --- To assure uniqueness the member_service has to conduct a search. The token should be validated first. ---#
        
        # Handle the case that the token is not certified safe.
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
        # --- Check if the token is already in the dataset before adding it. ---#
        search_result = self.search_tokens(context=TokenContext(id=token.id))
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=UniqueTokenInsertionFailedException(
                        message=f"{method}: {UniqueTokenInsertionFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the token is already in the dataset.
        if search_result.is_success:
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
        # --- Use _token_data_service.insert_token because order does not matter for the token access. ---#
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
# src/chess/token/service/data/unique/service.py

"""
Module: chess.token.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, Optional

from chess.token import (
    AddingDuplicateTokenException, Token, TokenContext, TokenContextService, TokenDataService, TokenService,
    UniqueTokenDataServiceException
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
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   data_service (TokenDataService): = TokenDataService()
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
    def remove_token_by_designation(
            self,
            designation: str,
            identity_service: IdentityService = IdentityService(),
    ) -> DeletionResult[Token]:
        method = "UniqueTokenDataService.remove_token_by_designation"
        deletion_result = self._token_data_service.delete_by_designation(designation, identity_service)
        if deletion_result.is_failure:
            return DeletionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        return DeletionResult.success(deletion_result.payload)
    
    @LoggingLevelRouter.monitor
    def remove_token(
            self,
            id: Optional[int] = None,
            designation: Optional[str] = None,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        method = "UniqueTokenDataService.remove_token"
        
        context_build = self.context_service.build(id=id, designation=designation, identity_service=identity_service)
        if context_build.is_failure:
            return DeletionResult.failure(
                UniqueTokenDataServiceException()
            )
        deletion_result = self._token_data_service.delete_by_id(id, identity_service)
        if deletion_result.is_failure:
            return DeletionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=deletion_result.exception
                )
            )
        return DeletionResult.success(deletion_result.payload)
   
    @LoggingLevelRouter.monitor
    def add_token(self, token: Token) -> InsertionResult[Token]:
        method = "UniqueTokenDataService.add_token"
        # Handle the case that the token is not safe.
        validation = self.token_service.validator.validate(candidate=token)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        
        # --- Check if the token is already in the dataset before adding it. ---#
        
        search_result = self.search_tokens(context=TokenContext(id=token.id))
        # Handle the case that the search fails
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Handle the case that the token is already in the dataset.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
                )
            )
        # The token is not in the dataset it can be added.
        insertion_result = self._token_data_service.add_token(token=token)
        
        result = self.push_unique_item(token)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the InsertionResult.
            return SearchResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def undo_add_token(self) -> DeletionResult[Token]:
        method = "UniqueTokenDataService.undo_add_token"
        result = self.data_service.undo_item_push()
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the DeletionResult.
            return SearchResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
    
    @LoggingLevelRouter.monitor
    def search_tokens(self, context: TokenContext) -> SearchResult[List[Token]]:
        method = "UniqueTokenDataService.search_tokens"
        result = self.data_service.search(context)
        if result.is_failure:
            # Handle the failure case by wrapping the debugging exception then sending in the SearchResult.
            return SearchResult.failure(
                UniqueTokenDataServiceException(
                    message=f"ServiceID:{self.id} {method}: {UniqueTokenDataServiceException.ERROR_CODE}",
                    ex=result.exception
                )
            )
        # On a successful search directly return the result.
        return result
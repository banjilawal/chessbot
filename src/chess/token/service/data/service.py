# src/chess/token/service/data/service_.py

"""
Module: chess.token.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, Optional, cast

from chess.system import (
    DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter,
    SearchResult, id_emitter
)
from chess.token import (
    Token, TokenContext, TokenDataServiceException, TokenDoesNotExistForRemovalException,
    TokenService, TokenContextService
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
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Token] = List[Token],
            service: TokenService = TokenService(),
            context_service: TokenContextService = TokenContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   items (List[Team])
            *   service (TeamService)
            *   context_service (TeamContextService)
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
            entity_service=service,
            context_service=context_service,
        )
        
    @property
    def token_service(self) -> TokenService:
        return cast(TokenService, self.entity_service)
    
    @property
    def token_context_service(self) -> TokenContextService:
        return cast(TokenContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def add_token(self, token: Token) -> InsertionResult[Token]:
        """
        # ACTION:
            1.  If the token is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
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
                    ex=validation.exception
                )
            )
        
        push_result = self.push_item(item=token)
        # Handle the case that super().push_item fails
        if push_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=push_result.exception
                )
            )
        # On success cast the payload and return to the caller in an insertion result.
        return push_result
    
    @LoggingLevelRouter.monitor
    def delete_token_by_id(self, id: int, identity_service: IdentityService = IdentityService()) -> DeletionResult[Token]:
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
        method = "TokenDataService.remove_token_by_id"
        
        # Handle the case of an unsafe id.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                TokenDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
                    ex=TokenDeletionFailedException(
                        message=f"{method}: {TokenDeletionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        for item in self.items:
            if item.id == id:
                token = cast(Token, item)
                self.items.remove(token)
                return DeletionResult.success(payload=token)
        return DeletionResult.nothing()
    #
    #
    # @LoggingLevelRouter.monitor
    # def delete_by_designation(
    #         self,
    #         designation: str,
    #         identity_service: IdentityService = IdentityService()
    # ) -> DeletionResult[Token]:
    #     """
    #     # ACTION:
    #         1.  If the designation is not certified safe send the exception in the DeletionResult. Else, call
    #             _delete_tokens_by_search_result with the outcome of an id search.
    #         2.  Forward the DeletionResult from _delete_tokens_by_search_result to the deletion client.
    #     # PARAMETERS:
    #                 *   designation (str)
    #                 *   identity_service (IdentityService)
    #     # RETURNS:
    #         *   InsertionResult[Token] containing either:
    #                 - On failure: Exception.
    #                 - On success: Token in the payload.
    #     # RAISES:
    #         *   TokenDataServiceException
    #     """
    #     method = "TokenDataService.remove_token_by_designation"
    #
    #     # Handle the case of an unsafe designation.
    #     validation = identity_service.validate_name(candidate=designation)
    #     if validation.is_failure:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             TokenDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
    #                 ex=validation.exception
    #             )
    #         )
    #     # # Pass the results of a designation search to the deletion helper.
    #     search_result = self.token_context_service.finder.find(context=TokenContext(designation=designation))
    #     return self._delete_tokens_by_search_result(search_result=search_result)
    #
    # @LoggingLevelRouter.monitor
    # def _delete_tokens_by_search_result(self, search_result: SearchResult) -> DeletionResult[Token]:
    #     """
    #     # ACTION:
    #         1.  If the search_result param is a failure send the exception in the DeletionResult.
    #         2.  If the search_result param is empty there is nothing to delete, send the exception in the
    #             DeletionResult.
    #         3.  If the search_result was a success delete all copies of the target in from the dataset then,
    #             send the deleted item in the DeletionResult.
    #     # PARAMETERS:
    #                 *   search_result (SearchResult[Token])
    #     # RETURNS:
    #         *   DeletionResult[Token] containing either:
    #                 - On failure: Exception.
    #                 - On success: Token in the payload.
    #     # RAISES:
    #         *   TokenDataServiceException
    #         8   TokenDoesNotExistForRemovalException
    #     """
    #     method = "TokenDataService._delete_tokens_by_search_result"
    #
    #     # Handle the case that the search fails
    #     if search_result.is_failure:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             TokenDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
    #                 ex=search_result.exception
    #             )
    #         )
    #     # Handle the case that token does not exist in the dataset.
    #     if search_result.is_empty:
    #         # Return the exception chain on failure.
    #         return DeletionResult.failure(
    #             TokenDataServiceException(
    #                 message=f"ServiceId:{self.id}, {method}: {TokenDataServiceException.ERROR_CODE}",
    #                 ex=TokenDoesNotExistForRemovalException(
    #                     f"{method}: {TokenDoesNotExistForRemovalException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )
    #     # Cast the payload to the array of matches, Then remove all occurrences in a loop
    #     matches = cast(List[Token], search_result.payload)
    #     token_removed = matches[0]
    #     # Python remove is not exhaustive hence the loop.
    #     for token in matches:
    #         self.items.remove(token)
    #     # Send the token_removed in the DeletionResult to confirm success.
    #     return DeletionResult.success(payload=token_removed)
        
        
        
        
        
            
        
        



# src/chess/token/service/data/service_.py

"""
Module: chess.token.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import (
    DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
)
from chess.token import (
    AppendingTokenDirectlyIntoItemsFailedException, PoppingEmptyTokenStackException, Token, TokenDataServiceException,
    TokenDoesNotExistForRemovalException, TokenService, TokenContextService, TokenDeletionFailedException,
    TokenInsertionFailedException
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
        # On success return the toke in the InsertionResult
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
            return DeletionResult.nothing()
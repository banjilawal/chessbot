# src/chess/square/database/service.py

"""
Module: chess.square.database.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from chess.square import (
    AddingDuplicateSquareException, AddingSquareOccupantException, DeleteTokenBySearchFailedException,
    InsertingSquareInDatabaseFailedException, Square, SquareContext, SquareContextService, SquareStack, SquareService,
    FullSquareStackException, SquareDatabaseException, SquareToOccupyNotFoundException
)

from chess.system import (
    IdFactory, NUMBER_OF_COLUMNS, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, NUMBER_OF_ROWS,
    SearchResult,
    Database, id_emitter
)
from chess.token import Token, TokenService


class SquareDatabase(Database[Square]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by SquareStack are unique.
    2.  Guarantee consistency of records in SquareStack.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "SquareDatabase"
    _stack_service: SquareStack
    _token_map: [Token, Square]
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SquareDatabase"),
            data_service: SquareStack = SquareStack(capacity=NUMBER_OF_ROWS * NUMBER_OF_COLUMNS),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (SquareStack)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._square_stack_service = data_service
        self._token_map = {}
    
    @property
    def integrity_service(self) -> SquareService:
        return self._stack_service.integrity_service
    
    @property
    def context_service(self) -> SquareContextService:
        return self._stack_service.context_service
    
    @property
    def size(self) -> int:
        return self._stack_service.size
    
    @property
    def max_capacity(self) -> int:
        return self._stack_service.capacity
    
    @property
    def is_full(self) -> bool:
        return self._stack_service.is_full
    
    @property
    def is_empty(self) -> bool:
        return self._stack_service.is_empty
    
    @property
    def token_map(self) -> dict[Token, Square]:
        return self._token_map
    
    @LoggingLevelRouter.monitor
    def add_occupant_to_square(
            self,
            token: Token,
            square: Square,
            token_service: TokenService = TokenService()
    ) -> InsertionResult:
        """
        # ACTION:
            1.  If token_service cannot verify the occupation candidate is actionable send the wrapped exception
                in the InsertionResult.
            2.  If the square either:
                    *   Fails validation.
                    *   Searching for it in the database raises an error.
                    *   The square is not in the database.
                send the wrapped exception in the InsertionResult.
            3.  If the occupation fails send the wrapped exception in the InsertionResult.
            4.  Add an entry for the occupant in the token_map then send the success InsertionResult.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
            *   token_service (TokenService)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        # RAISES:
            *   SquareDatabaseException
            *   SquareToOccupyNotFoundException
            *   AddingSquareOccupantException
        """
        method = "SquareDatabase.add_occupant_to_square"
        
        # Handle the case that the token is not active
        actionable_token_validation = token_service.verify_access_token(token)
        if actionable_token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=actionable_token_validation.exception
                    )
                )
            )
        # Handle the case that the target square is not certified safe.
        square_validation = self.integrity_service.validator.validate(square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the target square is not in the database
        square_search_result = self._stack_service.context_service.finder.find(
            context=SquareContext(id=square.id)
        )
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=square_search_result.exception
                    )
                )
            )
        # Handle the case that the item does not square in the database
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=SquareToOccupyNotFoundException(
                            f"{method}: {SquareToOccupyNotFoundException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the occupation fails.
        insertion_result = self.integrity_service.add_occupant_to_square(square, token)
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantException(
                        message=f"{method}: {AddingSquareOccupantException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- Update the token map and send the success result. ---#
        self._token_map[token] = square
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_occupant_by_search(self, occupant: Token) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  If the search handler cannot certify the occupant is a valid token the exception chain will include.
                TokenVerificationFailedException.
            2.  If the token is not found in any of the squares send a nothing_to_delete result.
            3.  If the token was found in a square but the removal failed send the wrapped exception in the
                DeletionResult.
            4.  When the token is successfully removed from the square remove its entry from the token_map then
                send the ejected token in the DeletionResult.
        # PARAMETERS:
            *   occupant (Token)
        # RETURN:
            *   DeletionResult[Token] containing either:
                    - On failure: An exception.
                    - On success: Token in payload.
                    - On occupant not found: Empty DeletionResult.
        # RAISES:
            *   SquareDatabaseException
            *   DeleteTokenBySearchFailedException
        """
        method = "SquareService.empty_square_by_token_search"
        
        search_result = self.search(context=SquareContext(occupant=occupant))
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=DeleteTokenBySearchFailedException(
                        message=f"{method}: {DeleteTokenBySearchFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that the search target was not found.
        if search_result.is_empty:
            return DeletionResult.nothing_to_delete()
        
        for square in search_result.payload:
            deletion_result = self.integrity_service.remove_occupant(square)
            
            # Handle the case that removing the occupant does not succeed.
            if deletion_result.is_failure:
                # Return the exception chain on failure.
                return DeletionResult.failure(
                    SquareDatabaseException(
                        message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                        ex=DeleteTokenBySearchFailedException(
                            message=f"{method}: {DeleteTokenBySearchFailedException.ERROR_CODE}",
                            ex=search_result.exception
                        )
                    )
                )
            # --- Update the token map then send the ejected occupant in the DeletionResult ---#
            self._token_map.pop(occupant)
            return DeletionResult.success(payload=occupant)
    
    @LoggingLevelRouter.monitor
    def insert_square(self, square: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the item either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _stack_service.insert_square fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   item (Square)
        # RETURN:
            *   InsertionResult[Square] containing either:
                    - On failure: An exception.
                    - On success: Square in payload.
        # RAISES:
            *   SquareDatabaseException
            *   InsertingSquareInDatabaseFailedException
        """
        method = "SquareDatabase.insert_square"
        
        # Handle the case that the service cannot manage anymore squares.
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=InsertingSquareInDatabaseFailedException(
                        message=f"{method}: {InsertingSquareInDatabaseFailedException.ERROR_CODE}",
                        ex=FullSquareStackException(
                            f"{method}: {FullSquareStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        
        # --- To assure uniqueness the member_service has to conduct a search. The item should be validated first. ---#
        
        # Handle the case that the item is not certified safe.
        validation = self.integrity_service.validator.validate(candidate=square)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=Squ(
                        message=f"{method}: {InsertingSquareInDatabaseFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the item is already in the dataset.
        if square in self._stack_service.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=InsertingSquareInDatabaseFailedException(
                        message=f"{method}: {InsertingSquareInDatabaseFailedException.ERROR_CODE}",
                        ex=AddingDuplicateSquareException(f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Use _stack_service.insert_square because order does not matter for the item access. ---#
        
        insertion_result = self._stack_service.push(square=square)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=InsertingSquareInDatabaseFailedException(
                        message=f"{method}: {InsertingSquareInDatabaseFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: SquareContext) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Pass the context param to stack_service.context_service manages all error handling and operations in
                search lifecycle.
            2.  Any failures stack_service.context_service will be encapsulated inside a SquareDatabaseException
                which is sent inside a SearchResult.
            3.  If the search completes successfully the result can be sent directly because it will contain the
                payload.
        # PARAMETERS:
            *   context (SquareContext)
        # RETURN:
            *   SearchResult[Square] containing either:
                    - On failure: An exception.
                    - On success: List[Square] in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.search"
        
        # --- Handoff the search responsibility to _stack_service. ---#
        search_result = self._stack_service.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
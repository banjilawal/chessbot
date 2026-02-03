# src/chess/square/database/service.py

"""
Module: chess.square.database.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from chess.square import (
    AddingDuplicateSquareException, AddingSquareOccupantFailedException, DeleteTokenBySearchFailedException, Square,
    SquareContext,
    SquareContextService,
    SquareStackService, SquareService, FullSquareStackException, SquareDatabaseException,
    SquareToOccupyNotFoundException, UniqueSquareInsertionFailedException,
    UniqueSquareSearchFailedException
)
from chess.square.state import SquareState
from chess.system import (
    NUMBER_OF_COLUMNS, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, NUMBER_OF_ROWS, SearchResult,
    Database,
    id_emitter
)
from chess.token import Token, TokenService


class SquareDatabase(Database[Square]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag in managed by SquareStackService are unique.
    2.  Guarantee consistency of records in SquareStackService.

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
    _square_database_core: SquareStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: SquareStackService = SquareStackService(capacity=NUMBER_OF_ROWS * NUMBER_OF_COLUMNS),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   member_service (SquareStackService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._square_stack_service = data_service
    
    @property
    def integrity_service(self) -> SquareService:
        return self._square_database_core.integrity_service
    
    @property
    def context_service(self) -> SquareContextService:
        return self._square_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._square_database_core.size
    
    @property
    def max_capacity(self) -> int:
        return self._square_database_core.capacity
    
    @property
    def is_full(self) -> bool:
        return self._square_database_core.is_full
    
    @property
    def is_empty(self) -> bool:
        return self._square_database_core.is_empty
    
    @LoggingLevelRouter.monitor
    def add_occupant_to_square(
            self,
            square: Square,
            token: Token,
            token_service: TokenService = TokenService()
    ) -> InsertionResult:
        method = "SquareDatabase.add_occupant_to_square"
        
        # Handle the case that the is not active
        actionable_token_validation = token_service.verify_access_token(token)
        if actionable_token_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=actionable_token_validation.exception
                    )
                )
            )
        
        # Handle the case that the item is not certified safe.
        square_validation = self.integrity_service.validator.validate(square)
        if square_validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=square_validation.exception
                    )
                )
            )
        # Handle the case that the item is not in the database
        square_search_result = self._square_database_core.context_service.finder.find(
            context=SquareContext(id=square.id)
        )
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=square_search_result.exception
                    )
                )
            )
        # Handle the case that the item does not exist in the database
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
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
                    ex=AddingSquareOccupantFailedException(
                        message=f"{method}: {AddingSquareOccupantFailedException.ERROR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_occupant_by_search(self, occupant: Token) -> DeletionResult[Token]:
        """
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
            
            # --- The token has bee completely removed from the dataset. ---#
            return DeletionResult.success(payload=occupant)
    
    @LoggingLevelRouter.monitor
    def add_unique_square(self, square: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the item fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the item either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _square_database_core.insert_square fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   item (Square)
        # RETURN:
            *   InsertionResult[Square] containing either:
                    - On failure: An exception.
                    - On success: Square in payload.
        # RAISES:
            *   SquareDatabaseException
            *   UniqueSquareInsertionFailedException
            *   SquareDatabaseException
        """
        method = "SquareDatabase.add_unique_square"
        
        # Handle the case that the service cannot manage anymore squares.
        if self.is_full:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
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
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the item is already in the dataset.
        if square in self._square_database_core.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
                        ex=AddingDuplicateSquareException(f"{method}: {AddingDuplicateSquareException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # --- Use _square_database_core.insert_square because order does not matter for the item access. ---#
        
        insertion_result = self._square_database_core.push(square=square)
        
        # Handle the case that the insertion is not completed.
        if insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceId:{self.id}, {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=UniqueSquareInsertionFailedException(
                        message=f"{method}: {UniqueSquareInsertionFailedException.ERROR_CODE}",
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
            1.  Get the result of calling _square_database_core.delete_square_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Square] containing either:
                    - On failure: A                self._stack.remove(square)n exception.
                    - On success: Square in payload.
                    - On Empty: No payload nor exception.
        # RAISES:
            *   SquareDatabaseException
            *   DeleteTokenBySearchFailedException
        """
        method = "SquareDatabase.search_squares"
        
        # --- Handoff the search responsibility to _square_database_core. ---#
        search_result = self._square_database_core.context_service.finder.find(context=context)
        
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=UniqueSquareSearchFailedException(
                        message=f"{method}: {UniqueSquareSearchFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
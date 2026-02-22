# src/chess/square/database/service.py

"""
Module: chess.square.database.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import List, cast

from chess.square import (
    AddingDuplicateSquareException, AddingSquareOccupantException, DeleteTokenBySearchException,
    InsertingSquareInDatabaseFailedException, Square, SquareContext, SquareContextService, SquareStackService, SquareService,
    SquareStackFullException, SquareDatabaseException, SquareToOccupyNotFoundException
)

from chess.system import (
    IdFactory, NUMBER_OF_COLUMNS, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, NUMBER_OF_ROWS,
    SearchResult,
    Database, UpdateResult, id_emitter
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
    _token_map: [Token, Square]
    _stack_service: SquareStackService

    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="SquareDatabase"),
            stack_service: SquareStackService = SquareStackService(capacity=NUMBER_OF_ROWS * NUMBER_OF_COLUMNS),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   stack_service (SquareStackService)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, data_service=stack_service)
        self._token_map = {}
        self._stack_service = stack_service

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
    def add_occupant_to_square(self,token: Token, square: Square,) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  Handoff validation and occupation responsibility to stack_service.util.occupation_service.
            2.  If occupation_service fails, wrap the exception in SquareDatabaseException then send in
                the UpdateResult.
            3.  If occupation_service succeeds, update token_map with the with its new square.
            4.  Forward the update_result to the client.
        # PARAMETERS:
            *   token (Token)
            *   square (Square)
        # RETURN:
            *   UpdateResult[Square]
        # RAISES:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.add_occupant_to_square"
        
        # --- Handoff the responsibility for the occupation to stack_service. ---#
        occupation_update_result = self._stack_service.util.occupation_service.add_occupant(
            square=square,
            token=token
        )
        # Handle the case that, the occupation was aborted.
        if occupation_update_result.is_failure:
            # Encapsulate original and exception from occupation_update_result in a
            # SquareDatabaseException chain then, send to client in new UpdateResult.
            return UpdateResult.update_failure(
                original=occupation_update_result.original,
                exception=SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=occupation_update_result.exception
                )
            )
        # update the token_map with the token's current location.
        self._token_map[token] = square
        
        # --- Forward the success result to the client. ---#
        return occupation_update_result
    
    @LoggingLevelRouter.monitor
    def remove_occupant_by_search(self, occupant: Token) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  Handoff validation and eviction responsibility to stack_service.util.remove_occupant_by_search.
            2.  If occupation_service fails, wrap the exception in SquareDatabaseException then send in
                the DeletionResult.
            3.  If occupation_service succeeds, if the token exists in token_map remove it.
            4.  Forward the deletion_result to the client.
        # PARAMETERS:
            *   token (Token)
        # RETURN:
            *   DeletionResult[Square]
        # RAISES:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.remove_occupant_by_search"
        
        # --- Handoff eviction responsibility to stack_service. ---#
        occupant_removal_result = self._stack_service.util.occupation_service.remove_occupant_by_search(
            token=occupant
        )
        # Handle the case that, the eviction was aborted.
        if occupant_removal_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=occupant_removal_result.exception
                )
            )
        # Remove the token from the map, if it exists.
        if occupant in self._token_map.keys():
            self._token_map.pop(occupant)
        
        # --- Forward the success result to the client. ---#
        return occupant_removal_result
    
    @LoggingLevelRouter.monitor
    def insert_square(self, square: Square) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  Handoff validation and insertion responsibility to stack_service.
            2.  If stack_service fails, wrap the exception in SquareDatabaseException then send in the InsertionResult.
            3.  If insertion succeeds forward the insertion_result to the client.
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   InsertionResult
        # RAISES:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.insert_square"
        
        # --- Handoff square insertion responsibility to stack_service. ---#
        square_insertion_result = self._stack_service.push(square=square)
        
        # Handle the case that, the square insertion was aborted.
        if square_insertion_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=square_insertion_result.exception
                )
            )
        # --- Forward the success result to the client. ---#
        return square_insertion_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: SquareContext) -> SearchResult[List[Square]]:
        """
        # ACTION:
            1.  Handoff validation and search responsibility to stack_service.
            2.  If stack_service fails, wrap the exception in SquareDatabaseException then send in the SearchResult.
            3.  Forward the search_result to the client.
        # PARAMETERS:
            *   context (SquareContext)
        # RETURN:
            *   SearchResult
        # RAISES:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.search"
        
        # --- Handoff square insertion responsibility to stack_service. ---#
        query_result = self._stack_service.query(context=context)
        
        # Handle the case that, the query was aborted.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                SquareDatabaseException(
                    message=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERROR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- Forward the success result to the client. ---#
        return query_result
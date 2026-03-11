# src/logic/square/database/service.py

"""
Module: logic.square.database.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Dict, List, Optional

from logic.square import Square, SquareContextService, SquareService, SquareStackService
from logic.system import Database, IdFactory, LoggingLevelRouter, UpdateResult
from logic.system.database.database import T
from logic.token import Token, TokenService


class SquareDatabase(Database[Square]):
    """
    # ROLE: Data Repository, CRUD Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Higher level API for SquareStackService.
    2.  ACID service provider for SquareStackService.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   token_map Dict[Toke, Square]
        *   stack_service (SquareStackService)

    # INHERITED ATTRIBUTES:
        *   See Database for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   stack_service (StackService)
        Inherited:
            *   See Database for inherited parameters.
            
    # LOCAL METHODS:
        *   add_occupant_to_square(token: Token, square: Square) -> UpdateResult[Square]
        *   remove_occupant_by_search(occupant: Token) -> DeletionResult[Token]
        *   insert_square(square: Square) -> InsertionResult[bool]
        *   search(context: SquareContext) -> SearchResult[List[Square]]

    # INHERITED METHODS:
    None
    """
    SERVICE_NAME = "SquareDatabase"
    _token_map: Dict[Token, Square]
    _stack_service: SquareStackService

    def __init__(
            self,
            stack_service: SquareStackService,
            id: int = IdFactory.next_id(class_name="SquareDatabase"),
            name: str = SERVICE_NAME,
    ):
        """
        Args:
            id: int
            name: str
            stack_service: SquareStackService
        """
        super().__init__(id=id, name=name)
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
    
    @property
    def current_item(self) -> Optional[Square]:
        return self._stack_service.current_item
    
    @LoggingLevelRouter.monitor
    def add_occupant_to_square(
            self,
            token: Token,
            square: Square,
            token_service:TokenService = TokenService(),
        ) -> UpdateResult[Square]:
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
        Raises:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.add_occupant_to_square"
        
        # --- Handoff the responsibility for the occupation to stack_service. ---#
        occupation_update_result = self._stack_service.handler.token.occupy_stack_square(
            token=token,
            square=square,
            token_service=token_service,
        )
        # Handle the case that, the occupation was aborted.
        if occupation_update_result.is_failure:
            # Encapsulate occupation_update_result.{original, exception} in exception chain returned on failure.
            return UpdateResult.update_failure(
                original=occupation_update_result.original,
                exception=SquareDatabaseException(
                    msg=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERR_CODE}",
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
            *   DeletionResult[Token]
        Raises:
            *   SquareDatabaseException
        """
        method = "SquareDatabase.remove_occupant_by_search"
        
        # --- Handoff eviction responsibility to stack_service. ---#
        occupant_removal_result = self._stack_service.util.occupation_service.remove_occupant_from_stack(
            token=occupant
        )
        # Handle the case that, the eviction was aborted.
        if occupant_removal_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareDatabaseException(
                    msg=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERR_CODE}",
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
        Raises:
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
                    msg=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERR_CODE}",
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
        Raises:
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
                    msg=f"ServiceID:{self.id} {method}: {SquareDatabaseException.ERR_CODE}",
                    ex=query_result.exception
                )
            )
        # --- Forward the success result to the client. ---#
        return query_result
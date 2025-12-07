# src/chess/piece/service/data/service_.py

"""
Module: chess.piece.service.data.entity_service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.piece import Piece, PieceContext, PieceDataServiceException, PieceFinder, PieceService, PieceContextService


class PieceDataService(DataService[Piece]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Stack data structure for Piece objects with no guarantee of uniqueness.
    3.  Implements searcher, insert, delete, and update operations on Piece objects.
    4.  ContextService for building selecting different searcher attributes.
    5.  Including a PieceService instance creates a microservice for clients.

    # PROVIDES:
        *   PieceService
        *   ContextService
        *   Finder
        *   PieceStack data structure

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   items (List[Piece]):
        *   searcher (Finder[Piece]):
        *   entity_service (EntityService[Piece]):
        *   context_service (EntityService[PieceContext]);
        *   current_item (Piece):
        *   size (int):
    """
    DEFAULT_NAME = "PieceDataService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            items: List[Piece] = List[Piece],
            search: PieceFinder = PieceFinder(),
            service: PieceService = PieceService(),
            context_service: PieceContextService = PieceContextService(),
    ):
        """
        # Action
        1.  Use id_emitter to automatically generate a unique id for each PieceDataService instance.
        2.  Automatic dependency injection by providing working default instances of each attribute.
        """
        method = "PieceService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            search=search,
            entity_service=service,
            context_service=context_service,
        )
    
    @LoggingLevelRouter.monitor
    def push_item(self, item: Piece) -> InsertionResult[Piece]:
        """
        # ACTION:
        1.  Use PieceDataService.service.validator to certify item.
        2.  If certification fails return the exception inside an InsertionResult.
        3.  Otherwise, push item onto the stack.
        4.  Send the successfully pushed data back in an InsertionResult.

        # PARAMETERS:
            *   item (Piece)

        # Returns:
        InsertionResult[TPiece] containing either:
            - On success: Piece in the payload.
            - On failure: Exception.

        # Raises:
            *   PieceDataServiceException
        """
        method = "PieceDataService.push"
        
        try:
            validation = self.data.item_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                PieceDataServiceException(ex=ex, message=f"{method}: {PieceDataServiceException.DEFAULT_MESSAGE}")
            )


    @LoggingLevelRouter.monitor
    def search(self, context: PieceContext) -> SearchResult[List[Piece]]:
        """
        # ACTION:
        1.  Pass context argument to self.searcher.
        2.  Pass self.items and self.context_service.validator to self.searcher's renaming params.
        3.  The Finder object will return any exceptions if it fails, success otherwise.
        4.  Because Finder object does all the error using a try-catch is uneccesar
        
        2.  If certification fails return the exception inside an InsertionResult.
        3.  Otherwise, push item onto the stack.
        4.  Send the successfully pushed data back in an InsertionResult.

        # PARAMETERS:
            *   item (Piece)

        # Returns:
        SearchResult[List[Piece]] containing either:
            - On success: List[Piece] in the payload.
            - On failure: Exception.

        # Raises:
        None
        """
        method = "PieceDataService.searcher"
        
        return self.search.find(
            data_set=self.items, context=context, context_validator=self.context_service.item_validator
        )

# src/database/board/database.py

"""
Module: database.board.database
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from database import Database


class BoardDatabase(Database[Board]):
    """
    Role:
        _   Frontend
        -   Interface
        -   Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: Microservice[T]

    Provides:
        -   iterator() ->: iter
        -   insert(item: T) -> InsertionResult:
        -   delete_by_id(id: int) -> DeletionResult[T]:
        -   search(context: Context[T]) -> SearchResult[List[T]]

    Role:Unique Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Ensure all bag in managed by BoardStackService are unique.
    2.  Guarantee consistency of records in BoardStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "BoardDatabase"
    _board_database_core: BoardStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: BoardStackService = BoardStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (BoardStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._board_stack_service = data_service
    
    @property
    def microservice(self) -> BoardService:
        return self._board_database_core.board_service
    
    @property
    def context_service(self) -> BoardQueryService:
        return self._board_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._board_database_core.size
    
    @property
    def is_empty(self) -> bool:
        return self._board_database_core.is_empty
    
    @LoggingLevelRouter.monitor
    def add_unique_board(self, board: Board) -> InsertionResult[Board]:
        """
        # ACTION:
            1.  If the board fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the board either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _board_database_core.insert_board fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   board (Board)
        # RETURN:
            *   InsertionResult[Board] containing either:
                    - On failure: An exception.
                    - On success: Board in payload.
        Raises:
            *   BoardDatabaseException
            *   UniqueBoardInsertionException
            *   BoardDatabaseException
        """
        method = "BoardDatabase.add_unique_board"
        
        # --- To assure uniqueness the member_service has to conduct a search. The board should be validated first. ---#
        
        # Handle the case that, the boardis not safe.
        validation = self.microservice.validator.validate(candidate=board)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueBoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueBoardDataServiceException.ERR_CODE}",
                    ex=UniqueBoardInsertionException(
                        msg=f"{method}: {UniqueBoardInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the board is already in the collider_candidates before adding it. ---#
        search_result = self.search_boards(context=BoardContext(id=board.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueBoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueBoardDataServiceException.ERR_CODE}",
                    ex=UniqueBoardInsertionException(
                        msg=f"{method}: {UniqueBoardInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the board is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueBoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueBoardDataServiceException.ERR_CODE}",
                    ex=UniqueBoardInsertionException(
                        msg=f"{method}: {UniqueBoardInsertionException.ERR_CODE}",
                        ex=AddingDuplicateBoardException(f"{method}: {AddingDuplicateBoardException.MSG}")
                    )
                )
            )
        # --- Use _board_database_core.insert_board because order does not matter for the board access. ---#
        insertion_result = self._board_database_core.insert_board(board=board)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueBoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueBoardDataServiceException.ERR_CODE}",
                    ex=UniqueBoardInsertionException(
                        msg=f"{method}: {UniqueBoardInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_boards(self, context: BoardContext) -> SearchResult[List[Board]]:
        """
        # ACTION:
            1.  Get the result of calling _board_database_core.delete_board_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Board] containing either:
                    - On failure: An exception.
                    - On success: Board in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   BoardDatabaseException
            *   ExhaustiveBoardDeletionException
        """
        method = "BoardDatabase.search_boards"
        
        # --- Handoff the search responsibility to _board_database_core. ---#
        search_result = self._board_database_core.board_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueBoardDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueBoardDataServiceException.ERR_CODE}",
                    ex=UniqueBoardSearchException(
                        msg=f"{method}: {UniqueBoardSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result
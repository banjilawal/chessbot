# src/chess/board/service/data/service_.py

"""
Module: chess.board.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.arena import Arena
from chess.system import DataService, DeletionResult, IdentityService, InsertionResult, LoggingLevelRouter, id_emitter
from chess.board import (
    AppendingBoardDirectlyIntoItemsFailedException, ArenaAlreadyContainsBoardException, PoppingEmptyBoardStackException,
    Board, BoardContext,
    BoardDataServiceException, BoardDoesNotExistForRemovalException, BoardService, BoardContextService,
    BoardDeletionFailedException, BoardInsertionFailedException
)


class BoardDataService(DataService[Board]):
    """
    # ROLE: Data Stack, Searcher EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Microservice for managing Board objects and their lifecycles.
    3.  Ensure integrity of Board data stack
    4.  Stack data structure for Board objects with no guarantee of uniqueness.

    # PARENT:
        *   DataService[Board]

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "BoardDataService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Board] = List[Board],
            service: BoardService = BoardService(),
            context_service: BoardContextService = BoardContextService(),
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
        method = "BoardService.__init__"
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def board_service(self) -> BoardService:
        return cast(BoardService, self.entity_service)
    
    @property
    def board_context_service(self) -> BoardContextService:
        return cast(BoardContextService, self.context_service)
    
    @LoggingLevelRouter.monitor
    def insert_board(self, board: Board) -> InsertionResult[Board]:
        """
        # ACTION:
            1.  If the board is not validated send the exception in the InsertionResult. Else, call the super class
                push method.
            2.  If super().push_item fails send the exception in the InsertionResult. Else extract the payload to cast
                and return to the caller in the BuildResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   board (Board)
        # RETURNS:
            *   InsertionResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        # RAISES:
            *   BoardDataServiceException
        """
        method = "BoardDataService.add_board"
        
        # Handle the case that the board is unsafe.
        validation = self.board_service.validator.validate(candidate=board)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardInsertionFailedException(
                        message=f"{method}: {BoardInsertionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Check if an item in the list shares the board's arena. ---#
        search_result = self.board_context_service.finder.find(
            dataset=self.items,
            context=BoardContext(arena=board.arena)
        )
        # Handle the case that the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardInsertionFailedException(
                        message=f"{method}: {BoardInsertionFailedException.ERROR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that a board in collection has the same arena.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardInsertionFailedException(
                        message=f"{method}: {BoardInsertionFailedException.ERROR_CODE}",
                        ex=ArenaAlreadyContainsBoardException(
                            f"{method}: {ArenaAlreadyContainsBoardException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # --- Board order is not required. Direct insertion into the dataset is simpler that a push. ---#
        self.items.append(board)
        
        # Handle the case that the board was not appended to the dataset.
        if board not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardInsertionFailedException(
                        message=f"{method}: {BoardInsertionFailedException.ERROR_CODE}",
                        ex=AppendingBoardDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingBoardDirectlyIntoItemsFailedException.ERROR_CODE}"
                        )
                    )
                )
            )
        # On success return the board in the InsertionResult
        return InsertionResult.success(payload=board)
    
    @LoggingLevelRouter.monitor
    def delete_board_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Board]:
        """
        # ACTION:
            1.  If the id is not certified safe send the exception in the DeletionResult. Else, call
                _delete_boards_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_boards_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        # RAISES:
            *   BoardDataServiceException
        """
        method = "BoardDataService.delete_board_by_id"
        
        # Handle the case that there are no items in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardDeletionFailedException(
                        message=f"{method}: {BoardDeletionFailedException.ERROR_CODE}",
                        ex=PoppingEmptyBoardStackException(
                            f"{method}: {PoppingEmptyBoardStackException.DEFAULT_MESSAGE}"
                        )
                    )
                )
            )
        # Handle the case that the id is not certified safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                BoardDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                    ex=BoardDeletionFailedException(
                        message=f"{method}: {BoardDeletionFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for a board with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that the match is the wrong type.
                if not isinstance(item, Board):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        BoardDataServiceException(
                            message=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERROR_CODE}",
                            ex=BoardDeletionFailedException(
                                message=f"{method}: {BoardDeletionFailedException.ERROR_CODE}",
                                ex=TypeError(
                                    f"{method}: Could not cast deletion target to Board, got {type(item).__name__} "
                                    f"instead of a Board."
                                )
                            )
                        )
                    )
                # --- Cast the item before removal and return the deleted board in the DeletionResult. ---#
                board = cast(Board, item)
                self.items.remove(board)
                return DeletionResult.success(payload=board)
        
        # If none of the items had that id return an empty DeletionResult.
        return DeletionResult.empty()
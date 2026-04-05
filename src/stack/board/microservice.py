# src/microservice/stack/board/board.py

"""
Module: microservice.stack.board.board
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class BoardStackService(StackService[Board]):
    """
    Role:Data Stack, SearchRouter Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing API.
    2.  Microservice for managing Board objects and their lifecycles.
    3.  Ensure integrity of Board data schema
    4.  Stack data structure for Board objects with no guarantee of uniqueness.

    Super Class:
        *   StackService[Board]

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "BoardStackService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Board] = List[Board],
            service: BoardService = BoardService(),
            context_service: BoardQueryService = BoardQueryService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   bag (List[Team])
            *   service (TeamService)
            *   context_service (TeamQueryService)
        # RETURNS:
            None
        Raises:
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
    def board_context_service(self) -> BoardQueryService:
        return cast(BoardQueryService, self.context_service)
    
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
        Raises:
            *   BoardDataServiceException
        """
        method = "BoardStackService.add_board"
        
        # Handle the case that, the board is unsafe.
        validation = self.board_service.validator.validate(candidate=board)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardInsertionException(
                        msg=f"{method}: {BoardInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if an item in the list shares the board's arena. ---#
        search_result = self.board_context_service.finder.find(
            dataset=self.items,
            context=BoardContext(arena=board.arena)
        )
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardInsertionException(
                        msg=f"{method}: {BoardInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, a board in collection has the same arena.
        if search_result.is_success:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardInsertionException(
                        msg=f"{method}: {BoardInsertionException.ERR_CODE}",
                        ex=ArenaAlreadyContainsBoardException(
                            f"{method}: {ArenaAlreadyContainsBoardException.MSG}"
                        )
                    )
                )
            )
        # --- Board order is not required. Direct insertion into the collider_candidates is simpler that a push. ---#
        self.items.append(board)
        
        # Handle the case that, the board was not appended to the collider_candidates.
        if board not in self.items:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardInsertionException(
                        msg=f"{method}: {BoardInsertionException.ERR_CODE}",
                        ex=AppendingBoardDirectlyIntoItemsFailedException(
                            f"{method}: {AppendingBoardDirectlyIntoItemsFailedException.ERR_CODE}"
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
            1.  If the idis not safe send the exception in the DeletionResult. Else, call
                _delete_boards_by_search_result with the outcome of an id search.
            2.  Forward the DeletionResult from _delete_boards_by_search_result to the deletion client.
        # PARAMETERS:
                    *   id (int)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   InsertionResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        Raises:
            *   BoardDataServiceException
        """
        method = "BoardStackService.delete_board_by_id"
        
        # Handle the case that, there are no bag in the list.
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardDeletionException(
                        msg=f"{method}: {BoardDeletionException.ERR_CODE}",
                        ex=PoppingEmptyBoardStackException(
                            f"{method}: {PoppingEmptyBoardStackException.MSG}"
                        )
                    )
                )
            )
        # Handle the case that, the idis not safe.
        validation = identity_service.validate_id(candidate=id)
        if validation.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                BoardDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                    ex=BoardDeletionException(
                        msg=f"{method}: {BoardDeletionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- Search the list for a board with target id. ---#
        for item in self.items:
            if item.id == id:
                # Handle the case that, the match is the wrong type.
                if not isinstance(item, Board):
                    # Return the exception chain on failure.
                    return DeletionResult.failure(
                        BoardDataServiceException(
                            msg=f"ServiceId:{self.id}, {method}: {BoardDataServiceException.ERR_CODE}",
                            ex=BoardDeletionException(
                                msg=f"{method}: {BoardDeletionException.ERR_CODE}",
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
        
        # If none of the bag had that id return an empty DeletionResult.
        return DeletionResult.empty()
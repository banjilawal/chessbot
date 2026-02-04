# src/chess/coord/database/core/stack.py

"""
Module: chess.coord.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional, cast

from chess.coord.database.core.exception.push.duplicate import DuplicateCoordPushException
from chess.coord.database.core.exception.push.wrapper import PushingCoordFailedException
from chess.system import StackService, DeletionResult, InsertionResult, SearchResult, id_emitter
from chess.coord import (
    Coord, CoordContext, CoordDataServiceException, CoordService, CoordContextService, MaxConsecutiveCoordPopException,
    PoppingEmtpyCoordStackException
)


class CoordStackService(StackService[Coord]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching Coord collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Coords are put in the collection.
    4.  Assure updates do not break the integrity individual bag in the collection or
        the collection itself.
    5.  Provide Coord stack data structure with no guarantee of uniqueness.
    6.  Search utility.

    # PARENT:
        *   StackService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    SERVICE_NAME = "CoordStackService"
    
    _current_coord: Optional[Coord]
    _previous_coord: Optional[Coord]
    _stack: List[Coord]
    
    def service(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Coord] = List[Coord],
            service: CoordService = CoordService(),
            context_service: CoordContextService = CoordContextService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   bag (List[Coord]): = List[Coord]
            *   service (CoordService): = CoordService()
            *   context_service (CoordContextService): = CoordContextService()
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
        self._previous_coord = None
        self._current_coord = None
        self._stack = items
    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def previous_coord(self) -> Optional[Coord]:
        return self._stack[-2] if self._stack else None
    
    @property
    def current_coord(self) -> Optional[Coord]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> CoordService:
        """Get CoordService instance."""
        return cast(CoordService, self.entity_service)
    
    @property
    def context_service(self) -> CoordContextService:
        """Get CoordContextService."""
        return cast(CoordContextService, self.context_service)
    
    @property
    def coords(self) -> List[Coord]:
        return cast(List[Coord], self.items)
    
    def push(self, item: Coord) -> InsertionResult[bool]:
        """
        # ACTION:
            1.  If the coord fails validation send an exception chain in the InsertionResult.
            2.  If the current_position is not null, store it in previous_top then call super().push_item.
            3.  If super().push_item fails send the exception chain in the InsertionResult. Else,
                *   Set self.previous_coord = previous_top.
                *   Forward the InsertionResult from super().push_item to the caller.
        # PARAMETERS:
            *   coord (Coord)
        # RETURN:
            *   InsertionResult[Coord] containing either:
                    - On failure: Exception
                    - On success: Coord in the payload.
        # RAISES:
            *   CoordStackException
        """
        method = "CoordStackService.push"
        
        # Handle the case that coord validation fails.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=PushingCoordFailedException(
                        message=f"{method}: {PushingCoordFailedException.ERROR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that the Coord is already at the top.
        if item == self.current_coord:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=PushingCoordFailedException(
                        message=f"{method}: {PushingCoordFailedException.ERROR_CODE}",
                        ex=DuplicateCoordPushException(f"{method}: {DuplicateCoordPushException.DEFAULT_MESSAGE}")
                    )
                )
            )
        #--- Set the current coord as the previous one then, push the new coord. ---#
        self._previous_coord = self._current_coord
        self._stack.append(item)
        
        # Return the successful result to the caller.
        return InsertionResult.success()
    
    def pop(self) -> DeletionResult[Coord]:
        """
        # ACTION:
            1.  If the list is empty send the exception in the DeletionResult. Else, call the super class undo_push
            2.  If the super class undo_push failed encapsulate the super class exception and send in the
                DeletionResult, Else, forward the super().push_item() result to the caller.
        # PARAMETERS:
            None
        # RETURN:
            *   DeletionResult[Coord] containing either:
                - On failure: Exception
                - On success: Coord in the payload.
        # RAISES:
            *   CoordStackException
            *   PoppingEmtpyCoordStackException
        """
        method = "CoordStackService.pop_coord"
        
        # Handle the case that the list is empty
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {CoordDataServiceException.ERROR_CODE}",
                    ex=PoppingEmtpyCoordStackException(
                        message=f"{method}: {PoppingEmtpyCoordStackException.ERROR_CODE}",
                        ex=PoppingEmtpyCoordStackException(f"{method}: {CoordDataServiceException.DEFAULT_MESSAGE}")
                    )
                )
            )
        # Handle the case that a new coord has not been pushed onto the stack. Only one undo is allowed in a turn.
        if self._previous_coord == self._current_coord:
            return DeletionResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {CoordDataServiceException.ERROR_CODE}",
                    ex=MaxConsecutiveCoordPopException(f"{method}: {MaxConsecutiveCoordPopException.DEFAULT_MESSAGE}")
                )
            )
        # --- Remove the coord at the top of the stack and send in the DeletionResult. ---#
        coord = self._stack.pop(-1)
        return DeletionResult.success(payload=coord)
    
    def coord_search(self, coord_context: CoordContext) -> SearchResult[List[Coord]]:
        """
        # ACTION:
            1.  If coord_context fails validation send the exception chain in the SearchResult. Else use the
                coord_context_service to run the search.
            2.  If the search fails send the exception chain in the SearchResult. Else, send the search_result.
        # PARAMETERS:
            *   coord_context (CoordContext)
        # RETURN:
            *   SearchResult[Coord] containing either:
                - On failure: Exception
                - On success: Coord in the payload.
                - On empty: Payload is null, Exception is null.
        # RAISES:
            *   CoordStackException
        """
        method = "CoordStackService.coord_search"
        
        # Handle the case that the context is not certified safe.
        context_validation = self.context_service.validator.validate(coord_context)
        if context_validation.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=context_validation.exception
                )
            )
        # --- Run the search for the coord ---#
        search_result = self.context_service.finder.find(context=coord_context)
        
        # Handle the case that the search does not complete.
        if search_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        # Handle the case that a successful search result does no[Coord]  t have List[Coord] as its payload.
        if not isinstance(search_result.payload, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordDataServiceException(
                    message=f"ServiceId:{self.id}, {method}: {CoordDataServiceException.ERROR_CODE}",
                    ex=TypeError(
                        f"{method}: Expected List as CoordSearch payload. "
                        f"Got {search_result.payload.__name__} instead.")
                )
            )
        # Empty or successful searches are directly returned to the caller.
        return search_result


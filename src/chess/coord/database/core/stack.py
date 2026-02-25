# src/chess/coord/database/core/stack.py

"""
Module: chess.coord.database.core.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List, Optional, cast


from chess.system import StackService, DeletionResult, InsertionResult, SearchResult, id_emitter
from chess.coord import (
    Coord, CoordContext, CoordService, CoordContextService, CoordStackException, DuplicateCoordPushException,
    MaxConsecutiveCoordPopException,
    PoppingCoordStackFailedException, PoppingEmtpyCoordStackException, PushingCoordFailedException
)


class CoordStack(StackService[Coord]):
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
    SERVICE_NAME = "CoordStack"
    
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
        method = "CoordStack.push"
        
        # Handle the case that, coord validation fails.
        validation = self.integrity_service.validator.validate(candidate=item)
        if validation.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                CoordStackException(
                    msg=f"ServiceId:{self.id}, {method}: {CoordStackException.ERR_CODE}",
                    ex=PushingCoordFailedException(
                        msg=f"{method}: {PushingCoordFailedException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # Handle the case that, the Coord is already at the top.
        if item == self.current_coord:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                CoordStackException(
                    msg=f"ServiceId:{self.id}, {method}: {CoordStackException.ERR_CODE}",
                    ex=PushingCoordFailedException(
                        msg=f"{method}: {PushingCoordFailedException.ERR_CODE}",
                        ex=DuplicateCoordPushException(f"{method}: {DuplicateCoordPushException.MSG}")
                    )
                )
            )
        #--- Set the updated coord as the original one then, push the new coord. ---#
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
        method = "CoordStack.pop_coord"
        
        # Handle the case that, the list is empty
        if self.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                CoordStackException(
                    msg=f"ServiceId:{self.id}, {CoordStackException.ERR_CODE}",
                    ex=PoppingCoordStackFailedException(
                        msg=f"{method}: {PoppingCoordStackFailedException.ERR_CODE}",
                        ex=PoppingEmtpyCoordStackException(f"{method}: {CoordStackException.MSG}")
                    )
                )
            )
        # Handle the case that, a new coord has not been pushed onto the stack. Only one undo is allowed in a turn.
        if self._previous_coord == self._current_coord:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                CoordStackException(
                    msg=f"ServiceId:{self.id}, {CoordStackException.ERR_CODE}",
                    ex=PoppingCoordStackFailedException(
                        msg=f"{method}: {PoppingCoordStackFailedException.ERR_CODE}",
                        ex=MaxConsecutiveCoordPopException(
                            f"{method}: {MaxConsecutiveCoordPopException.MSG}"
                        )
                    )
                )
            )
        # --- Remove the coord at the top of the stack and send in the DeletionResult. ---#
        coord = self._stack.pop(-1)
        return DeletionResult.success(payload=coord)
    

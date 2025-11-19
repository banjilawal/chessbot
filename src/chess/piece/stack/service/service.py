# src/chess/coord/stack/service/service.py

"""
Module: chess.coord.stack.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord, CoordService
from chess.piece import (
    CoordStackServiceException, CoordStackValidator, CoordStack, PoppingEmptyCoordStackException,
    PushingDuplicateCoordException
)
from chess.piece.stack.service.exception import CannotUndoPreviousTurnException, DoubleCoordPushException
from chess.system import LoggingLevelRouter, Result, SearchResult, ValidationResult


class CoordStackService:
    """
    # ROLE: Service, Data Structure Operations

    # RESPONSIBILITIES:
    1.  Provides Piece instance with a single interface for CoordStack, CoordStackValidator
        and CoordService.
    2.  Prevents direct access to CoordStack.
    3.  Manages push, pop and search operations on CoordStack.


    # PROVIDES:
    ValidationResult[CoordStackService] containing either:
        - On success: CoordStackService in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
        *   stack_size (int):                                  Shows the size of the internal stack.
        
        *   is_empty (bool):                                    Shows if the internal stack is empty.
        
        *   pops_per_turn (int):                                Assures only the current move can be undone.
        .
        *   stack (CoordStack):                                 The stack of Coord objects. Protected
                                                                from direct access.
                                                                
        *   current_coord (Coord):                              Shows the current coord on the stack.
        
        *   coord_service (CoordService):                       Validates Coord objects before pushing them
                                                                onto the stack.
                                                                
        *   coord_stack_validator (type[CoordStackValidator]):  For internally validating the stack attribute
                                                                when running CoordStackServiceValidator
    """
    
    _is_empty: bool
    _stack_size: int
    _pops_per_turn: int
    _stack: CoordStack
    _current_coord: Coord
    _coord_service: CoordService
    _coord_stack_validator: type[CoordStackValidator]
    
    def __init__(
            self,
            stack: CoordStack = CoordStack(),
            coord_service: CoordService = CoordService(),
            coord_stack_validator: type[CoordStackValidator] = CoordStackValidator,
    ):
        self._stack = stack
        self._coord_service = coord_service
        self._coord_stack_validator = coord_stack_validator

        self._pops_per_turn = 0
        self._stack_size = self._stack.size
        self._is_empty = self._stack.is_empty()
        self._current_coord = self._stack.current_coord
        
    @property
    def stack(self) -> CoordStack:
        return self._stack
    
    @property
    def stack_size(self) -> int:
        return self._stack.size
    
    @property
    def is_empty(self) -> bool:
        return self._stack.is_empty()
    
    @property
    def current_coord(self) -> Optional[Coord]:
        return self._stack.current_coord
    
    @property
    def pops_per_turn(self) -> int:
        return self._pops_per_turn
    
    @LoggingLevelRouter.monitor
    def validate_coord_stack(self) -> ValidationResult[CoordStack]:
        """Validates the internal CoordStack without exposing it."""
        return self._coord_stack_validator.validate(self._stack)
    
    @LoggingLevelRouter.monitor
    def push_coord(self, coord) -> Result[Coord]:
        """
        # ACTION:
        1.  Verify the stack is not empty.
        2.  Make sure pops_per_turn is zero.
        3.  Validate the Coord is safe to push.
        4.  Make sure the coord does not already at the top of the stack.
        5.  If any check fails, return the exception inside a Result.
        6.  Pussh the new coord ontop of the stack.
        8.  Return the pushed coord in a Result to show success.

        # PARAMETERS:
        None

        # Returns:
        Result[Coord] containing either:
            - On success:   Coord in the payload.
            - On failure:   Exception.

        # RAISES:
            *   DoubleCoordPushException
        """
        method = "CoordStackService.push_coord"
        
        try:
            coord_validation = self._coord_service.validate_as_coord(coord)
            if coord_validation.is_failure():
                return Result.failure(coord_validation.exception)
            
            if coord == self._stack.current_coord:
                return Result.failure(
                    DoubleCoordPushException(
                        f"{method}: {DoubleCoordPushException.DEFAULT_MESSAGE}"
                    )
                )
            
            self._stack.items.append(coord)
            self._pops_per_turn = 0
            return Result.success(coord)
        
        except Exception as ex:
            return Result.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def undo_push(self) -> Result[Coord]:
        """
        # ACTION:
        1.  Verify the stack is not empty.
        2.  Make sure pops_per_turn is zero.
        3.  Validate the Coord is safe to push.
        5.  If any check fails, return the exception inside a Result.
        6.  Pop current_position from the stack.
        7.  Increment pops_per_turn.
        8.  Return the pushed coord in a Result.

        # PARAMETERS:
        None

        # Returns:
        Result[Coord] containing either:
            - On success:   Coord in the payload.
            - On failure:   Exception.

        # RAISES:
            *   PoppingEmptyCoordStackException
            *   CannotUndoPreviousTurnException
        """
        method = "CoordStackService.undo_push"
        
        try:
            if self._stack.is_empty():
                return Result.failure(
                    PoppingEmptyCoordStackException(
                        f"{method}: "
                        f"{PoppingEmptyCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if self._pops_per_turn != 0:
                return Result.failure(
                    CannotUndoPreviousTurnException(
                        f"{method}: "
                        f"{CannotUndoPreviousTurnException.DEFAULT_MESSAGE}"
                    )
                )
            
            coord = self._stack.items.pop()
            self._pops_per_turn += 1
            return Result.success(coord)
        
        except Exception as ex:
            return Result.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_coord(self, coord) -> SearchResult[Coord]:
        method = "CoordStackService.find_coord"
        
        try:
            coord_validation = self._coord_service.validate_as_coord(coord)
            if coord_validation.is_failure():
                return SearchResult.failure(coord_validation.exception)
            
            for coord in self._stack.items:
                if coord == coord:
                    return SearchResult.success(coord)
            return SearchResult.empty()
        
        except Exception as ex:
            return SearchResult.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )

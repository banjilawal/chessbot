# src/chess/piece/stack/service/service.py

"""
Module: chess.piece.stack.service.service
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
from chess.system import LoggingLevelRouter, Result, SearchResult, Service, ValidationResult


class CoordStackService(Service[CoordStack]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for CoordStack, CoordStackValidator and CoordStackBuilde.
    2.  Protects CoordStack objects from direct manipulation.
    3.  Extends behavior and functionality of CoordStack objects.
    4.  Public facing API for CoordStack modules.

    # PROVIDES:
        *   CoordStack building
        *   CoordStack validation
        *   CoordStack exceptions
        *   Stack operations (push, pop, search

    # ATTRIBUTES:
        *   stack_size (int)
        *   is_empty (bool)
        *   pops_per_turn (int)
        *   stack (CoordStack)
        *   current_coord (Coord)
        *   coord_service (CoordService)
        *   validator (type[CoordStackValidator]
    """
    SERVICE_NAME = "CoordStackService"
    
    _is_empty: bool
    _stack_size: int
    _pops_per_turn: int
    _stack: CoordStack
    _current_coord: Coord
    _coord_service: CoordService
    _validator: type[CoordStackValidator]
    
    def __init__(
            self,
            id: int,
            name: str = SERVICE_NAME,
            stack: CoordStack = CoordStack(),
            coord_service: CoordService = CoordService(),
            validator: type[CoordStackValidator] = CoordStackValidator,
    ):
        super().__init__(id=id, name=name)
        
        self._stack = stack
        self._coord_service = coord_service
        self._validator = validator

        self._pops_per_turn = 0
        self._stack_size = self._stack.size
        self._is_empty = self._stack.is_empty()
        self._current_coord = self._stack.current_coord
        
    # @property
    # def stack(self) -> CoordStack:
    #     return self._stack
    
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
    
    @property
    def validator(self) -> type[CoordStackValidator]:
        """
        CoordValidator is the single-source-of truth for certifying the safety of
        Piece instances, their organic row and column attributes. It makes sense
        providing direct access here and letting validator return its Validation
        result directly to the caller.
        """
        return self._validator
    
    @LoggingLevelRouter.monitor
    def push_coord(self, coord) -> Result[Coord]:
        """
        # ACTION:
        1.  Verify the stack is not empty.
        2.  Make sure pops_per_turn is zero.
        3.  Validate the Coord is safe to push.
        4.  Make sure the target does not already at the top of the stack.
        5.  If any check fails, return the exception inside a Result.
        6.  Pussh the new target ontop of the stack.
        8.  Return the pushed target in a Result to show success.

        # PARAMETERS:
        None

        # Returns:
        Result[Coord] containing either:
            - On success:   Coord in the payload.
            - On failure:   Exception.

        # RAISES:
            *   DoubleCoordPushException
            *   PieceServiceException
        """
        method = "CoordStackService.push_coord"
        
        try:
            coord_validation = self._coord_service.validator.validate(candidate=coord)
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
        8.  Return the pushed target in a Result.

        # PARAMETERS:
        None

        # Returns:
        Result[Coord] containing either:
            - On success:   Coord in the payload.
            - On failure:   Exception.

        # RAISES:
            *   PoppingEmptyCoordStackException
            *   CannotUndoPreviousTurnException
            *   PieceServiceException
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
    
    def find_coord(self, target: Coord) -> SearchResult[[Coord]]:
        """
        # ACTION:
        1.  Verify target is safe with CoordStackService.coord_service.
        2.  If the check fails, return the exception inside a SearchResult.
        3.  Return the first hit found in an array for consistency with other Search flow.
        4.  If no match is found return an empty SearchResult.

        # PARAMETERS:
            * target (Coord):   Coord to search for.

        # Returns:
        SearchResult[Coord] containing either:
            - On getting a hit:     Coord in the payload.
            - On getting no hit:    Empty SearchResult.
            - On failure:           Exception.

        # RAISES:
            *   PieceServiceException
        """
        method = "CoordStackService.find_coord"
        
        try:
            coord_validation = self._coord_service.validator.validate(candidate=target)
            if coord_validation.is_failure():
                return SearchResult.failure(coord_validation.exception)
            
            for target in self._stack.items:
                if target == target:
                    return SearchResult.success([target])
            return SearchResult.empty()
        
        except Exception as ex:
            return SearchResult.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_coord_by_row(self, target: int) -> SearchResult[[Coord]]:
        """
        # ACTION:
        1.  Use CoordStackService.coord_service to verify target meets safety requirements
            for a Coord.row attribute.
        2.  If the check fails, return the exception inside a SearchResult.
        3.  Return all Coords with a matching row attribute.
        4.  If no match is found return an empty SearchResult.

        # PARAMETERS:
            * target (int):   row to search for.

        # Returns:
        SearchResult[[Coord]] containing either:
            - On getting a hit:     [Coord] in the payload.
            - On getting no hit:    Empty SearchResult.
            - On failure:           Exception.

        # RAISES:
            *   PieceServiceException
        """
        method = "CoordStackService.find_coord"
        
        try:
            row_validation = (self._coord_service
                                .validator
                                .validate_row(candidate=target))
            if row_validation.is_failure():
                return SearchResult.failure(row_validation.exception)
            
            matches = [coord for coord in self._stack.items if coord.row == target]
            if len(matches) == 0:
                return SearchResult.empty()
            
            return SearchResult.success(matches)
        
        except Exception as ex:
            return SearchResult.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )
    
    def find_coord_by_column(self, target: int) -> SearchResult[[Coord]]:
        """
        # ACTION:
        1.  Use CoordStackService.coord_service to verify target meets safety requirements
            for a Coord.column attribute.
        2.  If the check fails, return the exception inside a SearchResult.
        3.  Return all Coords with a matching row attribute.
        4.  If no match is found return an empty SearchResult.

        # PARAMETERS:
            * target (int):   column to search for.

        # Returns:
        SearchResult[[Coord]] containing either:
            - On getting a hit:     [Coord] in the payload.
            - On getting no hit:    Empty SearchResult.
            - On failure:           Exception.

        # RAISES:
            *   PieceServiceException
        """
        method = "CoordStackService.find_coord"
        
        try:
            column_validation = (self._coord_service
                              .validator
                              .validate_column(candidate=target))
            if column_validation.is_failure():
                return SearchResult.failure(column_validation.exception)
            
            matches = [coord for coord in self._stack.items if coord.column == target]
            if len(matches) == 0:
                return SearchResult.empty()
            
            return SearchResult.success(matches)
        
        except Exception as ex:
            return SearchResult.failure(
                CoordStackServiceException(
                    ex=ex,
                    message=f"{method}: "
                            f"{CoordStackServiceException.DEFAULT_MESSAGE}"
                )
            )

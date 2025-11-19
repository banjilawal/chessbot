# src/chess/coord/stack/service/service.py

"""
Module: chess.coord.stack.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import List, Optional

from chess.coord import Coord, CoordService
from chess.piece import CoordStackValidator, CoordStack
from chess.system import LoggingLevelRouter, Result, SearchResult


class CoordStackService:
    _pop_count: int
    _is_empty: bool
    _stack: CoordStack
    _current_coord: Coord
    _coord_service: CoordService
    _validator: type[CoordStackValidator]
    
    def __init__(
            self,
            stack: CoordStack = CoordStack(),
            coord_service: CoordService = CoordService(),
            validator: type[CoordStackValidator] = CoordStackValidator,
    ):
        self._stack = stack
        self._validator = validator
        self._coord_service = coord_service
        
        self._pop_count = 0
        self._is_empty = self._stack.is_empty()
        self._current_coord = self._stack.current_coord
    
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
    def pop_count(self) -> int:
        return self._pop_count
    
    @LoggingLevelRouter.monitor
    def push_coord(self, coord) -> Result[Coord]:
        """"""
        method = "CoordStackService.push_coord"
        
        try:
            coord_validation = self._coord_service.validate_coord(coord)
            if coord_validation.is_failure():
                return Result.failure(coord_validation.exception)
            
            if coord in self._stack.items:
                return Result.failure(
                    PushingDuplicateCoordException(
                        f"{method}: {PushingDuplicateCoordException.DEFAULT_MESSAGE}"
                    )
                )
            
            self._stack.items.append(coord)
            self._pop_count = 0
            return Result.success(coord)
        
        except Exception as ex:
            return Result.failure(
                CoordStackServiceException(
                    f"{method}: {CoordStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def undo_push(self) -> Result[Coord]:
        method = "CoordStackService.undo_push"
        
        try:
            if self._stack.is_empty():
                return Result.failure(
                    PopEmptyStackException(
                        f"{method}: {PopEmptyStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            if self._pop_count == 1:
                return Result.failure()
            
            coord = self._stack.items.pop()
            return Result.success(coord)
        
        except Exception as ex:
            return Result.failure(
                CoordStackServiceException(
                    f"{method}: {CoordStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )
    
    def find_coord(self, coord) -> SearchResult[Coord]:
        method = "CoordStackService.find_coord"
        
        try:
            coord_validation = self._coord_service.validate_coord(coord)
            if coord_validation.is_failure():
                return SearchResult.failure(coord_validation.exception)
            
            for coord in self._stack.items:
                if coord == coord:
                    return SearchResult.success(coord)
            
            return SearchResult.empty()
        except Exception as ex:
            return SearchResult.failure(
                CoordStackServiceException(
                    f"{method}: {CoordStackServiceException.DEFAULT_MESSAGE}",
                    ex
                )
            )

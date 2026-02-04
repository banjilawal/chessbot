# src/chess/coord/database/service.py

"""
Module: chess.coord.database.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, Database, id_emitter
)
from chess.coord import Coord, CoordContext, CoordContextService, CoordDatabaseException, CoordStack, CoordService

class CoordDatabase(Database[Coord]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all bag managed by CoordStack are unique.
    2.  Guarantee consistency of records in CoordStack.

    # PARENT:
        *   Database

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "CoordDatabase"
    
    _coord_stack: CoordStack
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            coord_stack: CoordStack = CoordStack(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   member_service (CoordStack): = CoordStack()

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, data_service=coord_stack)
        self._coord_stack = coord_stack
    
    @property
    def size(self) -> int:
        return self._coord_stack.size
    
    @property
    def is_empty(self) -> bool:
        return self._coord_stack.is_empty
    
    @property
    def integrity_service(self) -> CoordService:
        return self._coord_stack.integrity_service
    
    @property
    def context_service(self) -> CoordContextService:
        return self._coord_stack.context_service
    
    @LoggingLevelRouter.monitor
    def push(self, coord: Coord) -> InsertionResult[bool]:
        push_result = self._coord_stack.push(coord)
        if push_result.is_failure:
            return InsertionResult.failure(
                CoordDatabaseException(
                    message=f"ServiceId:{self.id}, {CoordDatabaseException.ERROR_CODE}",
                    ex=push_result.exception
                )
            )
        return push_result
    
    @LoggingLevelRouter.monitor
    def undo_push(self) -> DeletionResult[Coord]:
        pop_result = self._coord_stack.pop()
        if pop_result.is_failure:
            return InsertionResult.failure(
                CoordDatabaseException(
                    message=f"ServiceId:{self.id}, {CoordDatabaseException.ERROR_CODE}",
                    ex=pop_result.exception
                )
            )
        return pop_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: CoordContext) -> SearchResult[List[Coord]]:
        search_result = self._coord_stack.coord_search(context)
        if search_result.is_failure:
            return SearchResult.failure(
                CoordDatabaseException(
                    message=f"ServiceId:{self.id}, {CoordDatabaseException.ERROR_CODE}",
                    ex=search_result.exception
                )
            )
        return search_result

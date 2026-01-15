# src/chess/coord/service/data/unique/service.py

"""
Module: chess.coord.service.data.unique.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import (
    DeletionResult, InsertionResult, LoggingLevelRouter, SearchResult, UniqueDataService, id_emitter
)
from chess.coord import Coord, CoordContext, CoordContextService, CoordDataService, CoordService

class UniqueCoordDataService(UniqueDataService[Coord]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Ensure all items managed by CoordDataService are unique.
    2.  Guarantee consistency of records in CoordDataService.

    # PARENT:
        *   UniqueDataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UniqueDataService class for inherited attributes.
    """
    SERVICE_NAME = "UniqueCoordDataService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: CoordDataService = CoordDataService(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int): = id_emitter.service_id
            *   name (str): = SERVICE_NAME
            *   member_service (CoordDataService): = CoordDataService()

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name, data_service=data_service)
    
    @property
    def coord_service(self) -> CoordService:
        return cast(CoordDataService, self.data_service).coord_service
    
    @property
    def context_service(self) -> CoordContextService:
        return cast(CoordDataService, self.data_service).coord_context_service
    
    @property
    def size(self) -> int:
        return self.data_service.size
    
    @property
    def is_empty(self) -> bool:
        return self.data_service.is_empty
    
    @LoggingLevelRouter.monitor
    def add_coord(self, coord: Coord) -> InsertionResult[Coord]:
        return self.push_unique_item(coord)
    
    @LoggingLevelRouter.monitor
    def undo_add_coord(self) -> DeletionResult[Coord]:
        return self.data_service.undo_item_push()
    
    @LoggingLevelRouter.monitor
    def search_coords(self, context: CoordContext) -> SearchResult[List[Coord]]:
        return self.data_service.search(context)

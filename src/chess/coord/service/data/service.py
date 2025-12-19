# src/chess/coord/service/data/service.py

"""
Module: chess.coord.service.data.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List, cast

from chess.system import DataService, id_emitter
from chess.coord import Coord, CoordService, CoordContextService


class CoordDataService(DataService[Coord]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Microservice API for managing and searching Coord collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Coords are put in the collection.
    4.  Assure updates do not break the integrity individual items in the collection or
        the collection itself.
    5.  Provide Coord stack data structure with no guarantee of uniqueness.
    6.  Search utility.

    # PARENT:
        *   DataService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataService class for inherited attributes.
    """
    SERVICE_NAME = "CoordDataService"
    
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
            *   designation (str): = SERVICE_NAME
            *   items (List[Coord]): = List[Coord]
            *   service (CoordService): = CoordService()
            *   context_service (CoordContextService): = CoordContextService()

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(
            id=id,
            name=name,
            items=items,
            entity_service=service,
            context_service=context_service,
        )
    
    @property
    def coord_service(self) -> CoordService:
        """Get CoordService instance."""
        return cast(CoordService, self.entity_service)
    
    @property
    def coord_context_service(self) -> CoordContextService:
        """Get CoordContextService."""
        return cast(CoordContextService, self.context_service)
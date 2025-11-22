# src/chess/coord/service/data/__init__.py

"""
Module: chess.coord.service.data.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""
from typing import List

from chess.coord import Coord, CoordContext, CoordSearchService, CoordService
from chess.coord.context.service.service import CoordContextService
from chess.system import DataService, SearchResult


class CoordDataService(DataService[Coord]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for Square, VectoValidator and SquareBuilder objects.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects Square objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   SquareBuilder
        *   SquareValidator
        *   Coord Data Service
        *

    # ATTRIBUTES:
        *   builder (type[SquareBuilder]):
        *   validator (type[SquareValidator]):
        *   coord_service (CoordService)
        *   identity_service (IdentityService)
    """
    """
    # ROLE: Service, Data Protraction

    # RESPONSIBILITIES:
    1.  Manages integrity lifecycle of Coord objects.
    2.  Vector addition and scalar multiplication of Coord objects.
    3.  Calculate distance between two Coords.
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for CoordStackValidator and CoordStackBuilder.
    2.  Protects CoordStack objects from direct manipulation.
    3.  Extends behavior and functionality of CoordStack objects.
    4.  Public facing API for CoordStack modules.
    5.  Vector addition
    6.  Scalar multiplication

    # PROVIDES:
        *   CoordBuilding
        *   CoordValidation
        *   Scalar multiplication
        *   Vector addition


    # ATTRIBUTES:
        *   builder (type[CoordBuilder])
        *   validator (type[CoordValidator])
        *   scalar_service (type[ScalarService):
        *   vector_service (type[VectorService])
    """
    SERVICE_NAME = "CoordService"
    
    id: int
    name: str
    _items: [Coord]
    _coord_service: CoordService
    _context_service: CoordContextService
    _search_service: CoordSearchService
    
    def __init__(
            self,
            id: int,
            items: List[Coord] = [],
            name: str = SERVICE_NAME,
            coord_service: CoordService = CoordService(),
            context_service: CoordContext = CoordContextService(),
            search_service: CoordSearchService = CoordSearchService(),
    ):
        super().__init__(id=id, name=name)
        self._coord_service = coord_service
        self._coord_service = context_service
        self._search_service = search_service
        
        self._items = items
        
    @property
    def items(self) -> List[Coord]:
        return self._items
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def context_service(self) -> CoordContextService:
        return self._context_service
    
    def search(self, context: CoordContext) -> SearchResult[[Coord]]:
        return self._search_service.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.validator
        )

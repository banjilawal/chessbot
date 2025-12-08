# src/chess/coord/service/data/__init__.py

"""
Module: chess.coord.service.data.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from typing import List

from chess.system import DataService, InsertionResult, LoggingLevelRouter, SearchResult, id_emitter
from chess.coord import Coord, CoordContext, CoordDataServiceException, CoordFinder, CoordService, CoordContextService


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
        *   Coord Data EntityService
        *

    # ATTRIBUTES:
        *   builder (type[SquareBuilder]):
        *   validator (type[SquareValidator]):
        *   coord_service (CoordService)
        *   idservice (IdentityService)
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
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            items: List[Coord] = List[Coord],
            search: CoordFinder = CoordFinder(),
            service: CoordService = CoordService(),
            context_service: CoordContext = CoordContextService(),
    ):
        super().__init__(
            self,
            id=id,
            name=name,
            items=items,
            search=search,
            entity_service=service,
            context_service=context_service,
        )
    
    @LoggingLevelRouter.monitor
    def push_item(self, item: Coord) -> InsertionResult[Coord]:
        method = "CoordDataService.push"
        try:
            validation = self.data.item_validator.validate(item)
            if validation.is_failure():
                return InsertionResult.failure(validation.exception)
            self.items.append(item)
            
            return InsertionResult.success(payload=item)
        except Exception as ex:
            return InsertionResult.failure(
                CoordDataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{CoordDataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    @LoggingLevelRouter.monitor
    def search(self, context: CoordContext) -> SearchResult[[Coord]]:
        method = "CoordDataService.searcher"
        return self._search_service.find(
            data_set=self.items,
            context=context,
            context_validator=self.context_service.item_validator
        )
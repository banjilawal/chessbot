# src/logic/coord/context/service/service.py

"""
Module: logic.coord.context.service.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from typing import cast

from logic.system import ContextService, id_emitter
from logic.coord import CoordContext, CoordContextBuilder, CoordContextValidationProcess, CoordFinder


class CoordContextService(ContextService[CoordContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Coord search microservice API.
    2.  Provides a map aware utility for searching Coord objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Coord search results by having single entry and exit points for the
        Coord search flow.

    Super Class:
        *   ContextService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "CoordContextService"
    def service(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: CoordFinder = CoordFinder(),
            builder: CoordContextBuilder = CoordContextBuilder(),
            validator: CoordContextValidationProcess = CoordContextValidationProcess(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   finder (CoordFinder)
            *   builder (CoordContextBuilder)
            *   validator (CoordContextValidationProcess)

        # RETURNS:
        None

        Raises:
        """
        method = "CoordContextService.service"
        super().service(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> CoordFinder:
        """Get CoordFinder instance."""
        return cast(CoordFinder, self.entity_finder)
    
    @property
    def builder(self) -> CoordContextBuilder:
        """Get CoordContextBuilder instance."""
        return cast(CoordContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> CoordContextValidationProcess:
        """Get CoordContextValidationProcess instance."""
        return cast(CoordContextValidationProcess, self.entity_validator)
# src/chess/coord/context/service/service.py

"""
Module: chess.coord.context.service.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""
from typing import cast

from chess.system import ContextService, id_emitter
from chess.coord import CoordContext, CoordContextBuilder, CoordContextValidator, CoordFinder


class CoordContextService(ContextService[CoordContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Coord search microservice API.
    2.  Provides a context aware utility for searching Coord objects.
    3.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    4.  Create a single source of truth for Coord search results by having single entry and exit points for the
        Coord search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   CoordContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "CoordContextService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: CoordFinder = CoordFinder(),
            builder: CoordContextBuilder = CoordContextBuilder(),
            validator: CoordContextValidator = CoordContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (CoordFinder): Default value - CoordFinder()
            *   builder (CoordContextBuilder): Default value - CoordContextBuilder()
            *   validator (CoordContextValidator): Default value - CoordContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "CoordContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> CoordFinder:
        """Get CoordFinder instance."""
        return cast(CoordFinder, self.entity_finder)
    
    @property
    def builder(self) -> CoordContextBuilder:
        """Get CoordContextBuilder instance."""
        return cast(CoordContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> CoordContextValidator:
        """Get CoordContextValidator instance."""
        return cast(CoordContextValidator, self.entity_validator)
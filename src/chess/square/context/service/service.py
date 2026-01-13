# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.square import SquareContext, SquareContextBuilder, SquareContextValidator, SquareFinder


class SquareContextService(ContextService[SquareContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square search microservice API.
    2.  Provides a map aware utility for searching Square objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Square search results by having single entry and exit points for the
        Square search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   SquareContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "SquareContextService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: SquareFinder = SquareFinder(),
            builder: SquareContextBuilder = SquareContextBuilder(),
            validator: SquareContextValidator = SquareContextValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (SquareFinder): Default value - SquareFinder()
            *   builder (SquareContextBuilder): Default value - SquareContextBuilder()
            *   validator (SquareContextValidator): Default value - SquareContextValidator()

        # RETURNS:
        None

        # RAISES:
        None
        """
        method = "SquareContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> SquareFinder:
        """Get SquareFinder instance."""
        return cast(SquareFinder, self.entity_finder)
    
    @property
    def builder(self) -> SquareContextBuilder:
        """Get SquareContextBuilder instance."""
        return cast(SquareContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareContextValidator:
        """Get SquareContextValidator instance."""
        return cast(SquareContextValidator, self.entity_validator)
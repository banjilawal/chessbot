# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.square import Square, SquareBuilder, SquareValidator


class SquareService(EntityService[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   SquareService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "SquareService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (SquareFactory)
            *   number_bounds_validator (SquareValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> SquareBuilder:
        """get SquareBuilder"""
        return cast(SquareBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareValidator:
        """get SquareValidator"""
        return cast(SquareValidator, self.entity_validator)
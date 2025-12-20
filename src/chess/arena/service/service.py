# src/chess/arena/service/service.py

"""
Module: chess.arena.service.service
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""


from typing import cast

from chess.arena import Arena, ArenaBuilder
from chess.system import EntityService, id_emitter


class ArenaService(EntityService[Arena]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Arena State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single source of truth for Arena state by providing single entry and exit points to Arena
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "ArenaService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: ArenaBuilder = ArenaBuilder(),
            validator: ArenaValidator = ArenaValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (ArenaFactory)
            *   number_bounds_validator (ArenaValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> ArenaBuilder:
        """get ArenaBuilder"""
        return cast(ArenaBuilder, self.entity_builder)
    
    @property
    def validator(self) -> ArenaValidator:
        """get ArenaValidator"""
        return cast(ArenaValidator, self.entity_validator)
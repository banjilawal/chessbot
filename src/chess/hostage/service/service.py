# src/chess/item/service/service.py

"""
Module: chess.item.service.service
Author: Banji Lawal
Created: 2026-01-18
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.hostage import Hostage, HostageBuilder, HostageValidator


class HostageService(EntityService[Hostage]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   HostageService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "HostageService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: HostageBuilder = HostageBuilder(),
            validator: HostageValidator = HostageValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SquareFactory)
            *   validator (SquareValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> HostageBuilder:
        """get SquareBuilder"""
        return cast(HostageBuilder, self.entity_builder)
    
    @property
    def validator(self) -> HostageValidator:
        """get SquareValidator"""
        return cast(HostageValidator, self.entity_validator)
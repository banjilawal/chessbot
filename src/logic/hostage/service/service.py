# src/logic/item/service/service.py

"""
Module: logic.item.service.service
Author: Banji Lawal
Created: 2026-01-18
version: 1.0.0
"""

from typing import cast

from logic.system import IntegrityService, id_emitter
from logic.hostage import Hostage, HostageBuildProcess, HostageValidationProcess


class HostageService(IntegrityService[Hostage]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    Super Class:
        *   IntegrityService

    # PROVIDES:
        *   HostageService


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "HostageService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            builder: HostageBuildProcess = HostageBuildProcess(),
            validator: HostageValidationProcess = HostageValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SquareFactory)
            *   validator (SquareValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def build(self) -> HostageBuildProcess:
        """get SquareBuildProcess"""
        return cast(HostageBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> HostageValidationProcess:
        """get SquareValidationProcess"""
        return cast(HostageValidationProcess, self.entity_validator)
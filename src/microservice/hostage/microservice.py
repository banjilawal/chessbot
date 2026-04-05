# src/microservice/hostage/microservice.py

"""
Module: microservice.hostage.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class HostageService(Microservice[Hostage]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    Super Class:
        *   Microservice

    # PROVIDES:
        *   HostageService


    # INHERITED ATTRIBUTES:
        *   See Microservice for inherited attributes.
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
            *   schema (str)
            *   build (SquareFactory)
            *   validation (SquareValidator)
        # RETURNS:
            None
        Raises:
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
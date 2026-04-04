# src/logic/hostage/context/service/servicepy

"""
Module: logic.hostage.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from model.hostage import CaptivityContext, CaptivityContextBuilder, CaptivityContextValidator, HostageFinder


class HostageQueryService(QueryService[CaptivityContext]):
    """
    Role:Search Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Captivity search microservice API.
    2.  Provides a map aware utility for searching Captivity objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Captivity search results by having single entry and exit points for the
        Captivity search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   HostageQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "HostageQueryService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: HostageFinder = HostageFinder(),
            builder: CaptivityContextBuilder = CaptivityContextBuilder(),
            validator: CaptivityContextValidator = CaptivityContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   schema (str)
            *   id (int)
            *   route (HostageFinder)
            *   build (CaptivityContextBuilder)
            *   validation (CaptivityContextValidator)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "HostageQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> HostageFinder:
        """Get CaptivityFinder instance."""
        return cast(HostageFinder, self.entity_finder)
    
    @property
    def build(self) -> CaptivityContextBuilder:
        """Get CaptivityContextBuilder instance."""
        return cast(CaptivityContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> CaptivityContextValidator:
        """Get CaptivityContextValidator instance."""
        return cast(CaptivityContextValidator, self.entity_validator)
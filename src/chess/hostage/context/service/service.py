# src/chess/hostage/context/service/servicepy

"""
Module: chess.hostage.context.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.hostage import CaptivityContext, CaptivityContextBuilder, CaptivityContextValidator, HostageManifestFinder


class CaptivityContextService(ContextService[CaptivityContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Captivity search microservice API.
    2.  Provides a map aware utility for searching Captivity objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Captivity search results by having single entry and exit points for the
        Captivity search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   CaptivityContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "CaptivityContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: HostageManifestFinder = HostageManifestFinder(),
            builder: CaptivityContextBuilder = CaptivityContextBuilder(),
            validator: CaptivityContextValidator = CaptivityContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (HostageManifestFinder)
            *   builder (CaptivityContextBuilder)
            *   validator (CaptivityContextValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "CaptivityContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> HostageManifestFinder:
        """Get CaptivityFinder instance."""
        return cast(HostageManifestFinder, self.entity_finder)
    
    @property
    def builder(self) -> CaptivityContextBuilder:
        """Get CaptivityContextBuilder instance."""
        return cast(CaptivityContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> CaptivityContextValidator:
        """Get CaptivityContextValidator instance."""
        return cast(CaptivityContextValidator, self.entity_validator)
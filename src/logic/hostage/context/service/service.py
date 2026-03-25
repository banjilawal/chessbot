# src/logic/hostage/query/service/servicepy

"""
Module: logic.hostage.query.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from logic.hostage import CaptivityContext, CaptivityContextBuildProcess, CaptivityContextValidationProcess, HostageFinder


class HostageQueryService(QueryService[CaptivityContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

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
            builder: CaptivityContextBuildProcess = CaptivityContextBuildProcess(),
            validator: CaptivityContextValidationProcess = CaptivityContextValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   route (HostageFinder)
            *   build (CaptivityContextBuildProcess)
            *   validation (CaptivityContextValidationProcess)
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
    def build(self) -> CaptivityContextBuildProcess:
        """Get CaptivityContextBuildProcess instance."""
        return cast(CaptivityContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> CaptivityContextValidationProcess:
        """Get CaptivityContextValidationProcess instance."""
        return cast(CaptivityContextValidationProcess, self.entity_validator)
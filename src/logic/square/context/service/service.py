# src/logic/square/query/service/servicepy

"""
Module: logic.square.query.service.service
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.system import QueryService, id_emitter
from logic.square import SquareContext, SquareContextBuildProcess, SquareContextValidationProcess, SquareFinder


class SquareQueryService(QueryService[SquareContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Square search microservice API.
    2.  Provides a map aware utility for searching Square objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Square search results by having single entry and exit points for the
        Square search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   SquareQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "SquareQueryService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: SquareFinder = SquareFinder(),
            builder: SquareContextBuildProcess = SquareContextBuildProcess(),
            validator: SquareContextValidationProcess = SquareContextValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   route (SquareFinder)
            *   build (SquareContextBuildProcess)
            *   validation (SquareContextValidationProcess)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "SquareQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> SquareFinder:
        """Get SquareFinder instance."""
        return cast(SquareFinder, self.entity_finder)
    
    @property
    def build(self) -> SquareContextBuildProcess:
        """Get SquareContextBuildProcess instance."""
        return cast(SquareContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> SquareContextValidationProcess:
        """Get SquareContextValidationProcess instance."""
        return cast(SquareContextValidationProcess, self.entity_validator)
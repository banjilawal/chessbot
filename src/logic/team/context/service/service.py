# src/logic/team/service/transaction.py

"""
Module: logic.team.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from logic.team import TeamContext, TeamContextBuilder, TeamContextValidationTransaction, TeamFinder


class TeamQueryService(QueryService[TeamContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Team search microservice API.
    2.  Provides a map aware utility for searching Team objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Team search results by having single entry and exit points for the
        Team search flow.

    Super Class:
        *   QueryService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "TeamQueryService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: TeamFinder = TeamFinder(),
            builder: TeamContextBuilder = TeamContextBuilder(),
            validator: TeamContextValidationTransaction = TeamContextValidationTransaction(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   route (TeamFinder): Default value - TeamFinder()
            *   build (TeamContextBuilder): Default value - TeamContextBuilder()
            *   validation (TeamContextValidationTransaction): Default value - TeamContextValidationTransaction()

        # RETURNS:
        None

        Raises:
        """
        method = "TeamQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> TeamFinder:
        """Get TeamFinder instance."""
        return cast(TeamFinder, self.entity_finder)
    
    @property
    def build(self) -> TeamContextBuilder:
        """Get TeamContextBuilder instance."""
        return cast(TeamContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> TeamContextValidationTransaction:
        """Get TeamContextValidationTransaction instance."""
        return cast(TeamContextValidationTransaction, self.entity_validator)
    
    
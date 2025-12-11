# src/chess/team/context/service/service.py

"""
Module: chess.team.context.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, EntityService, id_emitter
from chess.team import TeamContext, TeamContextBuilder, TeamContextValidator, TeamFinder


class TeamContextService(ContextService[TeamContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Team search microservice.
    2.  Encapsulates query building and searching functions into a single extendable module that easy to use.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   TeamFinder
        *   TeamContextBuilder
        *   TeamContextValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "TeamContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: TeamFinder = TeamFinder(),
            builder: TeamContextBuilder = TeamContextBuilder(),
            validator: TeamContextValidator = TeamContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (TeamFinder): Default value - TeamFinder()
            *   builder (TeamContextBuilder): Default value - TeamContextBuilder()
            *   validator (TeamContextValidator): Default value - TeamContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "TeamContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> TeamFinder:
        return cast(TeamFinder, self.entity_finder)
    
    @property
    def builder(self) -> TeamContextBuilder:
        return cast(TeamContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> TeamContextValidator:
        return cast(TeamContextValidator, self.entity_validator)
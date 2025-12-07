# src/chess/team/context/entity_service/entity_service.py

"""
Module: chess.team.context.entity_service.entity_service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""
from typing import cast

from chess.system import EntityService, id_emitter
from chess.team import TeamContext, TeamContextBuilder, TeamContextValidator, TeamFinder


class TeamContextService(EntityService[TeamContext]):
    """
    # ROLE: EntityService, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects TeamContext instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing TeamContext lifecycles with TeamContextBuilder and TeamContextValidator.

    # PROVIDES:
        *   TeamContextBuilder
        *   TeamContextValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (TeamContextBuilder)
        *   validator (TeamContextValidator)
     
     # CONSTRUCTOR:
        *   __init__(
                id: int = id_emmit=service_id,
                name: Optional[str] = DEFAULT_SERVICE_NAME,
                builder: TeamContextBuilder = TeamContextBuilder(),
                validator: TeamContextValidator = TeamContextValidator(),
            ):
        For ease of use and cleaner code dependencies are given default values.

    # CLASS METHODS:
    None
    
    # INSTANCE METHODS:
    See super class.
    """
    DEFAULT_SERVICE_NAME = "TeamContextService"
    _search: TeamFinder
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_SERVICE_NAME,
            builder: TeamContextBuilder = TeamContextBuilder(),
            validator: TeamContextValidator = TeamContextValidator(),
            search: TeamFinder = TeamFinder(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._search = search
        
    @property
    def item_builder(self) -> TeamContextBuilder:
        return cast(TeamContextBuilder, self.item_builder)
    
    @property
    def item_validator(self) ->TeamContextValidator:
        return cast(TeamContextValidator, self.item_validator)
        
    @property
    def search(self) -> TeamFinder:
        return self._search
        
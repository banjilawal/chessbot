# src/chess/team/context/service/service.py

"""
Module: chess.team.context.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.team import TeamContext, TeamContextBuilder, TeamContextValidator


class TeamContextService(Service[TeamContext]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single entry point for TeamContextBuilder and TeamContextValidator objects.
    2.  Passing its self._validator to the self._builder simplifies the Context lifecycle.
    3.  Protects Context from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
        *   TeamContextValidator
        *   TeamContextBuilder

    # ATTRIBUTES:
        *   builder (TeamContextBuilder):
        *   validator (TeamContextValidator):
    """
    DEFAULT_NAME = "TeamContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: TeamContextBuilder = TeamContextBuilder(),
            validator: TeamContextValidator = TeamContextValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
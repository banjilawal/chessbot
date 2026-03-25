# src/logic/rank/searcher/service.py

"""
Module: logic.rank.searcher.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from logic.system import QueryService
from logic.rank import RankContext, RankContextValidator, RankContextBuilder, RankFinder

class RankQueryService(QueryService[RankContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Rank search microservice API.
    2.  Provides a map aware utility for searching Rank objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Rank search results by having single entry and exit points for the
        Rank search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   RankQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    DEFAULT_NAME = "RankQueryService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder: RankFinder = RankFinder(),
            builder: RankContextBuilder = RankContextBuilder(),
            validator: RankContextValidator = RankContextValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   route (RankFinder): Default value - RankFinder()
            *   build (RankContextBuildProcess): Default value - RankContextBuildProcess()
            *   validation (RankContextValidationProcess): Default value - RankContextValidationProcess()

        # RETURNS:
        None

        Raises:
        """
        method = "RankQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> RankFinder:
        """Get RankFinder instance."""
        return cast(RankFinder, self.entity_finder)
    
    @property
    def build(self) -> RankContextBuilder:
        """Get RankContextBuildProcess instance."""
        return cast(RankContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> RankContextValidator:
        """Get RankContextValidationProcess instance."""
        return cast(RankContextValidator, self.entity_validator)

    
# src/chess/rank/searcher/service.py

"""
Module: chess.rank.searcher.service
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ContextService
from chess.rank import RankContext, RankContextValidator, RankContextBuilder, RankFinder

class RankContextService(ContextService[RankContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Rank search microservice API.
    2.  Provides a map aware utility for searching Rank objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Rank search results by having single entry and exit points for the
        Rank search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   RankContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "RankContextService"
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
            *   finder (RankFinder): Default value - RankFinder()
            *   builder (RankContextBuilder): Default value - RankContextBuilder()
            *   validator (RankContextValidator): Default value - RankContextValidator()

        # RETURNS:
        None

        # RAISES:
        None
        """
        method = "RankContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> RankFinder:
        """Get RankFinder instance."""
        return cast(RankFinder, self.entity_finder)
    
    @property
    def builder(self) -> RankContextBuilder:
        """Get RankContextBuilder instance."""
        return cast(RankContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> RankContextValidator:
        """Get RankContextValidator instance."""
        return cast(RankContextValidator, self.entity_validator)

    
# src/chess/rank/service/service.py

"""
Module: chess.rank.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""
from typing import cast

from chess.system import EntityService, id_emitter
from chess.rank import Rank, RankFactory, RankSpecValidator, RankValidatorFactory


class RankService(EntityService[Rank]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Rank microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Rank state by providing single entry and exit points to Rank
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
        *   RankService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    DEFAULT_NAME = "RankService"
    _spec_service: RankSpecService
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: RankFactory = RankFactory(),
            spec_service: RankSpecService = RankSpecService(),
            validator: RankValidatorFactory = RankValidatorFactory(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (RankFactory)
            *   validator (RankValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> RankFactory:
        """get RankBuilder."""
        return cast(RankFactory, self.entity_builder)
    
    @property
    def validator(self) -> RankValidatorFactory:
        """get RankValidator."""
        return cast(RankValidatorFactory, self.entity_validator)
    
    @property
    def spec_service(self) -> RankSpecService:
        """get RankSpecService."""
        return self._spec_service
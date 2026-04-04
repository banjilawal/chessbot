# src/logic/rank/service/validator.py

"""
Module: logic.rank.service.service
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from typing import cast

from catalog.persona import PersonaService
from system import IntegrityMicroservice, id_emitter
from logic.rank import Rank, RankFactory, RankValidatorFactory


class RankService(IntegrityMicroservice[Rank]):
    """
    Role:Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Rank microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Rank state by providing single entry and exit points to Rank
        lifecycle.

    Super Class:
        *   IntegrityMicroservice

    # PROVIDES:
        *   RankService


    # INHERITED ATTRIBUTES:
        *   See IntegrityMicroservice for inherited attributes.
    """
    DEFAULT_NAME = "RankService"
    _persona_service: PersonaService
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: RankFactory = RankFactory(),
            persona_service: PersonaService = PersonaService(),
            validator: RankValidatorFactory = RankValidatorFactory(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   schema (str)
            *   build (RankFactory)
            *   validation (RankValidator)

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._persona_service = persona_service
    
    @property
    def builder(self) -> RankFactory:
        """get RankBuilder."""
        return cast(RankFactory, self.entity_builder)
    
    @property
    def validator(self) -> RankValidatorFactory:
        """get RankValidator."""
        return cast(RankValidatorFactory, self.entity_validator)
    
    @property
    def persona_service(self) -> PersonaService:
        return self._persona_service
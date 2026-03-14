# src/logic/pair/listing/service/service.py

"""
Module: logic.pair.listing.service.service
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import PairList, PairListBuilder, PairListValidator
from logic.system import IdFactory, IntegrityService


class PairListService(IntegrityService[PairList]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PairList microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PairList state by providing
        single entry and exit points to PairList lifecycle.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "PairListService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: PairListBuilder = PairListBuilder(),
            validator: PairListValidator = PairListValidator(),
            id: int = IdFactory.next_id(class_name="PairListService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: PairListBuilder
            validator: PairListValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
    
    @property
    def builder(self) -> PairListBuilder:
        return cast(PairListBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PairListValidator:
        return cast(PairListValidator, self.entity_validator)
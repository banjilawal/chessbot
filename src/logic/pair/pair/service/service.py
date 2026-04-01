# src/logic/pair/pair/service/validator.py

"""
Module: logic.pair.pair.service.service
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import Pair, PairBuilder, PairValidator
from logic.system import IdFactory, IntegrityMicroService


class PairService(IntegrityMicroService[Pair]):
    """
    Role:MicroService, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Pair microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Pair state by providing
        single entry and exit points to Pair lifecycle.

    Super Class:
        *   IntegrityMicroService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityMicroService for inherited attributes.
    """
    SERVICE_NAME = "PairService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: PairBuilder = PairBuilder(),
            validator: PairValidator = PairValidator(),
            id: int = IdFactory.next_id(class_name="PairService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: PairBuilder
            validator: PairValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> PairBuilder:
        return cast(PairBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PairValidator:
        return cast(PairValidator, self.entity_validator)
        
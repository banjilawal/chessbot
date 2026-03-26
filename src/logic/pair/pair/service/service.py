# src/logic/pair/pair/service/compute.py

"""
Module: logic.pair.pair.service.service
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import Pair, PairBuildProcess, PairValidationProcess
from logic.system import IdFactory, IntegrityService


class PairService(IntegrityService[Pair]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Pair microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Pair state by providing
        single entry and exit points to Pair lifecycle.

    Super Class:
        *   IntegrityService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "PairService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: PairBuildProcess = PairBuildProcess(),
            validator: PairValidationProcess = PairValidationProcess(),
            id: int = IdFactory.next_id(class_name="PairService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: PairBuildProcess
            validator: PairValidationProcess
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def build(self) -> PairBuildProcess:
        return cast(PairBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> PairValidationProcess:
        return cast(PairValidationProcess, self.entity_validator)
        
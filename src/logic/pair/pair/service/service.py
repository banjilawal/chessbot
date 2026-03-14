# src/logic/pair/pair/service/service.py

"""
Module: logic.pair.pair.service.service
Author: Banji Lawal
Created: 2026-03-13
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import NodePair, NodePairBuilder, NodePairValidator
from logic.system import IdFactory, IntegrityService


class NodePairService(IntegrityService[NodePair]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing NodePair microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for NodePair state by providing
        single entry and exit points to NodePair lifecycle.

    # PARENT:
        *   IntegrityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "NodePairService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: NodePairBuilder = NodePairBuilder(),
            validator: NodePairValidator = NodePairValidator(),
            id: int = IdFactory.next_id(class_name="NodePairService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: NodePairBuilder
            validator: NodePairValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> NodePairBuilder:
        return cast(NodePairBuilder, self.entity_builder)
    
    @property
    def validator(self) -> NodePairValidator:
        return cast(NodePairValidator, self.entity_validator)
        
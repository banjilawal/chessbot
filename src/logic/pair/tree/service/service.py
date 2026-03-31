# src/logic/pair/tree/service/validator.py

"""
Module: logic.pair.tree.service.service
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import NodeTree, NodeTreeBuilder, NodeTreeValidator
from logic.pair.listing.service import PairListService
from logic.system import IdFactory, IntegrityService


class NodeTreeService(IntegrityService[NodeTree]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing NodeTree microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for NodeTree state by providing
        single entry and exit points to NodeTree lifecycle.

    Super Class:
        *   IntegrityService

    Provides:

    # LOCAL ATTRIBUTES:
        *   branch_service: PairListService

    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    SERVICE_NAME = "NodeTreeService"
    _branch_service: PairListService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: NodeTreeBuilder = NodeTreeBuilder(),
            validator: NodeTreeValidator = NodeTreeValidator(),
            branch_service: PairListService = PairListService(),
            id: int = IdFactory.next_id(class_name="NodeTreeService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: NodeTreeBuilder
            validator: NodeTreeValidator
            branch_service: PairListService
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._branch_service = branch_service
        
    
    @property
    def builder(self) -> NodeTreeBuilder:
        return cast(NodeTreeBuilder, self.entity_builder)
    
    @property
    def validation(self) -> NodeTreeValidator:
        return cast(NodeTreeValidator, self.entity_validator)
    
    @property
    def branch_service(self) -> PairListService:
        return self._branch_service
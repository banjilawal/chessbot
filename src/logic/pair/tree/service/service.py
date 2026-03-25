# src/logic/pair/tree/service/process.py

"""
Module: logic.pair.tree.service.service
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.pair import NodeTree, NodeTreeBuildProcess, NodeTreeValidationProcess
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
            builder: NodeTreeBuildProcess = NodeTreeBuildProcess(),
            validator: NodeTreeValidationProcess = NodeTreeValidationProcess(),
            branch_service: PairListService = PairListService(),
            id: int = IdFactory.next_id(class_name="NodeTreeService"),
    ):
        """
        Args:
            id: int
            name: str
            builder: NodeTreeBuildProcess
            validator: NodeTreeValidationProcess
            branch_service: PairListService
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._branch_service = branch_service
        
    
    @property
    def build(self) -> NodeTreeBuildProcess:
        return cast(NodeTreeBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> NodeTreeValidationProcess:
        return cast(NodeTreeValidationProcess, self.entity_validator)
    
    @property
    def branch_service(self) -> PairListService:
        return self._branch_service
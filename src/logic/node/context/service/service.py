# src/logic/node/context/service/servicepy

"""
Module: logic.node.context.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.system import ContextService, id_emitter
from logic.node import NodeContext, NodeContextBuilder, NodeContextValidationProcess, NodeFinder


class NodeContextService(ContextService[NodeContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Node search microservice API.
    2.  Provides a map aware utility for searching Node objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Node search results by having single entry and exit points for the
        Node search flow.

    Super Class:
        *   ContextService

    # PROVIDES:
        *   NodeContextService


    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "NodeContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: NodeFinder = NodeFinder(),
            builder: NodeContextBuilder = NodeContextBuilder(),
            validator: NodeContextValidationProcess = NodeContextValidationProcess(),
    ):
        """
        Args:
            id: int
            name: str
            finder: NodeFinder
            builder: NodeContextBuilder
            validator: NodeContextValidationProcess
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> NodeFinder:
        """Get NodeFinder instance."""
        return cast(NodeFinder, self.entity_finder)
    
    @property
    def builder(self) -> NodeContextBuilder:
        """Get NodeContextBuilder instance."""
        return cast(NodeContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> NodeContextValidationProcess:
        """Get NodeContextValidationProcess instance."""
        return cast(NodeContextValidationProcess, self.entity_validator)
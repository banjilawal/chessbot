# src/logic/node/context/service/servicepy

"""
Module: logic.node.context.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from system import QueryService, id_emitter
from graph.node import NodeContext, NodeContextBuilder, NodeContextValidator, NodeFinder


class NodeQueryService(QueryService[NodeContext]):
    """
    Role:Search Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Node search microservice API.
    2.  Provides a map aware utility for searching Node objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Node search results by having single entry and exit points for the
        Node search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   NodeQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "NodeQueryService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: NodeFinder = NodeFinder(),
            builder: NodeContextBuilder = NodeContextBuilder(),
            validator: NodeContextValidator = NodeContextValidator(),
    ):
        """
        Args:
            id: int
            name: str
            finder: NodeFinder
            builder: NodeContextBuilder
            validator: NodeContextValidator
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> NodeFinder:
        """Get NodeFinder instance."""
        return cast(NodeFinder, self.entity_finder)
    
    @property
    def build(self) -> NodeContextBuilder:
        """Get NodeContextBuilder instance."""
        return cast(NodeContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> NodeContextValidator:
        """Get NodeContextValidator instance."""
        return cast(NodeContextValidator, self.entity_validator)
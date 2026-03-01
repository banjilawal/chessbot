# src/chess/node/context/service/servicepy

"""
Module: chess.node.context.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.system import ContextService, id_emitter
from chess.node import NodeContext, NodeContextBuilder, NodeContextValidator, NodeFinder


class NodeContextService(ContextService[NodeContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Node search microservice API.
    2.  Provides a map aware utility for searching Node objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Node search results by having single entry and exit points for the
        Node search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   NodeContextService

    # LOCAL ATTRIBUTES:
    None

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
            validator: NodeContextValidator = NodeContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (NodeFinder)
            *   builder (NodeContextBuilder)
            *   validator (NodeContextValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "NodeContextService.__init__"
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
    def validator(self) -> NodeContextValidator:
        """Get NodeContextValidator instance."""
        return cast(NodeContextValidator, self.entity_validator)
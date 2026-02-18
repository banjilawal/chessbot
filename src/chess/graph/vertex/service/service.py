# src/chess/graph/node/service/service.py

"""
Module: chess.graph.node.service.service
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.graph.node.service import NodeServiceException
from chess.system import EntityService, IdFactory, InsertionResult, LoggingLevelRouter
from chess.graph import Edge, EdgeValidator, Node, NodeBuilder, NodeValidator


class NodeService(EntityService[ Node]):
    """
    """
    SERVICE_NAME = "NodeService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: NodeBuilder = NodeBuilder(),
            validator: NodeValidator = NodeValidator(),
            id: int = IdFactory.next_id(class_name="NodeService"),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> NodeBuilder:
        return cast(NodeBuilder, self.entity_builder)
    
    @property
    def validator(self) -> NodeValidator:
        return cast(NodeValidator, self.entity_validator)
    
    @LoggingLevelRouter.monitor
    def add_incoming_edge(self, edge: Edge, edge_validator: EdgeValidator = EdgeValidator()) -> InsertionResult:
        method = "NodeService.add_incoming_edge"
        
        # Handle the case that the edge is not certified as safe.
        edge_validation_result = edge_validator.validate(edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                NodeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {NodeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        
        
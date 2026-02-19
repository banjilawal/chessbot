# src/chess/edge/service/service.py

"""
Module: chess.edge.service.service
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.edge import Edge, EdgeBuilder, EdgeValidator
from chess.system import EntityService, IdFactory, InsertionResult, LoggingLevelRouter


class EdgeService(EntityService[Edge]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Edge microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Edge state by providing single entry and exit points to Edge
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "EdgeService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: EdgeBuilder = EdgeBuilder(),
            validator: EdgeValidator = EdgeValidator(),
            id: int = IdFactory.next_id(class_name="EdgeService"),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (EdgeFactory)
            *   validator (EdgeValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> EdgeBuilder:
        return cast(EdgeBuilder, self.entity_builder)
    
    @property
    def validator(self) -> EdgeValidator:
        return cast(EdgeValidator, self.entity_validator)
    
    @LoggingLevelRouter.monitor
    def add_incoming_edge(self, edge: Edge, edge_validator: EdgeValidator = EdgeValidator()) -> InsertionResult:
        method = "EdgeService.add_incoming_edge"
        
        # Handle the case that the edge is not certified as safe.
        edge_validation_result = edge_validator.validate(edge)
        if edge_validation_result.is_failure:
            # Return the exception chain on failure.
            return InsertionResult.failure(
                EdgeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeServiceException.DEFAULT_MESSAGE}",
                    ex=AddIncomingEdgeFailedException(
                        message=f"ServiceId:{self.id}, {method}: {AddIncomingEdgeFailedException.DEFAULT_MESSAGE}",
                        ex=edge_validation_result.exception
                    )
                )
            )
        
        
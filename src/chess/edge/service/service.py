# src/chess/edge/service/service.py

"""
Module: chess.edge.service.service
Author: Banji Lawal
Created: 2025-02-17
version: 1.0.0
"""

from __future__ import annotations

import sys
from copy import deepcopy
from typing import cast

from chess.edge import Edge, EdgeBuilder, EdgeServiceException, EdgeValidator
from chess.system import EntityService, IdFactory, LoggingLevelRouter, NumberValidator, UpdateResult


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
    def update_edge_heuristic(
            self,
            edge: Edge,
            heuristic: int,
            number_validator: NumberValidator = NumberValidator()
    ) -> UpdateResult[Edge]:
        method = "EdgeService.update_edge_heuristic"
        
        # Handle the case that the edge is unsafe.
        edge_validation = self.integrity_service.validator.validate(candidate=edge)
        if edge_validation.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=edge,
                exception=EdgeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeServiceException.ERROR_CODE}",
                    ex=UpdatingEdgeHeuristicException(
                        message=f"{method}: {UpdatingEdgeHeuristicException.ERROR_CODE}",
                        ex=edge_validation.exception
                    )
                )
            )
        # Handle the case that the heuristic is not a number.
        heuristic_validation_result = number_validator.validate(
            candidate=heuristic,
            ceiling=sys.maxsize,
            floor=0,
        )
        if heuristic_validation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=edge,
                exception=EdgeServiceException(
                    message=f"ServiceId:{self.id}, {method}: {EdgeServiceException.ERROR_CODE}",
                    ex=EdgeHeuristicException(
                        message=f"{method}: {EdgeHeuristicException.DEFAULT_MESSAGE}",
                        ex=heuristic_validation_result.exception
                    )
                )
            )
        original_edge = deepcopy(edge)
        
        edge.heuristic = heuristic
        return UpdateResult.update_success(original=original_edge, updated=edge)
    
        
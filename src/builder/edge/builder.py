# src/builder/edge/builder.py

"""
Module: builder.edge.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice.edge import Edge, EdgeBuilderException
from system import Builder, BuildResult, LoggingLevelRouter, NumberValidator


class EdgeBuilder(Builder[Edge]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Edge instance is born safe and reliable.

    Attributes:

    Provides:
        def build(
                cls,
                row: int,
                column: int,
                number_validator: NumberValidator = NumberValidator(),
        ) -> BuildResult[Edge]:

     Super Class:
         Builder
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            row: int,
            column: int,
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[Edge]:
        """
        Build a Edge.

        Action:
            1.  Send an exception chain in the BuildResult if either:
                    -   The row
                    -   The column
                are fail its validation checks.
            2.  Otherwise, build the Edge then, send the success reult.
        Args:
            row: int
            column: int
            number_validator: NumberValidator)
        Returns:
            BuildResult[Edge]
        Raises:
            EdgeBuilderException
        """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            head: Node,
            tail: Node,
            id: int = IdFactory.next_id(class_name="Edge"),
            edge_service: EdgeService = EdgeService(),
            node_service: NodeService = NodeService(),
            identity_service: IdentityService = IdentityService(),
     ) -> BuildResult[Edge]:
         """
         # ACTION:
             1. If any build param fails its certification tests send the exception in the BuildResult.
             2. Use edge_service to compute the edge's Euclidean dist. If the arithmetic fails send the
                exception in the BuildResult.
            3.  Return an Edge whose heuristic is zero in the BuildResult.
         # PARAMETERS:
             *   id (int)
             *   head (Edge)
             *   tail: (Edge)
             *   edge_service (EdgeService)
             *   edge_service (EdgeService)
             *   identity_service (IdentityService)
             *   formation_service: (FormationService)
         # RETURNS:
             *   BuildResult[Edge] containing either:
                     - On failure: Exception.
                     - On success: Edge in the payload.
         Raises:
             *   EdgeBuilderException
         """
         method = "EdgeBuilder.build"
         
         # Handle the case that, the idis not safe.
         id_validation = identity_service.validate_id(id)
         if id_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuilderException(
                     msg=f"{method} {EdgeBuilderException.MSG}",
                     ex=id_validation.exception
                 )
             )
         # Handle the case that, the head is not certified as a safe edge.
         head_validation = node_service.validator.search_service(candidate=head)
         if head_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuilderException(
                     msg=f"{method} {EdgeBuilderException.MSG}",
                     ex=head_validation.exception
                 )
             )
         # Handle the case that, the tail is not certified as a safe edge.
         tail_validation = node_service.search_service.search_service(candidate=tail)
         if tail_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuilderException(
                     msg=f"{method} {EdgeBuilderException.MSG}",
                     ex=tail_validation.exception
                 )
             )
         # Handle the case that, head and tail are the same.
         if head == tail:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuilderException(
                     msg=f"{method} {EdgeBuilderException.MSG}",
                     ex=HeadCannotBeTailException(f"{method}: {HeadCannotBeTailException.MSG}")
                 )
             )
         # --- After the inputs have been validated compute the edge's Euclidean dist. ---#
         distance_computation_result = edge_service.distance(
             u=head.home_square.edge,
             v=tail.home_square.edge
         )
         # Handle the case that, the dist is not computed successfully.
         if distance_computation_result.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuilderException(
                     msg=f"{method} {EdgeBuilderException.MSG}",
                     ex=distance_computation_result.exception
                 )
             )
         # --- Create the edge with a heuristic of zero then return in the BuildResult. ---#
         return BuildResult.success(
             payload=Edge(
                 id=id,
                 head=head,
                 tail=tail,
                 heuristic=0,
                 distance=distance_computation_result.payload,
             )
         )
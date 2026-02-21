# src/chess/edge/builder/builder.py

"""
Module: chess.edge.builder.builder
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.coord import CoordService
from chess.graph import Edge, EdgeBuildFailedException, HeadCannotBeTailException, Edge, EdgeValidator
from chess.system import BuildResult, Builder, IdFactory, IdentityService, LoggingLevelRouter


class EdgeBuilder(Builder[Edge]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Edge instances whose integrity is guaranteed at creation.
    2.  Manage construction of Edge instances that can be used safely by the client.
    3.  Ensure params for Edge creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            head: Edge,
            tail: Edge,
            id: int = IdFactory.next_id(class_name="Edge"),
            coord_service: CoordService = CoordService(),
            edge_validator: EdgeValidator = EdgeValidator(),
            identity_service: IdentityService = IdentityService(),
     ) -> BuildResult[Edge]:
         """
         # ACTION:
             1. If any build param fails its certification tests send the exception in the BuildResult.
             2. Use coord_service to compute the edge's Euclidean distance. If the computation fails send the
                exception in the BuildResult.
            3.  Return an Edge whose heuristic is zero in the BuildResult.
         # PARAMETERS:
             *   id (int)
             *   head (Edge)
             *   tail: (Edge)
             *   coord_service (CoordService)
             *   edge_service (EdgeService)
             *   identity_service (IdentityService)
             *   formation_service: (FormationService)
         # RETURNS:
             *   BuildResult[Edge] containing either:
                     - On failure: Exception.
                     - On success: Edge in the payload.
         # RAISES:
             *   EdgeBuildException
         """
         method = "EdgeBuilder.build"
         
         # Handle the case that the id is not certified safe.
         id_validation = identity_service.validate_id(id)
         if id_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=id_validation.exception
                 )
             )
         # Handle the case that the head is not certified as a safe edge.
         head_validation = edge_validator.validate(candidate=head)
         if head_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=head_validation.exception
                 )
             )
         # Handle the case that the tail is not certified as a safe edge.
         tail_validation = edge_validator.validate(candidate=tail)
         if tail_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=tail_validation.exception
                 )
             )
         # Handle the case that head and tail are the same.
         if head == tail:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=HeadCannotBeTailException(f"{method}: {HeadCannotBeTailException.DEFAULT_MESSAGE}")
                 )
             )
         # --- After the inputs have been validated compute the edge's Euclidean distance. ---#
         distance_computation_result = coord_service.euclidean_distance(
             u=head.square.coord,
             v=tail.square.coord
         )
         # Handle the case that the distance is not computed successfully.
         if distance_computation_result.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
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
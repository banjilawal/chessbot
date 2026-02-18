# src/chess/graph/edge/builder/builder.py

"""
Module: chess.graph.edge.builder.builder
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from chess.coord import CoordService
from chess.graph import Edge, EdgeBuildFailedException, Vertex, VertexValidator
from chess.system import BuildResult, Builder, IdentityService, LoggingLevelRouter


class EdgeBuilder(Builder[Edge]):
     
     @classmethod
     @LoggingLevelRouter.monitor
     def build(
             cls, 
             id: int,
             head: Vertex, 
             tail: Vertex,
             coord_service: CoordService = CoordService(),
             vertex_validator: VertexValidator = VertexValidator(),
             identity_service: IdentityService = IdentityService(),
     ) -> BuildResult[Edge]:
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
         # Handle the case that the head is not certified safe.
         head_validation = vertex_validator.validate(candidate=head)
         if head_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=head_validation.exception
                 )
             )
         # Handle the case that the tail is not certified safe.
         tail_validation = vertex_validator.validate(candidate=tail)
         if tail_validation.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=tail_validation.exception
                 )
             )
         
         distance_computation_result = coord_service.euclidean_distance(
             u=head.square.coord,
             v=tail.square.coord
         )
         # Handle the case that the distance is not computed.
         if distance_computation_result.is_failure:
             # Return the exception chain on failure
             return BuildResult.failure(
                 EdgeBuildFailedException(
                     message=f"{method} {EdgeBuildFailedException.DEFAULT_MESSAGE}",
                     ex=distance_computation_result.exception
                 )
             )
         
         # Create the Edge with a heuristic of zero. Then return to the caller.
         return BuildResult.success(
             payload=Edge(
                 id=id,
                 head=head,
                 tail=tail,
                 heuristic=0,
                 distance=distance_computation_result.payload,
             )
         )
    
# src/chess/graph/vertex/builder/builder.py

"""
Module: chess.graph.vertex.builder.builder
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.graph import Vertex, VertexBuildFailedException
from chess.square import Square, SquareValidator
from chess.system import BuildResult, Builder, LoggingLevelRouter


class VertexBuilder(Builder[Vertex]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Vertex instances whose integrity is guaranteed at creation.
    2.  Manage construction of Vertex instances that can be used safely by the client.
    3.  Ensure params for Vertex creation have met the application's safety contract.
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
    def build(cls, square: Square, square_validator: SquareValidator = SquareValidator()) -> BuildResult[Vertex]:
        """
        # ACTION:
            1.  If the square is not valid send an exception chain in the BuildResult. Otherwise, use the square
                to create a Vertex which is returned in the BuildResult.
        # PARAMETERS:
            *   square (Square)
            *   squareValidator: (SquareValidator)
        # RETURNS:
            *   BuildResult[Vertex] containing either:
                    - On failure: Exception.
                    - On success: Vertex in the payload.
        # RAISES:
            *   VertexBuildFailedException
        """
        method = "VertexBuilder.build"
        
        # Handle the case that the square is not certified as safe.
        validation_result = square_validator.validate(square)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                VertexBuildFailedException(
                    message=f"{method}: {VertexBuildFailedException.DEFAULT_MESSAGE}",
                    ex=validation_result.exception
                )
            )
        
        # --- Create the Vertex and return in the BuildResult. ---#
        return BuildResult.success(payload=Vertex(square=square))
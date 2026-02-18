# src/chess/graph/node/builder/builder.py

"""
Module: chess.graph.node.builder.builder
Author: Banji Lawal
Created: 2026-02-17
version: 1.0.0
"""

from __future__ import annotations

from chess.graph import Node, NodeBuildFailedException
from chess.square import Square, SquareValidator
from chess.system import BuildResult, Builder, LoggingLevelRouter


class NodeBuilder(Builder[Node]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Node instances whose integrity is guaranteed at creation.
    2.  Manage construction of Node instances that can be used safely by the client.
    3.  Ensure params for Node creation have met the application's safety contract.
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
    def build(cls, square: Square, square_validator: SquareValidator = SquareValidator()) -> BuildResult[Node]:
        """
        # ACTION:
            1.  If the square is not valid send an exception chain in the BuildResult. Otherwise, use the square
                to create a Node which is returned in the BuildResult.
        # PARAMETERS:
            *   square (Square)
            *   squareValidator: (SquareValidator)
        # RETURNS:
            *   BuildResult[Node] containing either:
                    - On failure: Exception.
                    - On success: Node in the payload.
        # RAISES:
            *   NodeBuildFailedException
        """
        method = "NodeBuilder.build"
        
        # Handle the case that the square is not certified as safe.
        validation_result = square_validator.validate(square)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeBuildFailedException(
                    message=f"{method}: {NodeBuildFailedException.DEFAULT_MESSAGE}",
                    ex=validation_result.exception
                )
            )
        
        # --- Create the Node and return in the BuildResult. ---#
        return BuildResult.success(payload=Node(square=square))
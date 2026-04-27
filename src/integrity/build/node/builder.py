# src/integrity/build/node/builder.py

"""
Module: integrity.build.node.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from graph.domain.graph import Node, NodeBuildException
from logic.square import Square, SquareValidator
from system import BuildResult, Builder, LoggingLevelRouter


class NodeBuilder(Builder[Node]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
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
        Raises:
            *   NodeBuildException
        """
        method = "NodeBuilder.build"
        
        # Handle the case that, the square does not pass a validation check.
        validation_result = square_validator.validate(square)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NodeBuildException(
                    msg=f"{method}: {NodeBuildException.MSG}",
                    ex=validation_result.exception
                )
            )
        
        # --- Create the Node and return in the BuildResult. ---#
        return BuildResult.success(payload=Node(square=square))
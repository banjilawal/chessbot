# src/toolkit/model/node/toolkit.py

"""
Module: toolkit.model.node.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Node
from toolkit import Toolkit


class NodeToolkit(Toolkit[Node]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """

    @LoggingLevelRouter.monitor
    def __init__(self, square: Square, square_validator: SquareValidator = SquareValidator()) -> ToolkitResult[Node]:
        """
        # ACTION:
            1.  If the square is not valid send an exception chain in the ToolkitResult. Otherwise, use the square
                to create a Node which is returned in the ToolkitResult.
        # PARAMETERS:
            *   square (Square)
            *   squareValidator: (SquareValidator)
        # RETURNS:
            *   ToolkitResult[Node] containing either:
                    - On failure: Exception.
                    - On success: Node in the payload.
        Raises:
            *   NodeToolkitException
        """
        method = "NodeToolkit.toolkit"
        
        # Handle the case that, the square does not pass a validation check.
        validation_result = square_validator.execute(square)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                NodeToolkitException(
                    msg=f"{method}: {NodeToolkitException.MSG}",
                    ex=validation_result.exception
                )
            )
        
        # --- Create the Node and return in the ToolkitResult. ---#
        return ToolkitResult.success(payload=Node(square=square))
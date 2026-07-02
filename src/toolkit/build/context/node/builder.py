# src/toolkit/context/node/toolkit.py

"""
Module: toolkit.context.node.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import sys
from typing import Optional

from model.node import (
    DiscoveryStatus, ArenaNodeContextFlagsException, Node, NodeContext, NodeContextToolkitException,
    NodeContextToolkitRouteException, NodeValidator, ZeroNodeContextFlagsException
)
from logic.square import Square, SquareService
from system import Toolkit, ToolkitResult, NumberValidator



class NodeContextToolkit(Toolkit[NodeContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Toolkit Process Owner

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
            ) -> ToolkitResult[Token]

     Super Class:
         Toolkit
     """
    @classmethod
    def __init__(
            self,
            priority: Optional[int] = None,
            square: Optional[Square] = None,
            predecessor: Optional[Node] = None,
            discovery_status: Optional[DiscoveryStatus] = None,
            square_service: SquareService = SquareService(),
            node_validator: NodeValidator = NodeValidator(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ToolkitResult[NodeContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the ToolkitResult.
            2.  If there is no toolkit route for the not-null context attribute send an exception chain in the ToolkitResult.
            3.  If the toolkit route exists and the context attribute is not verified send an exception chain in the
                ToolkitResult. Else toolkit the context and send it in the ToolkitResult's payload.
        # PARAMETERS:
            Only one these must be provided:

                *   priority Optional[(int)]
                *   predecessor Optional[(Predecessor)]
                *   discovery_status Optional[DiscoveryStatus]
            These Parameters must be provided:
                *   predecessor_service (PredecessorService)
                *   priority_service (PriorityService)
                *   square_validator (SquareService)
                *   number_validation (IdentityService)
            # RETURNS:
                *   ToolkitResult[NodeContext] containing either:
                        - On failure: Exception.
                        - On success: NodeContext in the payload.
            Raises:
                *   ZeroNodeContextFlagsException
                *   NodeContextToolkitException
                *   ArenaNodeContextFlagsException
                *   NodeContextToolkitRouteException
            """
        method = "NodeContextToolkit.toolkit"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [priority, square,predecessor, discovery_status,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that, all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                NodeContextToolkitException(
                    msg=f"{method}: {NodeContextToolkitException.MSG}",
                    ex=ZeroNodeContextFlagsException(
                        f"{method}: {ZeroNodeContextFlagsException.MSG}"
                    )
                )
            )
        # Handle the case that, more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return ToolkitResult.failure(
                NodeContextToolkitException(
                    msg=f"{method}: {NodeContextToolkitException.MSG}",
                    ex=ArenaNodeContextFlagsException(
                        f"{method}: {ArenaNodeContextFlagsException.MSG}"
                    )
                )
            )
        # --- Route to the appropriate validation/toolkit branch. ---#
        
        # Toolkit the priority NodeContext if its flag is enabled.
        if priority is not None:
            validation = number_validator.execute(
                candidate=priority,
                ceiling=sys.maxsize,
                floor=-(sys.maxsize - 1),
            )
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    NodeContextToolkitException(
                        msg=f"{method}: {NodeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_NodeContext in the ToolkitResult.
            return ToolkitResult.success(NodeContext(priority=priority))
        
        # Toolkit the square NodeContext if its flag is enabled.
        if square is not None:
            validation = square_service.validator.execute(candidate=square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    NodeContextToolkitException(
                        msg=f"{method}: {NodeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a square_NodeContext in the ToolkitResult.
            return ToolkitResult.success(NodeContext(square=square))
        
        # Toolkit the predecessor NodeContext if its flag is enabled.
        if predecessor is not None:
            validation = node_validator.execute(candidate=predecessor)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    NodeContextToolkitException(
                        msg=f"{method}: {NodeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a predecessor_NodeContext in the ToolkitResult.
            return ToolkitResult.success(NodeContext(predecessor=predecessor))
        
        # Toolkit the discovery_status NodeContext if its flag is enabled.
        if discovery_status is not None:
            validation = node_validator.validate_discovery_status(candidate=discovery_status)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ToolkitResult.failure(
                    NodeContextToolkitException(
                        msg=f"{method}: {NodeContextToolkitException.MSG}",
                        ex=validation.exception
                    )
                )
            # On validation success return a predecessor_NodeContext in the ToolkitResult.
            return ToolkitResult.success(NodeContext(discovery_status=discovery_status))
        
        # Return the exception chain if there is no toolkit route for the context.
        return ToolkitResult.failure(
            NodeContextToolkitException(
                msg=f"{method}: {NodeContextToolkitException.MSG}",
                ex=NodeContextToolkitRouteException(f"{method}: {NodeContextToolkitRouteException.MSG}")
            )
        )
# src/chess/node/context/builder/builder.py

"""
Module: chess.node.context.builder.builder
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations

import sys
from typing import Optional

from chess.node import (
    DiscoveryStatus, ExcessiveNodeContextFlagsException, Node, NodeContext, NodeContextBuildException,
    NodeContextBuildRouteException, NodeValidator, ZeroNodeContextFlagsException
)
from chess.square import Square, SquareService
from chess.system import Builder, BuildResult, NumberValidator



class NodeContextBuilder(Builder[NodeContext]):
    """
    # ROLE: Builder, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce NodeContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of NodeContext instances that can be used safely by the client.
    3.  Ensure params for NodeContext creation have met the application's safety contract.
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
    def build(
            cls,
            priority: Optional[int] = None,
            square: Optional[Square] = None,
            predecessor: Optional[Node] = None,
            discovery_status: Optional[DiscoveryStatus] = None,
            square_service: SquareService = SquareService(),
            node_validator: NodeValidator = NodeValidator(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> BuildResult[NodeContext]:
        """
        # ACTION:
            1.  If one-and-only-one context attribute is not null send an exception chain in the BuildResult.
            2.  If there is no build route for the not-null context attribute send an exception chain in the BuildResult.
            3.  If the build route exists and the context attribute is not verified send an exception chain in the
                BuildResult. Else build the context and send it in the BuildResult's payload.
        # PARAMETERS:
            Only one these must be provided:

                *   priority Optional[(int)]
                *   predecessor Optional[(Predecessor)]
                *   discovery_status Optional[DiscoveryStatus]
            These Parameters must be provided:
                *   predecessor_service (PredecessorService)
                *   priority_service (PriorityService)
                *   square_service (SquareService)
                *   number_validator (IdentityService)
            # RETURNS:
                *   BuildResult[NodeContext] containing either:
                        - On failure: Exception.
                        - On success: NodeContext in the payload.
            # RAISES:
                *   ZeroNodeContextFlagsException
                *   NodeContextBuildException
                *   ExcessiveNodeContextFlagsException
                *   NodeContextBuildRouteException
            """
        method = "NodeContextBuilder.build"

        # --- Count how many optional parameters are not-null. only one should be not null. ---#
        params = [priority, square,predecessor, discovery_status,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeContextBuildException(
                    message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                    ex=ZeroNodeContextFlagsException(
                        f"{method}: {ZeroNodeContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeContextBuildException(
                    message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                    ex=ExcessiveNodeContextFlagsException(
                        f"{method}: {ExcessiveNodeContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Route to the appropriate validation/build branch. ---#
        
        # Build the priority NodeContext if its flag is enabled.
        if priority is not None:
            validation = number_validator.validate(
                candidate=priority,
                ceiling=sys.maxsize,
                floor=-(sys.maxsize - 1),
            )
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeContextBuildException(
                        message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return an id_NodeContext in the BuildResult.
            return BuildResult.success(NodeContext(priority=priority))
        
        # Build the square NodeContext if its flag is enabled.
        if square is not None:
            validation = square_service.validator.validate(candidate=square)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeContextBuildException(
                        message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a square_NodeContext in the BuildResult.
            return BuildResult.success(NodeContext(square=square))
        
        # Build the predecessor NodeContext if its flag is enabled.
        if predecessor is not None:
            validation = node_validator.validate(candidate=predecessor)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeContextBuildException(
                        message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a predecessor_NodeContext in the BuildResult.
            return BuildResult.success(NodeContext(predecessor=predecessor))
        
        # Build the discovery_status NodeContext if its flag is enabled.
        if discovery_status is not None:
            validation = node_validator.validate_discovery_status(candidate=discovery_status)
            if validation.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeContextBuildException(
                        message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a predecessor_NodeContext in the BuildResult.
            return BuildResult.success(NodeContext(discovery_status=discovery_status))
        
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            NodeContextBuildException(
                message=f"{method}: {NodeContextBuildException.DEFAULT_MESSAGE}",
                ex=NodeContextBuildRouteException(f"{method}: {NodeContextBuildRouteException.DEFAULT_MESSAGE}")
            )
        )
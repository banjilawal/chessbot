# src/logic/pair/array/builder/builder.py

"""
Module: logic.pair.array.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import Node, NodeService
from logic.pair import NodePairBuilder, NodePairListBuildException, TreeDoesNotOwnRayException
from logic.pair.array import NodePairList
from logic.span import SquareRay, SquareRayService
from logic.system import BuildResult, Builder, LoggingLevelRouter


class NodePairListBuilder(Builder[NodePairList]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor
    
     # RESPONSIBILITIES:
     1.  Produce NodePairList instances whose integrity and reliability are guaranteed.
     2.  Ensure params for NodePairList creation have met the application's safety contract.
     3.  Return an exception to the client if a build resource does not satisfy integrity requirements.
    
     # PARENT:
         * Builder
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
        *   See Builder class for inherited attributes.
    
    # CONSTRUCTOR PARAMETERS:
    None
    
    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
        *   See Builder class for inherited methods.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            parent_node: Node,
            square_ray: SquareRay,
            node_service: NodeService = NodeService(),
            node_pair_builder: NodePairBuilder = NodePairBuilder(),
            square_ray_service: SquareRayService = SquareRayService(),
    ) -> BuildResult[NodePairList]:
        """
        Action:
            1.  Send an exception chain if, either
                    *   origin_node.square != square_ray.origin
                    *   a node_pair build fails.
            2.  Otherwise, start the cursor at the origin_node then, iterate through
                the ray's members.
            3.  On each iteration
                    *   Build a node pair.
                    *   Append to the node_pair_list.
                    *   Advance the cursor.
            4.  Return the success result.

        Args:
            parent_node: Node
            square_ray: SquareRay
            node_service: NodeService
            node_pair_builder: NodePairBuilder
            square_ray_service: SquareRayService

        Returns:
            BuildResult[NodePairList]

        Raises:
            NodePairListBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        # Handle the case that, the parent_node is not certified as safe.
        parent_validation_result = node_service.validator.validate(parent_node)
        if not parent_validation_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                NodePairListBuildException(
                    mthd=method,
                    op=NodePairListBuildException.OP,
                    msg=NodePairListBuildException.MSG,
                    err_code=NodePairListBuildException.ERR_CODE,
                    rslt_type=NodePairListBuildException.RSLT_TYPE,
                    ex=parent_validation_result.exception,
                )
            )
        # Handle the case that, the ray is not certified as safe.
        square_ray_validation_result = square_ray_service.validator.validate(square_ray)
        if square_ray_validation_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                NodePairListBuildException(
                    mthd=method,
                    op=NodePairListBuildException.OP,
                    msg=NodePairListBuildException.MSG,
                    err_code=NodePairListBuildException.ERR_CODE,
                    rslt_type=NodePairListBuildException.RSLT_TYPE,
                    ex=square_ray_validation_result.exception,
                )
            )
        # Handle the case that the ray belongs to a different parent.
        if square_ray.origin != parent_node.square:
            # Return the exception chain on failure.
            BuildResult.failure(
                NodePairListBuildException(
                    mthd=method,
                    op=NodePairListBuildException.OP,
                    msg=NodePairListBuildException.MSG,
                    err_code=NodePairListBuildException.ERR_CODE,
                    rslt_type=NodePairListBuildException.RSLT_TYPE,
                    ex=TreeDoesNotOwnRayException(
                        msg=NodePairListBuildException.MSG,
                        err_code=NodePairListBuildException.ERR_CODE,
                    )
                )
            )
        # --- Initialize the cursor and create the return target.---#
        cursor = parent_node
        node_pair_list: NodePairList = NodePairList()

        # --- Do the node_pair building work on each ray member. ---#
        for member in square_ray.members:
            build_result = node_pair_builder.build(
                head=cursor,
                tail_square=member,
                node_service=node_service,
            )
            # Handle the case that, there is no work product.
            if build_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    NodePairListBuildException(
                        mthd=method,
                        op=NodePairListBuildException.OP,
                        msg=NodePairListBuildException.MSG,
                        err_code=NodePairListBuildException.ERR_CODE,
                        rslt_type=NodePairListBuildException.RSLT_TYPE,
                        ex=build_result.exception,
                    )
                )
                # --- Add the pair to the list, then advance the cursor. ---#.
                node_pair_list.items.append(build_result.payload)
                cursor = build_result.payload.tail
        
        # --- Send the completed list of node_pairs ---#
        return BuildResult.success(node_pair_list)
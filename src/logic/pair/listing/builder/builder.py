# src/logic/pair/listing/build/exception.py

"""
Module: logic.pair.listing.build.build
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import Node, NodeService
from logic.pair import PairBuildProcess, PairList, PairListBuildException, TreeDoesNotOwnRayException
from logic.span import SquareRay, SquareRayService
from logic.system import BuildResult, BuildProcess, LoggingLevelRouter


class PairListBuildProcess(BuildProcess[PairList]):
    """
     Role:BuildProcess, Data Integrity And Reliability Guarantor
    
     Responsibilities:
     1.  Produce PairList instances whose integrity and reliability are guaranteed.
     2.  Ensure params for PairList creation have met the application's safety contract.
     3.  Return an exception to the client if a build resource does not satisfy integrity requirements.
    
     Super Class:
         * BuildProcess
    
    Provides:
    
    
    # INHERITED ATTRIBUTES:
        *   See BuildProcess class for inherited attributes.
    
    Attributes:
    None
    
    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
        *   See BuildProcess class for inherited methods.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            parent_node: Node,
            square_ray: SquareRay,
            node_service: NodeService = NodeService(),
            pair_builder: PairBuildProcess = PairBuildProcess(),
            square_ray_service: SquareRayService = SquareRayService(),
    ) -> BuildResult[PairList]:
        """
        Action:
            1.  Send an exception chain if, either
                    *   origin_node.square != square_ray.origin
                    *   a pair build fails.
            2.  Otherwise, start the cursor at the origin_node then, iterate through
                the ray's members.
            3.  On each iteration
                    *   Build a node pair.
                    *   Append to the pair_list.
                    *   Advance the cursor.
            4.  Return the success result.

        Args:
            parent_node: Node
            square_ray: SquareRay
            node_service: NodeService
            pair_builder: PairBuildProcess
            square_ray_service: SquareRayService

        Returns:
            BuildResult[PairList]

        Raises:
            PairListBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
        # Handle the case that, the parent_node does not pass a validation check.
        parent_validation_result = node_service.validation.execute(parent_node)
        if not parent_validation_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                PairListBuildException(
                    mthd=method,
                    op=PairListBuildException.OP,
                    msg=PairListBuildException.MSG,
                    err_code=PairListBuildException.ERR_CODE,
                    rslt_type=PairListBuildException.RSLT_TYPE,
                    ex=parent_validation_result.exception,
                )
            )
        # Handle the case that, the ray does not pass a validation check.
        square_ray_validation_result = square_ray_service.validation.execute(square_ray)
        if square_ray_validation_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                PairListBuildException(
                    mthd=method,
                    op=PairListBuildException.OP,
                    msg=PairListBuildException.MSG,
                    err_code=PairListBuildException.ERR_CODE,
                    rslt_type=PairListBuildException.RSLT_TYPE,
                    ex=square_ray_validation_result.exception,
                )
            )
        # Handle the case that the ray belongs to a different parent.
        if square_ray.origin != parent_node.square:
            # Return the exception chain on failure.
            BuildResult.failure(
                PairListBuildException(
                    mthd=method,
                    op=PairListBuildException.OP,
                    msg=PairListBuildException.MSG,
                    err_code=PairListBuildException.ERR_CODE,
                    rslt_type=PairListBuildException.RSLT_TYPE,
                    ex=TreeDoesNotOwnRayException(
                        msg=PairListBuildException.MSG,
                        err_code=PairListBuildException.ERR_CODE,
                    )
                )
            )
        # --- Initialize the cursor and create the return target.---#
        cursor = parent_node
        pair_list: PairList = PairList()

        # --- Do the pair building work on each ray member. ---#
        for member in square_ray.members:
            build_result = pair_builder.execute(
                head=cursor,
                tail_square=member,
                node_service=node_service,
            )
            # Handle the case that, there is no work product.
            if build_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    PairListBuildException(
                        mthd=method,
                        op=PairListBuildException.OP,
                        msg=PairListBuildException.MSG,
                        err_code=PairListBuildException.ERR_CODE,
                        rslt_type=PairListBuildException.RSLT_TYPE,
                        ex=build_result.exception,
                    )
                )
                # --- Add the pair to the list, then advance the cursor. ---#.
                pair_list.items.append(build_result.payload)
                cursor = build_result.payload.tail
        
        # --- Send the completed list of pairs ---#
        return BuildResult.success(pair_list)
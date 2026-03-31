# src/logic/pair/build/exception.py

"""
Module: logic.pair.build.build
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import NodeService
from logic.pair import PairListBuilder, NodeTreeBuildException
from logic.pair.pair.service.service import PairService
from logic.pair.tree.tree import NodeTree
from logic.span import SquareSpan, SquareSpanService
from logic.system import BuildResult, Builder, LoggingLevelRouter


class NodeTreeBuilder(Builder[NodeTree]):
    """
     Role:Builder, Data Integrity And Reliability Guarantor

     Responsibilities:
     1.  Produce NodeTree instances whose integrity and reliability are guaranteed.
     2.  Ensure params for NodeTree creation have met the application's safety contract.
     3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     Super Class:
         * Builder

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Builder class for inherited attributes.

    Attributes:
    None

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See Builder class for inherited methods.
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            square_span: SquareSpan,
            node_service: NodeService = NodeService(),
            pair_service: PairService = PairService(),
            square_span_service: SquareSpanService = SquareSpanService(),
            pair_list_builder: PairListBuilder = PairListBuilder(),
    ) -> BuildResult[NodeTreeBuilder]:
        """
        Action:
            1.  If building a node from the tail_square fails send an exception chain in
                the BuildResult.
            2.  If the build was successful
                    *   Build a pair with the head and its new tail.
                    *   Return the work product.
        Args:
            square_span: SquareSpan
            node_service: NodeService
            square_span_service: SquareSpanService
            pair_list_builder: PairListBuilder
            

        Returns:
            BuildResult[NodeTree]

        Raises:
            NodeTreeBuildException
        """
        method = f"{cls.__class__.__name__}._build"
        
        # Handle the case that the square_span does not pass a validation check.
        square_span_result = square_span_service.validation.validate(candidate=square_span)
        if square_span_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeTreeBuildException(
                    mthd=method,
                    op=NodeTreeBuildException.OP,
                    msg=NodeTreeBuildException.MSG,
                    err_code=NodeTreeBuildException.ERR_CODE,
                    rslt_type=NodeTreeBuildException.RSLT_TYPE,
                    ex=square_span_result.exception,
                )
            )
        # --- Process the sub_span_roots then, build the tree's root node. ---#
        insertion_result = cls._convert_sub_span_roots_to_ray(span=square_span)
        root_node_build_result = node_service.build.execute(square=square_span.origin)
        
        # Handle the case that, the root_node is not built successfully.
        if root_node_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                NodeTreeBuildException(
                    mthd=method,
                    op=NodeTreeBuildException.OP,
                    msg=NodeTreeBuildException.MSG,
                    err_code=NodeTreeBuildException.ERR_CODE,
                    rslt_type=NodeTreeBuildException.RSLT_TYPE,
                    ex=root_node_build_result.exception,
                )
            )
        # --- Om success create the node_tree  ---#
        node_tree = NodeTree(root=root_node_build_result.payload, branches=[])
        
        for ray in square_span.rays:
            branch_build_result = pair_list_builder.execute(
                square_ray=ray,
                parent_node=node_tree.root,
            )
            # Handle the case that, the pair_list  is not built.
            if branch_build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    NodeTreeBuildException(
                        mthd=method,
                        op=NodeTreeBuildException.OP,
                        msg=NodeTreeBuildException.MSG,
                        err_code=NodeTreeBuildException.ERR_CODE,
                        rslt_type=NodeTreeBuildException.RSLT_TYPE,
                        ex=branch_build_result.exception,
                    )
                )
            # --- Add the pairs to the tree. ---#
            node_tree.branches.append(branch_build_result.payload)
        
        # --- Send the success result. ---#
        return BuildResult.success(node_tree)
        
        
        
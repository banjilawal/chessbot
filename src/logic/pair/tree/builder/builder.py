# src/logic/pair/builder/builder.py

"""
Module: logic.pair.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import NodeService
from logic.pair import NodePairListBuilder, NodeTreeBuildException
from logic.pair.tree.tree import NodeTree
from logic.span import SquareRay, SquareSpan, SquareSpanService
from logic.system import BuildResult, Builder, InsertionResult, LoggingLevelRouter


class NodeTreeBuilder(Builder[NodeTree]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce NodeTree instances whose integrity and reliability are guaranteed.
     2.  Ensure params for NodeTree creation have met the application's safety contract.
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
            square_span: SquareSpan,
            node_service: NodeService = NodeService(),
            square_span_service: SquareSpanService = SquareSpanService(),
            node_pair_list_builder: NodePairListBuilder = NodePairListBuilder(),
    ) -> BuildResult[NodeTreeBuilder]:
        """
        Action:
            1.  If building a node from the tail_square fails send an exception chain in
                the BuildResult.
            2.  If the build was successful
                    *   Build a node_pair with the head and its new tail.
                    *   Return the work product.
        Args:
            square_span: SquareSpan
            node_service: NodeService
            square_span_service: SquareSpanService
            node_pair_list_builder: NodePairListBuilder
            

        Returns:
            BuildResult[NodeTree]

        Raises:
            NodeTreeBuildException
        """
        method = f"{cls.__class__.__name__}._build"
        
        # Handle the case that the square_span is not certified as safe.
        square_span_result = square_span_service.validator.validate(candidate=square_span)
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
        root_node_build_result = node_service.builder.build(square=square_span.origin)
        
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
            branch_build_result = node_pair_list_builder.build(
                square_ray=ray,
                parent_node=node_tree.root,
            )
            # Handle the case that, the node_pair_list  is not built.
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
            # --- Add the node_pairs to the tree. ---#
            node_tree.branches.append(branch_build_result.payload)
        
        # --- Send the success result. ---#
        return BuildResult.success(node_tree)
        
        
        
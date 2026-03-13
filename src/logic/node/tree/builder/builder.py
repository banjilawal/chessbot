# src/logic/node/tree/builder/builder.py

"""
Module: logic.node.tree.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import NodeService, NodeTree, NodeTreeBuildException
from logic.span import SquareRay, SquareSpan, SquareSpanService
from logic.system import BuildResult, Builder, LoggingLevelRouter


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
        
        # --- If the span contains any child spans, put them in a ray, then append to the parent, rays. ---#
        if square_span.has_sub_spans:
            square_span.rays.append(
                SquareRay(
                    origin=square_span.origin,
                    members=square_span.sub_span_roots
                )
            )
            # Clear the roots so they don't get added again.
            square_span.sub_span_roots.clear()
        
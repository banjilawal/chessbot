# src/logic/pair/pair/builder/builder.py

"""
Module: logic.pair.pair.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.square import Square, SquareValidator
from logic.system import BuildResult, Builder, LoggingLevelRouter
from logic.node import HeadTailSquareException, Node, NodePair, NodePairBuildException, NodeService


class NodePairBuilder(Builder[NodePair]):
    """
     # ROLE: Builder, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce NodePair instances whose integrity and reliability are guaranteed.
     2.  Ensure params for NodePair creation have met the application's safety contract.
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
            head: Node,
            tail_square: Square,
            node_service: NodeService = NodeService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> BuildResult[NodePair]:
        """
        Action:
            1.  If building a node from the tail_square fails send an exception chain in
                the BuildResult.
            2.  If the build was successful
                    *   Build a node_pair with the head and its new tail.
                    *   Return the work product.
        Args:
            head: Node
            tail_square: NodePair
            node_service: NodeService
            square_validator: SquareValidator

        Returns:
            BuildResult[NodePair]

        Raises:
            NodePairBuildException
        """
        method = f"{cls.__class__.__name__}._build"
        
        # Handle the case that, the head is not certified as safe.
        node_validation_result = node_service.validator.validate(candidate=head)
        if node_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                NodePairBuildException(
                    mthd=method,
                    op=NodePairBuildException.OP,
                    msg=NodePairBuildException.MSG,
                    err_code=NodePairBuildException.ERR_CODE,
                    ex=node_validation_result.exception
                )
            )
        # Handle the case that, the nodePair is not certified as safe.
        tail_square_validation_result = square_validator.validate(candidate=tail_square)
        if tail_square_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                NodePairBuildException(
                    mthd=method,
                    op=NodePairBuildException.OP,
                    msg=NodePairBuildException.MSG,
                    err_code=NodePairBuildException.ERR_CODE,
                    ex=tail_square_validation_result.exception
                )
            )
        # Handle the case that, head.square == tail_square
        if tail_square == head.square:
            # Return the exception chain on failure
            return BuildResult.failure(
                NodePairBuildException(
                    mthd=method,
                    op=NodePairBuildException.OP,
                    msg=NodePairBuildException.MSG,
                    err_code=NodePairBuildException.ERR_CODE,
                    ex=HeadTailSquareException(
                        var="tail_square",
                        val=tail_square.name,
                        msg=HeadTailSquareException.MSG,
                        err_code=HeadTailSquareException.ERR_CODE,
                    )
                )
            )
        # --- Attempt building the tail node. ---#
        tail_node_build_result = node_service.builder.build(
            square=tail_square,
            square_validator=square_validator,
        )
        # Handle the case that, there is no work product.
        if tail_node_build_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                NodePairBuildException(
                    mthd=method,
                    op=NodePairBuildException.OP,
                    msg=NodePairBuildException.MSG,
                    err_code=NodePairBuildException.ERR_CODE,
                    ex=tail_node_build_result.exception
                )
            )
        # --- Send the work product. ---#
        BuildResult.success(NodePair(head=head, tail=tail_node_build_result.payload))
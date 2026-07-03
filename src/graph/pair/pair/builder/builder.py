# src/logic/pair/pair/build/exception.py

"""
Module: logic.pair.pair.build.build
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from model.node import Node, NodeService
from logic.square import Square, SquareValidator
from system import BuildResult, Builder, LoggingLevelRouter
from graph.pair import HeadTailSquareException, Pair, PairBuilderException

class PairBuilder(Builder[Pair]):
    """
     Role:Builder, Data Integrity And Reliability Guarantor

     Responsibilities:
     1.  Produce Pair instances whose integrity and reliability are guaranteed.
     2.  Ensure params for Pair creation have met the application's safety contract.
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
    def build(
            cls,
            head: Node,
            tail_square: Square,
            node_service: NodeService = NodeService(),
            square_validator: SquareValidator = SquareValidator(),
    ) -> BuildResult[Pair]:
        """
        Action:
            1.  If building a node from the tail_square fails send an exception chain in
                the BuildResult.
            2.  If the build was successful
                    *   Build a pair with the head and its new tail.
                    *   Return the work product.
        Args:
            head: Node
            tail_square: Pair
            node_service: NodeService
            square_validator: SquareValidator

        Returns:
            BuildResult[Pair]

        Raises:
            PairBuilderException
        """
        method = f"{cls.__class__.__name__}._build"
        
        # Handle the case that, the head does not pass a validation check.
        node_validation_result = node_service.validator.build(candidate=head)
        if node_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuilderException(
                    cls_mthd=method,
                    op=PairBuilderException.OP,
                    msg=PairBuilderException.MSG,
                    err_code=PairBuilderException.ERR_CODE,
                    ex=node_validation_result.exception
                )
            )
        # Handle the case that, the pair does not pass a validation check.
        tail_square_validation_result = square_validator.build(candidate=tail_square)
        if tail_square_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuilderException(
                    cls_mthd=method,
                    op=PairBuilderException.OP,
                    msg=PairBuilderException.MSG,
                    err_code=PairBuilderException.ERR_CODE,
                    ex=tail_square_validation_result.exception
                )
            )
        # Handle the case that, head.square == tail_square
        if tail_square == head.square:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuilderException(
                    cls_mthd=method,
                    op=PairBuilderException.OP,
                    msg=PairBuilderException.MSG,
                    err_code=PairBuilderException.ERR_CODE,
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
                PairBuilderException(
                    cls_mthd=method,
                    op=PairBuilderException.OP,
                    msg=PairBuilderException.MSG,
                    err_code=PairBuilderException.ERR_CODE,
                    ex=tail_node_build_result.exception
                )
            )
        # --- Send the work product. ---#
        BuildResult.success(Pair(head=head, tail=tail_node_build_result.payload))
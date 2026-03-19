# src/logic/pair/pair/builder/process.py

"""
Module: logic.pair.pair.builder.builder
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations

from logic.node import Node, NodeService
from logic.square import Square, SquareValidationProcess
from logic.system import BuildResult, BuildProcess, LoggingLevelRouter
from logic.pair import HeadTailSquareException, Pair, PairBuildException

class PairBuildProcess(BuildProcess[Pair]):
    """
     Role:BuildProcess, Data Integrity And Reliability Guarantor

     Responsibilities:
     1.  Produce Pair instances whose integrity and reliability are guaranteed.
     2.  Ensure params for Pair creation have met the application's safety contract.
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
            head: Node,
            tail_square: Square,
            node_service: NodeService = NodeService(),
            square_validator: SquareValidationProcess = SquareValidationProcess(),
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
            square_validator: SquareValidationProcess

        Returns:
            BuildResult[Pair]

        Raises:
            PairBuildException
        """
        method = f"{cls.__class__.__name__}._build"
        
        # Handle the case that, the head is not certified as safe.
        node_validation_result = node_service.validation.execute(candidate=head)
        if node_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuildException(
                    mthd=method,
                    op=PairBuildException.OP,
                    msg=PairBuildException.MSG,
                    err_code=PairBuildException.ERR_CODE,
                    ex=node_validation_result.exception
                )
            )
        # Handle the case that, the pair is not certified as safe.
        tail_square_validation_result = square_validator.execute(candidate=tail_square)
        if tail_square_validation_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuildException(
                    mthd=method,
                    op=PairBuildException.OP,
                    msg=PairBuildException.MSG,
                    err_code=PairBuildException.ERR_CODE,
                    ex=tail_square_validation_result.exception
                )
            )
        # Handle the case that, head.square == tail_square
        if tail_square == head.square:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuildException(
                    mthd=method,
                    op=PairBuildException.OP,
                    msg=PairBuildException.MSG,
                    err_code=PairBuildException.ERR_CODE,
                    ex=HeadTailSquareException(
                        var="tail_square",
                        val=tail_square.name,
                        msg=HeadTailSquareException.MSG,
                        err_code=HeadTailSquareException.ERR_CODE,
                    )
                )
            )
        # --- Attempt building the tail node. ---#
        tail_node_build_result = node_service.build.execute(
            square=tail_square,
            square_validator=square_validator,
        )
        # Handle the case that, there is no work product.
        if tail_node_build_result.is_failure:
            # Return the exception chain on failure
            return BuildResult.failure(
                PairBuildException(
                    mthd=method,
                    op=PairBuildException.OP,
                    msg=PairBuildException.MSG,
                    err_code=PairBuildException.ERR_CODE,
                    ex=tail_node_build_result.exception
                )
            )
        # --- Send the work product. ---#
        BuildResult.success(Pair(head=head, tail=tail_node_build_result.payload))
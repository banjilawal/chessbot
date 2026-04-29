# src/operation/finalize/finalize.py

"""
Module: operation.finalize.finalize
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import FinalizeSquareBuildException
from model import Square
from operation import AssemblyFinalizer
from result import BuildResult
from util import LoggingLevelRouter


class SquareAssemblyFinalizer(AssemblyFinalizer[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Square instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(product: Square, ) -> BuildResult[Square]:

     Super Class:
         Builder
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: Square, ) -> BuildResult[Square]:
        
        method = f"{cls.__name__}.execute"
        board = product.board
        insertion_result = board.squares.insert(item=product)
       # Handle the case that, the square is not successfully registered with its board.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                FinalizeSquareBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=FinalizeSquareBuildException.MSG,
                    err_code=FinalizeSquareBuildException.ERR_CODE,
                    ex=insertion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)

# Register the operation.
WorkerRegistryController.register(worker=SquareAssemblyFinalizer)
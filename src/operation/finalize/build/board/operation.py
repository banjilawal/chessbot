# src/operation/finalize/finalize.py

"""
Module: operation.finalize.finalize
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import FinalizeBoardBuildException
from model import Board
from operation import AssemblyFinalizer
from result import BuildResult
from system import LoggingLevelRouter


class BoardAssemblyFinalizer(AssemblyFinalizer[Board]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: Board, area_binder_service: ArenaBinderService) -> BuildResult[Board]:
        method = f"{cls.__name__}.execute"
        
        arena = product.arena
        if product != arena.binder.board:
            update_result = arena_binder_service.update_board(arena_binder=arena.binder, board=product)
            # Handle the case that, the board is not successfully registered with its arena.
            if insertion_result.is_failure:
                return BuildResult.failure(
                    FinalizeBoardBuildException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=FinalizeBoardBuildException.MSG,
                        err_code=FinalizeBoardBuildException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
            
        
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)
        
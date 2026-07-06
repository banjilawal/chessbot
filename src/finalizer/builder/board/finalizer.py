# src/finalizer/builder/board/finalizer.py

"""
Module: finalizer.builder.board.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import FinalizeBoardBuilderException
from model import Board
from operation import BuilderFinalizer
from result import BuildResult
from util import LoggingLevelRouter


class BoardBuilderFinalizer(BuilderFinalizer[Board]):
    
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
                    FinalizeBoardBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=FinalizeBoardBuilderException.MSG,
                        err_code=FinalizeBoardBuilderException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
            
        
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)
    
# Register the operation.
WorkerRegistryController.register_worker(worker=BoardBuilderFinalizer)
        
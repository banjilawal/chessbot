# src/builder/binder/builder.py

"""
Module: builder.binder.builder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from microservice import BoardService
from model import Board, BoardBinder
from operation.priming.build.binder.wrapper import TeamBinderBuilderException
from operation import Assemble
from result import BuildResult
from system import LoggingLevelRouter


class TeamBinderBuilder(Assemble[BoardBinder]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            board: Board,
            board_service: BoardService,
    ) -> BuildResult[BoardBinder]:
        method = f"{cls.__name__}.builder"
        
        # Handle the case that, board fails a validation check.
        board_validation_result = board_service.validator.build(board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamBinderBuilderException.MSG,
                    err_code=TeamBinderBuilderException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        return BuildResult.success(BoardBinder(board=board))
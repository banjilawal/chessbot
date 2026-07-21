# src/builder/model/binder/builder.py

"""
Module: builder.model.binder.builder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from microservice import BoardService
from model import Board, BoardBinder
from bootstrapper import TeamBinderBuilderException
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
        board_validator_result = board_service.validator.execute(board)
        if board_validator_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamBinderBuilderException.MSG,
                    err_code=TeamBinderBuilderException.ERR_CODE,
                    ex=board_validator_result.exception,
                )
            )
        return BuildResult.success(BoardBinder(board=board))
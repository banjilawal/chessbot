# src/integrity/build/binder/builder.py

"""
Module: integrity.build.binder.builder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from microservice import BoardService
from model import Board, TeamBinder
from operation.bootstrap.build.binder.wrapper import TeamBinderBuildException
from operation import Assemble
from result import BuildResult
from system import LoggingLevelRouter


class TeamBinderBuilder(Assemble[TeamBinder]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            board: Board,
            board_service: BoardService,
    ) -> BuildResult[TeamBinder]:
        method = f"{cls.__name__}.builder"
        
        # Handle the case that, board fails a validation check.
        board_validation_result = board_service.validator.validate(board)
        if board_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TeamBinderBuildException.MSG,
                    err_code=TeamBinderBuildException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
        return BuildResult.success(TeamBinder(board=board))
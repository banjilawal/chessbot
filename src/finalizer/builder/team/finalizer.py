# src/finalizer/builder/team/finalizer.py

"""
Module: finalizer.builder.team.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import FinalizeTeamBuilderException
from model import Team
from operation import BuilderFinalizer
from result import BuildResult
from util import LoggingLevelRouter


class TeamBuilderFinalizer(BuilderFinalizer[Team]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: Team,) -> BuildResult[Team]:
        method = f"{cls.__name__}.execute"
        
        owner = product.owner
        insertion_result = owner.teams.insert(product)
        if insertion_result.is_failure:
            # Handle the case that, the team is not successfully registered with its team.
            return BuildResult.failure(
                FinalizeTeamBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=FinalizeTeamBuilderException.MSG,
                    err_code=FinalizeTeamBuilderException.ERR_CODE,
                    ex=insertion_result.exception,
                )
        )
        board = product.board
        board.binder_controller.binder.satellite_table[product.schema] = product
        
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)

# Register the operation.
WorkerRegistryController.register_worker(worker=TeamBuilderFinalizer)
        
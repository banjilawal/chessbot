# src/operation/finalize/finalize.py

"""
Module: operation.finalize.finalize
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import FinalizeTeamBuildException
from model import Team
from operation import AssemblyFinalizer
from result import BuildResult
from system import LoggingLevelRouter


class TeamAssemblyFinalizer(AssemblyFinalizer[Team]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: Team,) -> BuildResult[Team]:
        method = f"{cls.__name__}.execute"
        
        owner = product.owner
        insertion_result = owner.teams.insert(product)
        if insertion_result.is_failure:
            # Handle the case that, the team is not successfully registered with its team.
            return BuildResult.failure(
                FinalizeTeamBuildException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=FinalizeTeamBuildException.MSG,
                    err_code=FinalizeTeamBuildException.ERR_CODE,
                    ex=insertion_result.exception,
                )
        )
        board = product.board
        board.binder_controller.binder.satellite_table[product.schema] = product
            
        
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)
        
# src/operation/finalize/finalize.py

"""
Module: operation.finalize.finalize
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from err import FinalizeTokenBuildException
from model import Token
from operation import AssemblyFinalizer
from result import BuildResult
from system import LoggingLevelRouter


class TokenAssemblyFinalizer(AssemblyFinalizer[Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, product: Token,) -> BuildResult[Token]:
        method = f"{cls.__name__}.execute"
        
        team = product.team
        if product not in team.roster:
            insertion_result = team.roster.insert(item=product)
            # Handle the case that, the token is not successfully registered with its team.
            if insertion_result.is_failure:
                return BuildResult.failure(
                    FinalizeTokenBuildException(
                        cls_mthd=method,
                        cls_name=method.__name__,
                        msg=FinalizeTokenBuildException.MSG,
                        err_code=FinalizeTokenBuildException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)
        
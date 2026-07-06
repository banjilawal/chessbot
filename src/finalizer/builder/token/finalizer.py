# src/finalizer/builder/token/finalizer.py

"""
Module: finalizer.builder.token.finalizer
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import WorkerRegistryController
from err import FinalizeTokenBuilderException
from model import Token
from operation import BuilderFinalizer, TokenAssembler
from result import BuildResult
from util import LoggingLevelRouter


class TokenBuilderFinalizer(BuilderFinalizer[Token]):
    
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
                    FinalizeTokenBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=FinalizeTokenBuilderException.MSG,
                        err_code=FinalizeTokenBuilderException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(product)

# Register the operation.
WorkerRegistryController.register_worker(worker=TokenAssembler)
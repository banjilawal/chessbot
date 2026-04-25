# src/pipeline/build/token/pipeline.py

"""
Module: pipeline.build.token.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import TokenBuildPipelineException
from model import Token, TokenBlueprint
from operation import TokenAssembler, TokenAssemblyBootstrapper, TokenAssemblyFinalizer
from pipeline import BuildPipeline
from result import BuildResult
from system import LoggingLevelRouter
from toolkit import TokenToolkit


class TokenBuildPipeline(BuildPipeline[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Workers:
        -   Workers are the logic that implements a process.
        -   Processes produce a result.
        
        Naming Problems:
            -   Don't have a good naming convention for workers yet. Maybe <ProcessName>Worker? as default,
                if it's not clunky.
            -   Worker entry points are named execute. Might change them to work() and the work executes the process.
            
            Exceptions:
                -   Exceptions are only about the process.
                -   Exception naming convention is <ProcessName>Exception.

        Transaction Worker:
            -   Work on stateful data objects.
            -   Include a data object's previous state in their work product.
            -   For simplicity, speed, and side-effect avoidance use deep copy before state changing logic.
            -   Client uses original data for rollbacks if transaction fails.
   
        Build Worker Naming:
            -   Builders are a core workers in the system.
            -   The least clunky and intuitive schema is <EntityName>Builder.
            -   Developers might assume other process exceptions are about the worker and use confusing naming
                conventions for other processes and their exceptions.
            -   Despite the possible confusion <EntityName>Builder naming is worth the trade off.
        
    Responsibilities:
        1.  Creation process owners.
        2.  Execute binding logic for related entities.
        3.  Assure objects comply with business logic at point of creation.
        4.  Ensure stateful data-holding build resources meet satisfy contracts.
    
    Attributes:

    Provides:
        -   build(*args, **kwargs) -> BuildResult[Token]
        
    Super Class:
    """
    _assembler: TokenAssembler
    _finalizer: TokenAssemblyFinalizer
    _bootstrapper: TokenAssemblyBootstrapper

    def __init__(
            self,
            assembler: TokenAssembler | None = None,
            finalizer: TokenAssemblyFinalizer | None = None,
            bootstrapper: TokenAssemblyFinalizer | None = None,
    ):
        self._assembler = assembler or TokenAssembler()
        self._finalizer = finalizer or TokenAssemblyFinalizer()
        self._bootstrapper = bootstrapper or TokenAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def build(self, blueprint: TokenBlueprint, toolkit: TokenToolkit) -> BuildResult[Token]:
        method = f"{self.__class__.__name__}.build"
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        if bootstrap_result.is_failure:
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        if assembly_result.is_failure:
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        final_result = self._finalizer.execute(product=assembly_result.payload)
        if final_result.is_failure:
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        return BuildResult.success(final_result.payload)
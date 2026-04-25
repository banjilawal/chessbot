# src/pipeline/build/arena/pipeline.py

"""
Module: pipeline.build.arena.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import ArenaToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Arena, ArenaBlueprint
from err import ArenaBuildPipelineException
from operation import ArenaAssembler, ArenaAssemblyBootstrapper, ArenaAssemblyFinalizer


class ArenaBuildPipeline(BuildPipeline[Arena]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Arena build lifecycle.
    
    Attributes:
        assembler: ArenaAssembler
        finalizer: ArenaAssemblyFinalizer
        bootstrapper: ArenaAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: ArenaBlueprint, toolkit: ArenaToolkit) -> BuildResult[Arena]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: ArenaAssembler
    _finalizer: ArenaAssemblyFinalizer
    _bootstrapper: ArenaAssemblyBootstrapper

    def __init__(
            self,
            assembler: ArenaAssembler | None = None,
            finalizer: ArenaAssemblyFinalizer | None = None,
            bootstrapper: ArenaAssemblyFinalizer | None = None,
    ):
        """
        Args:
            assembler: ArenaAssembler
            finalizer: ArenaAssemblyFinalizer
            bootstrapper: ArenaAssemblyBootstrapper
        """
        self._assembler = assembler or ArenaAssembler()
        self._finalizer = finalizer or ArenaAssemblyFinalizer()
        self._bootstrapper = bootstrapper or ArenaAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: ArenaBlueprint, toolkit: ArenaToolkit) -> BuildResult[Arena]:
        """
        Builds a safe, consistent Arena.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Arena build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: ArenaBlueprint
            toolkit: ArenaToolkit
        Returns:
            BuildResult[Arena]
        Raises:
            ArenaBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Arena's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                ArenaBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildPipelineException.MSG,
                    err_code=ArenaBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Arena from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the arena assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                ArenaBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildPipelineException.MSG,
                    err_code=ArenaBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Run the consistency assurance operations on the arena. ---#
        final_result = self._finalizer.execute(product=assembly_result.payload)
        # Handle the case that the arena's relationships are not established.
        if final_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                ArenaBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildPipelineException.MSG,
                    err_code=ArenaBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(final_result.payload)
# src/pipeline/build/vector/pipeline.py

"""
Module: pipeline.build.vector.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import MathToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Vector, VectorBlueprint
from err import VectorBuildPipelineException
from operation import VectorAssembler, VectorAssemblyBootstrapper


class VectorBuildPipeline(BuildPipeline[Vector]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Vector build lifecycle.
    
    Attributes:
        assembler: VectorAssembler
        bootstrapper: VectorAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: VectorBlueprint, toolkit: MathToolkit) -> BuildResult[Vector]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: VectorAssembler
    _bootstrapper: VectorAssemblyBootstrapper

    def __init__(
            self,
            assembler: VectorAssembler | None = None,
            bootstrapper: VectorAssemblyBootstrapper | None = None,
    ):
        """
        Args:
            assembler: VectorAssembler
            bootstrapper: VectorAssemblyBootstrapper
        """
        self._assembler = assembler or VectorAssembler()
        self._bootstrapper = bootstrapper or VectorAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: VectorBlueprint, toolkit: MathToolkit) -> BuildResult[Vector]:
        """
        Builds a safe, consistent Vector.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Vector build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: VectorBlueprint
            toolkit: MathToolkit
        Returns:
            BuildResult[Vector]
        Raises:
            VectorBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Vector's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                VectorBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildPipelineException.MSG,
                    err_code=VectorBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Vector from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the vector assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                VectorBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildPipelineException.MSG,
                    err_code=VectorBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(assembly_result.payload)
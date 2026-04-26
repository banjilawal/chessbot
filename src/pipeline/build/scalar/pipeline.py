# src/pipeline/build/scalar/pipeline.py

"""
Module: pipeline.build.scalar.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import MathToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Scalar, ScalarBlueprint
from err import ScalarBuildPipelineException
from operation import ScalarAssembler, ScalarAssemblyBootstrapper


class ScalarBuildPipeline(BuildPipeline[Scalar]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Scalar build lifecycle.
    
    Attributes:
        assembler: ScalarAssembler
        bootstrapper: ScalarAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: ScalarBlueprint, toolkit: MathToolkit) -> BuildResult[Scalar]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: ScalarAssembler
    _bootstrapper: ScalarAssemblyBootstrapper

    def __init__(
            self,
            assembler: ScalarAssembler | None = None,
            bootstrapper: ScalarAssemblyBootstrapper | None = None,
    ):
        """
        Args:
            assembler: ScalarAssembler
            bootstrapper: ScalarAssemblyBootstrapper
        """
        self._assembler = assembler or ScalarAssembler()
        self._bootstrapper = bootstrapper or ScalarAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: ScalarBlueprint, toolkit: MathToolkit) -> BuildResult[Scalar]:
        """
        Builds a safe, consistent Scalar.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Scalar build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: ScalarBlueprint
            toolkit: MathToolkit
        Returns:
            BuildResult[Scalar]
        Raises:
            ScalarBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Scalar's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                ScalarBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildPipelineException.MSG,
                    err_code=ScalarBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Scalar from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the scalar assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                ScalarBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildPipelineException.MSG,
                    err_code=ScalarBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(assembly_result.payload)
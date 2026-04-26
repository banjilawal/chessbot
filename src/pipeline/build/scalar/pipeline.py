# src/pipeline/build/scalar/pipeline.py

"""
Module: pipeline.build.scalar.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from result import BuildResult
from pipeline import BuildPipeline
from operation import ScalaAssembler
from system import LoggingLevelRouter
from model import Scalar, ScalarBlueprint
from err import ScalarBuildPipelineException
from toolkit import ScalarToolkit


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
        
    Provides:
        -   def run(blueprint: ScalarBlueprint, toolkit: ScalarToolkit) -> BuildResult[Scalar]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: ScalaAssembler
    _toolkit: ScalarToolkit

    def __init__(
            self,
            assembler: ScalaAssembler | None = None,
            toolkit: ScalarToolkit | None = None,
    ):
        """
        Args:
            assembler: ScalarAssembler
        """
        self._assembler = assembler or ScalaAssembler()
        self._toolkit = toolkit or ScalarToolkit()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: ScalarBlueprint) -> BuildResult[Scalar]:
        """
        Builds a safe, consistent Scalar.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Scalar build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: ScalarBlueprint
            toolkit: ScalarToolkit
        Returns:
            BuildResult[Scalar]
        Raises:
            ScalarBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Assemble the Scalar from the verified build params. ---#
        assembly_result = self._assembler.execute(
            blueprint=blueprint,
            toolkit=self._toolkit,
        )
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
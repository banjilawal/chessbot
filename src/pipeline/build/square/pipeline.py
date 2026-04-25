# src/pipeline/build/square/pipeline.py

"""
Module: pipeline.build.square.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import SquareToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Square, SquareBlueprint
from err import SquareBuildPipelineException
from operation import SquareAssembler, SquareAssemblyBootstrapper, SquareAssemblyFinalizer


class SquareBuildPipeline(BuildPipeline[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Square build lifecycle.
    
    Attributes:
        assembler: SquareAssembler
        finalizer: SquareAssemblyFinalizer
        bootstrapper: SquareAssemblyBootstrapper
        
    Provides:
        -   def build(blueprint: SquareBlueprint, toolkit: SquareToolkit) -> BuildResult[Square]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: SquareAssembler
    _finalizer: SquareAssemblyFinalizer
    _bootstrapper: SquareAssemblyBootstrapper

    def __init__(
            self,
            assembler: SquareAssembler | None = None,
            finalizer: SquareAssemblyFinalizer | None = None,
            bootstrapper: SquareAssemblyFinalizer | None = None,
    ):
        """
        Args:
            assembler: SquareAssembler
            finalizer: SquareAssemblyFinalizer
            bootstrapper: SquareAssemblyBootstrapper
        """
        self._assembler = assembler or SquareAssembler()
        self._finalizer = finalizer or SquareAssemblyFinalizer()
        self._bootstrapper = bootstrapper or SquareAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def build(self, blueprint: SquareBlueprint, toolkit: SquareToolkit) -> BuildResult[Square]:
        """
        Builds a safe, consistent Square.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Square build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: SquareBlueprint
            toolkit: SquareToolkit
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Square's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                SquareBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildPipelineException.MSG,
                    err_code=SquareBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Square from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the square assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                SquareBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildPipelineException.MSG,
                    err_code=SquareBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Run the consistency assurance operations on the square. ---#
        final_result = self._finalizer.execute(product=assembly_result.payload)
        # Handle the case that the square's relationships are not established.
        if final_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                SquareBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildPipelineException.MSG,
                    err_code=SquareBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(final_result.payload)
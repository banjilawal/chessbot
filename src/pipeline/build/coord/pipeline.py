# src/pipeline/build/coord/pipeline.py

"""
Module: pipeline.build.coord.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import MathToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Coord, CoordBlueprint
from err import CoordBuildPipelineException
from operation import CoordAssembler, CoordAssemblyBootstrapper


class CoordBuildPipeline(BuildPipeline[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Coord build lifecycle.
    
    Attributes:
        assembler: CoordAssembler
        bootstrapper: CoordAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: CoordBlueprint, toolkit: MathToolkit) -> BuildResult[Coord]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: CoordAssembler
    _bootstrapper: CoordAssemblyBootstrapper

    def __init__(
            self,
            assembler: CoordAssembler | None = None,
            bootstrapper: CoordAssemblyBootstrapper | None = None,
    ):
        """
        Args:
            assembler: CoordAssembler
            bootstrapper: CoordAssemblyBootstrapper
        """
        self._assembler = assembler or CoordAssembler()
        self._bootstrapper = bootstrapper or CoordAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: CoordBlueprint, toolkit: MathToolkit) -> BuildResult[Coord]:
        """
        Builds a safe, consistent Coord.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Coord build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: CoordBlueprint
            toolkit: MathToolkit
        Returns:
            BuildResult[Coord]
        Raises:
            CoordBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Coord's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                CoordBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildPipelineException.MSG,
                    err_code=CoordBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Coord from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the coord assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                CoordBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildPipelineException.MSG,
                    err_code=CoordBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(assembly_result.payload)
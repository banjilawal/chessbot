# src/pipeline/build/board/pipeline.py

"""
Module: pipeline.build.board.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import BoardToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Board, BoardBlueprint
from err import BoardBuildPipelineException
from operation import BoardAssembler, BoardAssemblyBootstrapper, BoardAssemblyFinalizer


class BoardBuildPipeline(BuildPipeline[Board]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Board build lifecycle.
    
    Attributes:
        assembler: BoardAssembler
        finalizer: BoardAssemblyFinalizer
        bootstrapper: BoardAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: BoardBlueprint, toolkit: BoardToolkit) -> BuildResult[Board]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: BoardAssembler
    _finalizer: BoardAssemblyFinalizer
    _bootstrapper: BoardAssemblyBootstrapper
    _toolkit: BoardToolkit

    def __init__(
            self,
            assembler: BoardAssembler | None = None,
            finalizer: BoardAssemblyFinalizer | None = None,
            bootstrapper: BoardAssemblyFinalizer | None = None,
            toolkit: BoardToolkit | None = None,
    ):
        """
        Args:
            assembler: BoardAssembler
            finalizer: BoardAssemblyFinalizer
            bootstrapper: BoardAssemblyBootstrapper
        """
        self._assembler = assembler or BoardAssembler()
        self._finalizer = finalizer or BoardAssemblyFinalizer()
        self._bootstrapper = bootstrapper or BoardAssemblyBootstrapper()
        self._toolkit = toolkit or BoardToolkit()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: BoardBlueprint, toolkit: BoardToolkit) -> BuildResult[Board]:
        """
        Builds a safe, consistent Board.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Board build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: BoardBlueprint
            toolkit: BoardToolkit
        Returns:
            BuildResult[Board]
        Raises:
            BoardBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Board's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=self._toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                BoardBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildPipelineException.MSG,
                    err_code=BoardBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Board from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the board assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                BoardBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildPipelineException.MSG,
                    err_code=BoardBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Run the consistency assurance operations on the board. ---#
        final_result = self._finalizer.execute(product=assembly_result.payload)
        # Handle the case that the board's relationships are not established.
        if final_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                BoardBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildPipelineException.MSG,
                    err_code=BoardBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(final_result.payload)
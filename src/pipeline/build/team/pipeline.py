# src/pipeline/build/team/pipeline.py

"""
Module: pipeline.build.team.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import TeamToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Team, TeamBlueprint
from err import TeamBuildPipelineException
from operation import TeamAssembler, TeamAssemblyBootstrapper, TeamAssemblyFinalizer


class TeamBuildPipeline(BuildPipeline[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Team build lifecycle.
    
    Attributes:
        assembler: TeamAssembler
        finalizer: TeamAssemblyFinalizer
        bootstrapper: TeamAssemblyBootstrapper
        
    Provides:
        -   def build(blueprint: TeamBlueprint, toolkit: TeamToolkit) -> BuildResult[Team]:
        
    Super Class:
        BuildPipeline
    """
    _assembler: TeamAssembler
    _finalizer: TeamAssemblyFinalizer
    _bootstrapper: TeamAssemblyBootstrapper

    def __init__(
            self,
            assembler: TeamAssembler | None = None,
            finalizer: TeamAssemblyFinalizer | None = None,
            bootstrapper: TeamAssemblyFinalizer | None = None,
    ):
        """
        Args:
            assembler: TeamAssembler
            finalizer: TeamAssemblyFinalizer
            bootstrapper: TeamAssemblyBootstrapper
        """
        self._assembler = assembler or TeamAssembler()
        self._finalizer = finalizer or TeamAssemblyFinalizer()
        self._bootstrapper = bootstrapper or TeamAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def build(self, blueprint: TeamBlueprint, toolkit: TeamToolkit) -> BuildResult[Team]:
        """
        Builds a safe, consistent Team.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Team build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TeamBlueprint
            toolkit: TeamToolkit
        Returns:
            BuildResult[Team]
        Raises:
            TeamBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Team's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TeamBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildPipelineException.MSG,
                    err_code=TeamBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Team from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the team assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TeamBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildPipelineException.MSG,
                    err_code=TeamBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Run the consistency assurance operations on the team. ---#
        final_result = self._finalizer.execute(product=assembly_result.payload)
        # Handle the case that the team's relationships are not established.
        if final_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TeamBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildPipelineException.MSG,
                    err_code=TeamBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(final_result.payload)
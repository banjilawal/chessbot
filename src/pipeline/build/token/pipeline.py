# src/pipeline/build/token/pipeline.py

"""
Module: pipeline.build.token.pipeline
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import BuildResult
from toolkit import TokenToolkit
from pipeline import BuildPipeline
from system import LoggingLevelRouter
from model import Token, TokenBlueprint
from err import TokenBuildPipelineException
from operation import TokenAssembler, TokenAssemblyBootstrapper, TokenAssemblyFinalizer


class TokenBuildPipeline(BuildPipeline[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
       
    Responsibilities:
        1.  Runs the Token build lifecycle.
    
    Attributes:
        assembler: TokenAssembler
        finalizer: TokenAssemblyFinalizer
        bootstrapper: TokenAssemblyBootstrapper
        
    Provides:
        -   def run(blueprint: TokenBlueprint, toolkit: TokenToolkit) -> BuildResult[Token]:
        
    Super Class:
        BuildPipeline
    """
    _toolkit: TokenToolkit
    _assembler: TokenAssembler
    _finalizer: TokenAssemblyFinalizer
    _bootstrapper: TokenAssemblyBootstrapper

    def __init__(
            self,
            toolkit: TokenToolkit | None = None,
            assembler: TokenAssembler | None = None,
            finalizer: TokenAssemblyFinalizer | None = None,
            bootstrapper: TokenAssemblyFinalizer | None = None,
    ):
        """
        Args:
            toolkit: TokenToolkit
            assembler: TokenAssembler
            finalizer: TokenAssemblyFinalizer
            bootstrapper: TokenAssemblyBootstrapper
        """
        self._toolkit = toolkit or TokenToolkit()
        self._assembler = assembler or TokenAssembler()
        self._finalizer = finalizer or TokenAssemblyFinalizer()
        self._bootstrapper = bootstrapper or TokenAssemblyBootstrapper()

    @LoggingLevelRouter.monitor
    def run(self, blueprint: TokenBlueprint,) -> BuildResult[Token]:
        """
        Builds a safe, consistent Token.
        
        Action:
            1.  Send an exception chain in the BuildResult any operation in the Token build process
                fails.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuildPipelineException
        """
        method = f"{self.__class__.__name__}.build"
        
        # --- Verify the Token's build params. ---#
        bootstrap_result = self._bootstrapper.execute(
            blueprint=blueprint,
            toolkit=self._toolkit
        )
        # Handle the case that the bootstrapper flags an build param.
        if bootstrap_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Assemble the Token from the verified build params. ---#
        assembly_result = self._assembler.execute(blueprint=bootstrap_result.payload)
        # Handle the case that the token assembly is not successful.
        if assembly_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Run the consistency assurance operations on the token. ---#
        final_result = self._finalizer.execute(product=assembly_result.payload)
        # Handle the case that the token's relationships are not established.
        if final_result.is_failure:
            # Return the exception on failure.
            return BuildResult.failure(
                TokenBuildPipelineException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildPipelineException.MSG,
                    err_code=TokenBuildPipelineException.ERR_CODE,
                    ex=final_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(final_result.payload)
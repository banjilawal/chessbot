# src/builder/model/team/builder.py

"""
Module: builder.model.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import TeamBlueprint
from builder import ModelBuilder
from err import TeamBuilderException
from model import Team
from operation import TeamAssembler
from finalizer import TeamAssemblyFinalizer
from result import BuildResult
from err.root import TeamRootCertifier
from toolkit import TeamToolkit
from util import LoggingLevelRouter
from validator import TeamCertifier


class TeamBuilder(ModelBuilder[Team]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
        
   Responsibilities:
        1.  Ensure a new Team instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Team]

     Super Class:
         Builder
     """
    _bootstrapper: TeamCertifier
    _assembler: TeamAssembler
    _finalizer: TeamAssemblyFinalizer
    _toolkit: TeamToolkit
    
    def __init__(
            self,
            bootstrapper: TeamCertifier | None = None,
            assembler : TeamAssembler | None = None,
            finalizer: TeamAssemblyFinalizer | None = None,
            toolkit: TeamToolkit | None = None,
    ):
        self._bootstrapper = bootstrapper or TeamRootCertifier()
        self._assembler = assembler or TeamAssembler()
        self._finalizer = finalizer or TeamAssemblyFinalizer()
        self._toolkit = toolkit or TeamToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TeamBlueprint, ) -> BuildResult[Team]:
        """
        Build a safe Team.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur:
                    -   The blueprint is not validated.
                    -   The team cannot be assembled from the blueprint.
                    -   An error occurs during the clean up.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TeamBlueprint
            blueprint_validator: Certifier
            assembler: TeamAssembler
            finalizer: TeamAssemblyFinalizer
        Returns:
            BuildResult[Team]
        Raises:
            TeamBuilderException
        """
        method = f"{cls.__name__}.build"
        

        bootstrap = self._bootstrapper.execute(
            candidate=blueprint,
            toolkit=self._toolkit,
        )
        # Handle the case that, the bootstrap is not successful.
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self._assembler.execute(
            blueprint=cast(TeamBlueprint, bootstrap.payload)
        )
        # Handle the case that, the assembly is not completed.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    ex=assembly.exception,
                )
            )
        # --- Handoff the product for consistency and other finalization steps. ---#
        finalization_result = self._finalizer.execute(
            product=assembly_result.payload
        )
        # Handle the case that, the clean is not successful.
        if finalization_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    ex=finalization_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(finalization_result.payload)


        
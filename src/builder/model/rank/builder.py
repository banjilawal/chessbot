# src/builder/model/rank/builder.py

"""
Module: builder.model.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import RankBlueprint
from builder import ModelBuilder
from err import RankBuildRouteException, RankBuilderException
from model import Bishop, King, Knight, Pawn, Queen, Rank, Rook
from result import BuildResult
from schema import Persona


class RankBuilder(ModelBuilder[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

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
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    _bootstrapper: RankCertifier
    
    def __init__(self, bootstrapper: RankCertifier | None = RankRootCertifier()):
        self._bootstrapper = bootstrapper
        
    

    @LoggingLevelRouter.monitor
    def execute(self, blueprint: RankBlueprint) -> BuildResult:
        """
        Build a concrete Rank base on the Person instance.

        Args:
            blueprint: RankBlueprint
        Raises:
          BuildResult
        Raises:
            RankBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the persona does not pass a validation check.
        bootstrap = self._bootstrapper.execute(blueprint)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuilderException.MSG,
                    err_code=RankBuilderException.ERR_CODE,
                    ex=bootstrap.exception
                )
            )
        # --- Route to the appropriate concrete builder. ---#
        
        # Entry point into building a King instance.
        if blueprint.persona == Persona.KING:
            return BuildResult.success(King(persona=blueprint.persona))
        # Entry point into building a Pawn instance.
        if blueprint.persona == Persona.PAWN:
            return BuildResult.success(Pawn( persona=blueprint.persona))
        # Entry point into building a Knight instance.
        if blueprint.persona == Persona.KNIGHT:
            return BuildResult.success(Knight(persona=blueprint.persona))
        # Entry point into building a Bishop instance.
        if blueprint.persona == Persona.BISHOP:
            return BuildResult.success(Bishop(persona=blueprint.persona))
        # Entry point into building a Rook instance.
        if blueprint.persona == Persona.ROOK:
            return BuildResult.success(Rook(persona=blueprint.persona))
        # Entry point into building a Queen instance.
        if blueprint.persona == Persona.QUEEN:
            return BuildResult.success(Queen(persona=blueprint.persona))
            
        # If there is no build path exists for a persona, Return an exception chain.
        return BuildResult.failure(
            RankBuilderException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=RankBuilderException.MSG,
                err_code=RankBuilderException.ERR_CODE,
                ex=RankBuildRouteException(
                    var="persona",
                    val=f"{blueprint.persona}",
                    msg=RankBuildRouteException.MSG,
                    err_code=RankBuildRouteException.ERR_CODE,
                )
            )
        )
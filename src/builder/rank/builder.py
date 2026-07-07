# src/builder/rank/builder.py

"""
Module: builder.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from schema.persona import Persona, PersonaService
from system import Builder, BuildResult, LoggingLevelRouter, id_emitter
from logic.rank import (
    Bishop, King, Knight, Pawn, Queen, Rank, RankBuilderException, RankBuildRouteException,
    RankFactoryException, Rook
)

class RankBuilder(Builder[Rank]):
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            persona: Persona,
            id: int = id_emitter.rank_id,
            persona_service: PersonaService = PersonaService(),
    ) -> BuildResult[Rank]:
        """
        Build a concrete Rank base on the Person instance.

        Args:
            id: int
            persona: Persona
            persona_service: PersonaService

        Raises:
          BuildResult[Rank]

        Raises:
            RankBuilderException
            RankFactoryException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the persona does not pass a validation check.
        validation_result = persona_service.run.build(candidate=persona)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankFactoryException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankFactoryException.MSG,
                    err_code=RankFactoryException.ERR_CODE,
                    ex=RankBuilderException(
                        cls_mthd=method,
                        op=RankBuilderException.OP,
                        msg=RankBuilderException.MSG,
                        err_code=RankBuilderException.ERR_CODE,
                        mthd_rslt_type=RankBuilderException.MTHD_RSLT,
                        ex=validation_result.exception
                    )
                )
            )
        # --- Route to the appropriate concrete builder. ---#
        
        # Entry point into building a King instance.
        if persona == Persona.KING:
            return BuildResult.success(King(id=id, persona=persona))
        # Entry point into building a Pawn instance.
        if persona == Persona.PAWN:
            return BuildResult.success(Pawn(id=id, persona=persona))
        # Entry point into building a Knight instance.
        if persona == Persona.KNIGHT:
            return BuildResult.success(Knight(id=id, persona=persona))
        # Entry point into building a Bishop instance.
        if persona == Persona.BISHOP:
            return BuildResult.success(Bishop(id=id, persona=persona))
        # Entry point into building a Rook instance.
        if persona == Persona.ROOK:
            return BuildResult.success(Rook(id=id, persona=persona))
        # Entry point into building a Queen instance.
        if persona == Persona.QUEEN:
            return BuildResult.success(Queen(id=id, persona=persona))
            
        # If there is no build path exists for a persona, Return an exception chain.
        return BuildResult.failure(
            RankFactoryException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=RankFactoryException.MSG,
                err_code=RankFactoryException.ERR_CODE,
                ex=RankBuilderException(
                    cls_mthd=method,
                    op=RankBuilderException.OP,
                    msg=RankBuilderException.MSG,
                    err_code=RankBuilderException.ERR_CODE,
                    mthd_rslt_type=RankBuilderException.MTHD_RSLT,
                    ex=RankBuildRouteException(
                        var="persona",
                        val=f"{persona}",
                        msg=RankBuildRouteException.MSG,
                        err_code=RankBuildRouteException.ERR_CODE,
                    )
                )
            )
        )
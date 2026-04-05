# src/integrity/build/rank/builder.py

"""
Module: integrity.build.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from catalog.persona import Persona, PersonaService
from system import Builder, BuildResult, LoggingLevelRouter, id_emitter
from logic.rank import (
    Bishop, King, Knight, Pawn, Queen, Rank, RankBuildException, RankBuildRouteException,
    RankFactoryException, Rook
)

class RankFactory(Builder[Rank]):
    """
    Role:Factory, Data Integrity Guarantor
  
    Responsibilities:
    1.  Produce Rank instances whose integrity is guaranteed at creation.
    2.  Manage construction of Rank instances that can be used safely by the client.
    3.  Ensure params for Rank creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.
        
    Super Class:
        *   Builder

    # PROVIDES:
        *   RankFactory
  
    
    # INHERITED ATTRIBUTES:
    None
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
            RankBuildException
            RankFactoryException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the persona does not pass a validation check.
        validation_result = persona_service.validator.validate(candidate=persona)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                RankFactoryException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankFactoryException.MSG,
                    err_code=RankFactoryException.ERR_CODE,
                    ex=RankBuildException(
                        mthd=method,
                        op=RankBuildException.OP,
                        msg=RankBuildException.MSG,
                        err_code=RankBuildException.ERR_CODE,
                        rslt_type=RankBuildException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
            )
        # --- Route to the appropriate concrete integrity.build. ---#
        
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
                ex=RankBuildException(
                    mthd=method,
                    op=RankBuildException.OP,
                    msg=RankBuildException.MSG,
                    err_code=RankBuildException.ERR_CODE,
                    rslt_type=RankBuildException.RSLT_TYPE,
                    ex=RankBuildRouteException(
                        var="persona",
                        val=f"{persona}",
                        msg=RankBuildRouteException.MSG,
                        err_code=RankBuildRouteException.ERR_CODE,
                    )
                )
            )
        )
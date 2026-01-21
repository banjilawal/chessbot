# src/chess/rank/factory/factory.py

"""
Module: chess.rank.factory.factory
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""

from chess.persona import Persona, PersonaService
from chess.system import Builder, BuildResult, LoggingLevelRouter, id_emitter
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rank, RankBuildFailedException, RankBuildRouteException, Rook

class RankFactory(Builder[Rank]):
    """
    # ROLE: Factory, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
    1.  Produce Rank instances whose integrity is guaranteed at creation.
    2.  Manage construction of Rank instances that can be used safely by the client.
    3.  Ensure params for Rank creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.
        
    # PARENT:
        *   Builder

    # PROVIDES:
        *   RankFactory
  
    # LOCAL ATTRIBUTES:
    None
    
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
        # ACTION:
        Given a Persona, return an appropriate Rank object.

        # PARAMETERS:
            * persona (Persona)

        # RETURNS:
          BuildResult[Rank] containing either:
                - On success: a concrete Rank in the payload.
                - On failure: Exception.

        # RAISES:
            * RankBuildFailedException
        """
        method = "RankFactory.builder"
        # Handle the case that the persona is not certifed as safe.
        validation = persona_service.validator.validate(candidate=persona)
        if validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                RankBuildFailedException(
                    message=f"{method}: {RankBuildFailedException.DEFAULT_MESSAGE}",
                    ex=validation.exception
                )
            )
        # --- Route to the appropriate concrete builder. ---#
        
        # Entry point into building a King instance.
        if persona == Persona.KING:
            return cls._build_king_rank(id=id)
        # Entry point into building a Pawn instance.
        if persona == Persona.PAWN:
            return cls._build_pawn_rank(id=id)
        # Entry point into building a Knight instance.
        if persona == Persona.KNIGHT:
            return cls._build_knight_rank(id=id)
        # Entry point into building a Bishop instance.
        if persona == Persona.BISHOP:
            return cls._build_bishop_rank(id=id)
        # Entry point into building a Rook instance.
        if persona == Persona.ROOK:
            return cls._build_rook_rank(id=id)
        # Entry point into building a Queen instance.
        if persona == Persona.QUEEN:
            return cls._build_queen_rank(id=id)
            
        # Return the exception chain if there is no build route for the context.
        return BuildResult.failure(
            RankBuildFailedException(
                message=f"{method}: {RankBuildFailedException.DEFAULT_MESSAGE}",
                ex=RankBuildRouteException(f"{method}: {RankBuildRouteException.DEFAULT_MESSAGE}")
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_king_rank(cls, id: int) -> BuildResult[King]:
        method = "RankFactory.build_king_rank"
        return BuildResult.success(
            King(
                id=id,
                name=Persona.KING.name,
                ransom=Persona.KING.ransom,
                team_quota=Persona.KING.quota,
                quadrants=Persona.KING.quadrants,
                designation=Persona.KING.designation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_pawn_rank(cls, id: int) -> BuildResult[Pawn]:
        """
        # ACTION:
        Returns a BuildResult containing a Pawn instance.

        # PARAMETERS:
        None

        # RETURNS:
          BuildResult[Pawn] containing either:
                - On success: a Pawn in the payload.
                - On failure: Exception.

        # RAISES:
        None
        """
        method = "RankFactory.build_pawn_rank"
        return BuildResult.success(
            Pawn(
                id=id_emitter.pawn_id,
                name=Persona.PAWN.name,
                ransom=Persona.PAWN.ransom,
                team_quota=Persona.PAWN.quota,
                quadrants=Persona.PAWN.quadrants,
                designation=Persona.PAWN.designation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_knight_rank(cls, id: int) -> BuildResult[Knight]:
        return BuildResult.success(
            Knight(
                id=id_emitter.knight_id,
                name=Persona.KNIGHT.name,
                ransom=Persona.KNIGHT.ransom,
                team_quota=Persona.KNIGHT.quota,
                quadrants=Persona.KNIGHT.quadrants,
                designation=Persona.KNIGHT.designation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_bishop_rank(cls, id: int) -> BuildResult[Bishop]:
        return BuildResult.success(
            Bishop(
                id=id_emitter.bishop_id,
                name=Persona.BISHOP.name,
                ransom=Persona.BISHOP.ransom,
                team_quota=Persona.BISHOP.quota,
                quadrants=Persona.BISHOP.quadrants,
                designation=Persona.BISHOP.designation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_rook_rank(cls, id: int) -> BuildResult[Rook]:
        return BuildResult.success(
            Rook(
                id=id_emitter.rook_id,
                name=Persona.ROOK.name,
                ransom=Persona.ROOK.ransom,
                team_quota=Persona.ROOK.quota,
                quadrants=Persona.ROOK.quadrants,
                designation=Persona.ROOK.designation,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_queen_rank(cls, id: int) -> BuildResult[Queen]:
        return BuildResult.success(
            Queen(
                id=id_emitter.queen_id,
                name=Persona.QUEEN.name,
                ransom=Persona.QUEEN.ransom,
                team_quota=Persona.QUEEN.quota,
                quadrants=Persona.QUEEN.quadrants,
                designation=Persona.QUEEN.designation,
            )
        )
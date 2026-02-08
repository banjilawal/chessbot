# src/chess/token/factory/factory.py

"""
Module: chess.token.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from __future__ import annotations

from chess.persona import Persona
from chess.team import Team, TeamService
from chess.rank import RankService
from chess.formation import Formation, FormationService
from chess.system import BuildResult, Builder, IdentityService, LoggingLevelRouter, id_emitter
from chess.token import CombatantToken, KingToken, PawnToken, TokenBuildFailedException, Token

class TokenFactory(Builder[Token]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Token instances whose integrity is guaranteed at creation.
    2.  Manage construction of Token instances that can be used safely by the client.
    3.  Ensure params for Token creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            owner: Team,
            formation: Formation,
            id: int = id_emitter.piece_id,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
    ) -> BuildResult[Token]:
        """
        # ACTION:
            1.  If any build param fails its certification tests send the exception in the BuildResult. Else,
                route to the appropriate concrete Token builder method.
        # PARAMETERS:
            *   id (int)
            *   owner (Team)
            *   formation: (Formation)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   identity_service (IdentityService)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[Token] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenBuildFailedException
        """
        method = "TokenFactory.builder"
        
        # Handle the case that the id is not certified as safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that the team is not certified as safe.
        owner_validation = team_service.validator.validate(candidate=owner)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=owner_validation.exception
                )
            )
        # Handle the case that the formation is not certified as safe.
        formation_validation = formation_service.validator.validate(candidate=formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=formation_validation.exception
                )
            )
        # --- Route to the appropriate concrete Token builder method. ---#
        
        if formation.persona == Persona.PAWN:
        # Build path for Pawns.
            return cls._build_pawn(
                id=id,
                owner=owner,
                designation=formation.designation,
                roster_number=formation.roster_number,
                opening_square_name=formation.square_name,
            )
        # Build path for Kings
        if formation.persona == Persona.KING:
            return cls._build_king(
                id=id,
                owner=owner,
                designation=formation.designation,
                roster_number=formation.roster_number,
                Opening_square_name=formation.square_name,
            )
        # The default path builds Combatants
        return cls._build_combatant(
            id=id,
            owner=owner,
            formation=formation,
            rank_service=rank_service,
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_pawn(
            cls,
            id: int,
            owner: Team,
            designation: str,
            roster_number: int,
            opening_square_name: str,
    ) -> BuildResult[PawnToken]:
        """
        # ACTION:
            1.  Use the params to build the PawnToken then return to caller in the
        # PARAMETERS:
            *   id (int)
            *   owner (Team)
            *   formation: (Formation)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   identity_service (IdentityService)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[PawnToken]

        # RAISES:
            *   None
        """
        method = "TokenFactory._build_pawn"
        
        return BuildResult.success(
            payload=PawnToken(
                id=id,
                team=owner,
                designation=designation,
                roster_number=roster_number,
                opening_square_name=opening_square_name,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_king(
            cls,
            id: int,
            owner: Team,
            designation: str,
            roster_number: int,
            Opening_square_name: str
    ) -> BuildResult[KingToken]:
        """
        # ACTION:
            1.  Build KingToken and return to the caller.
        # PARAMETERS:
            *   id (int)
            *   owner (Team)
            *   formation: (Formation)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   identity_service (IdentityService)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[PawnToken]
        # RAISES:
            *   None
        """
        method = "TokenFactory._build_king"
        
        return BuildResult.success(
                payload=KingToken(
                id=id,
                team=owner,
                designation=designation,
                roster_number=roster_number,
                opening_square_name=Opening_square_name,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_combatant(
            cls,
            id: int,
            owner: Team,
            formation: Formation, str,
            rank_service: RankService,
    ) -> BuildResult[KingToken]:
        """
        # ACTION:
            1.  Use the formation's Persona property to build the combatant's rank. If the rank build fails
                send an exception chain the BuildResult.
        # PARAMETERS:
            *   id (int)
            *   owner (Team)
            *   formation (Formation)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[CombatantToken]
        # RAISES:
            *   None
        """
        method = "TokenFactory._build_combatant"
        
        # Handle the case that the rank build is not completed.
        rank_build_result = rank_service.builder.build(persona=formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=rank_build_result.exception
                )
            )
        # Return the combatant's build result to the caller
        return BuildResult.success(
            payload=CombatantToken(
                id=id,
                team=owner,
                rank=rank_build_result.payload,
                designation=formation.designation,
                roster_number=formation.roster_number,
                opening_square_name=formation.square_name,
            )
        )
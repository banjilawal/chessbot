# src/logic/token/service/operation/build/exception.py

"""
Module: logic.token.service.operation.build.build
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from __future__ import annotations

from logic.persona import Persona
from logic.team import Team, TeamValidationProcess
from logic.rank import RankService
from logic.formation import Formation, FormationService
from logic.system import BuildResult, BuildProcess, IdFactory, IdentityService, LoggingLevelRouter
from logic.token import CombatantToken, KingToken, PawnToken, TokenBuildException, Token

class TokenBuild(BuildProcess[Token]):
    """
     Role:
        -   Worker, 
        -   Integrity Management

     Responsibilities:
         1.  Produce Token instances whose integrity is guaranteed at creation.
         2.  Ensure params for Token creation have met the application's safety contract.
         3.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidationProcess,
            ) -> BuildResult[Token]

     Super Class:
         BuildProcess
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            owner: Team,
            formation: Formation,
            rank_service: RankService = RankService(),
            id: int = IdFactory.next_id(class_name="Token"),
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
            team_validator: TeamValidationProcess = TeamValidationProcess(),
    ) -> BuildResult[Token]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if, either
                    -   id
                    -   name
                    -   team
                    -   formation
                fail their validation checks.
            2.  Otherwise, build the token then, send the success result.
        Args:
            id: int
            owner: Team
            formation: Formation
            rank_service: RankService
            identity_service: IdentityService
            formation_service: FormationService
            team_validator: TeamValidationProcess
        Returns:
            BuildResult[Token]
        Raises:
            *   TokenBuildException
        """
        method = f"{cls.__name__}.execute"
        

        # Handle the case that, a build param is not safe.
        param_validation_results = cls._run_build_param_checks(
            id=id,
            owner=owner,
            formation=formation,
            identity_service=identity_service,
            formation_service=formation_service,
            team_validator=team_validator,
        )
        if param_validation_results.is_failure:
            return param_validation_results
        # --- Route to the appropriate concrete Token build method. ---#
        
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
    def _run_build_param_checks(
            cls,
            id: int,
            owner: Team,
            formation: Formation,
            team_validator: TeamValidationProcess,
            identity_service: IdentityService = IdentityService(),
            formation_service: FormationService = FormationService(),
    ):
        method = f"{cls.__name__}._run_build_param_checks"
        
        # Handle the case that, the id is not certified as safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenBuildException.OP,
                    msg=TokenBuildException.MSG,
                    err_code=TokenBuildException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that, the team is not certified as safe.
        owner_validation = team_validator.execute(candidate=owner)
        if owner_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenBuildException.OP,
                    msg=TokenBuildException.MSG,
                    err_code=TokenBuildException.ERR_CODE,
                    ex=owner_validation.exception,
                )
            )
        # Handle the case that, the formation is not certified as safe.
        formation_validation = formation_service.validator.execute(candidate=formation)
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildException(
                    mthd=method,
                    title=cls.__name__,
                    op=TokenBuildException.OP,
                    msg=TokenBuildException.MSG,
                    err_code=TokenBuildException.ERR_CODE,
                    ex=formation_validation.exception,
                )
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
            *   team_validator (TeamValidationProcess)
            *   identity_service (IdentityService)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[PawnToken]

        Raises:
            *   None
        """
        method = "TokenBuild._build_pawn"
        
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
            *   team_validator (TeamValidationProcess)
            *   identity_service (IdentityService)
            *   formation_service: (FormationService)
        # RETURNS:
            *   BuildResult[PawnToken]
        Raises:
            *   None
        """
        method = "TokenBuild._build_king"
        
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
        Raises:
            *   None
        """
        method = "TokenBuild._build_combatant"
        
        # Handle the case that, the rank build is not completed.
        rank_build_result = rank_service.build.execute(persona=formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildException(
                    msg=f"{method}: {TokenBuildException.ERR_CODE}",
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
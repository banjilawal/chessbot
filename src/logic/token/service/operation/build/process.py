# src/logic/token/service/operation/build/exception.py

"""
Module: logic.token.service.operation.build.build
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from __future__ import annotations

from logic.persona import Persona
from logic.rank import RankService
from logic.team import Team, TeamValidationProcess
from logic.formation import Formation, FormationService
from logic.token import CombatantToken, KingToken, PawnToken, TokenBuildException, Token
from logic.system import BuildResult, BuildProcess, IdFactory, IdentityService, LoggingLevelRouter


class TokenBuild(BuildProcess[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner
        
   Responsibilities:
        1.  Token creation process owner.
        2.  Ensure Token build resources meet satisfy contracts.
        3.  Assure tokens  comply with business logic at point of creation.
        4.  Execute 1:M binding logic a token has with its owning entities..

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
            TokenBuildException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the id does not pass a validation check.
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
        # Handle the case that, the team does not pass a validation check.
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
        # Handle the case that, the formation does not pass a validation check.
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
        # --- Param checks are passed, Handoff creation to _create_concrete_token. ---#
        
        creation_result = cls._create_concrete_token(
            id=id,
            owner=owner,
            formation=formation,
            rank_service=rank_service
        )
        # Handle the case that, the creation was not successful.
        if creation_result.is_failure:
            return creation_result
        # --- Handoff binding to binding and finalization tasks. ---#
        binding_result = cls._create_bindings(token=creation_result.payload)
        
        # For legibility, handle the case that binding is not successful.
        if binding_result.is_failure:
            return binding_result
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(binding_result.payload)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _create_concrete_token(
            cls,
            id: int,
            owner: Team,
            formation: Formation,
            rank_service: RankService
    ) -> BuildResult[Token]:
        """
        Create a concrete token.
        
        Action:
            1.  If the formation's rank is not a king or pawn and its Rank instance is not
                build successfully send an exception chain in the BuildResult.
            2.  Otherwise, build the token then, send the success result.
        Args:
            id: int
            owner: Team
            formation: Formation
            rank_service: RankService
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuildException
        """
        method = "TokenBuild._build_pawn"
        
        # Build path for pawns.
        if formation.persona == Persona.PAWN:
            return BuildResult.success(
                PawnToken(
                    id=id,
                    team=owner,
                    designation=formation.designation,
                    roster_number=formation.roster_number,
                    opening_square_name=formation.square_name,
                )
            )
        # Build path for kings.
        if formation.persona == Persona.KING:
            return BuildResult.success(
                KingToken(
                    id=id,
                    team=owner,
                    designation=formation.designation,
                    roster_number=formation.roster_number,
                    opening_square_name=formation.square_name,
                )
            )
        # --- All other ranks run the CombatantToken build steps. ---#
        
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = rank_service.build.execute(persona=formation.persona)
        if rank_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildException(
                    msg=f"{method}: {TokenBuildException.ERR_CODE}",
                    ex=rank_build_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _create_bindings(cls, token: Token):
        """
        Binda token to its team with an insert.
        
        Action:
            1.  If the token cannot be inserted into the team roster send an exception chain
                in the BuildResult.
            2.  Otherwise, send the success result.
        Args:
            token: Token
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuildException
        """
        method = f"{cls.__name__}._create_bindings"
        
        team = token.team
        if token not in team.roster:
            insertion_result = team.roster.insert(item=token)
            # Handle the case that, the token is not successfully registered with its team.
            if insertion_result.is_failure:
                return BuildResult.failure(
                    TokenBuildException(
                        mthd=method,
                        title=cls.__name__,
                        op=TokenBuildException.OP,
                        msg=TokenBuildException.MSG,
                        err_code=TokenBuildException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(token)
        
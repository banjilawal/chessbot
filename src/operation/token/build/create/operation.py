# src/integrity/build/token/builder.py

"""
Module: integrity.build.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict

from model.catalog import Formation, Persona
from err import TokenBuildException
from microservice import RankService
from model import CombatantToken, KingToken, PawnToken, Team, Token
from result import BuildResult
from system import LoggingLevelRouter


class TokenCreationOperation:
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
            param_dict: Dict[str, Any],
    ) -> BuildResult[Token]:

        method = f"{cls.__name__}.execute"
        
        creation_result = cls._create_concrete_token(
            id=param_dict["id"],
            owner=param_dict["owner"],
            formation=param_dict["formation"],
            rank=param_dict["rank"],
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
        method = "TokenBuilder._build_pawn"
        
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
        rank_build_result = rank_service.builder.build(persona=formation.persona)
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
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenBuildException.OP,
                        msg=TokenBuildException.MSG,
                        err_code=TokenBuildException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(token)
        
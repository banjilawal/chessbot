# src/builder/token/builder.py

"""
Module: builder.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model.catalog import Formation, Persona
from err import TokenBuilderException
from integrity import Builder
from microservice import RankService
from model import CombatantToken, KingToken, PawnToken, Team, Token
from result import BuildResult
from system import IdFactory, LoggingLevelRouter
from toolkit.integrity.token.toolkit import TokenIntegrityToolkit


class TokenBuilder(Builder[Token]):
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
            owner: Team,
            formation: Formation,
            id: int = None,
            toolkit: TokenIntegrityToolkit = None,
    ) -> BuildResult[Token]:
        """
        Build a safe Token.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur:
                    -   Either id, schema, team. formation fail a validation check.
                    -   The token belongs on a different team.
                    -   The team has already filled the position.
                    -   The token's rank cannot be built.
                    -   The token cannot register with its team.
            2.  Otherwise, build the token then, send the success result.
        Args:
            id: int
            owner: Team
            formation: Formation
            toolkit: TokenIntegrityToolkit
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{cls.__name__}.execute"
        
        if id is None:
            id = IdFactory.next_id(class_name="Token")
        if toolkit is None:
            toolkit = TokenIntegrityToolkit()
        
        # Handle the case that, the id does not pass a validation check.
        id_validation = toolkit.identity_service.validate_id(id)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        owner_validation = toolkit.team_service.validator.build(owner)
        if owner_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=owner_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.build(formation)
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- Param checks are passed, Handoff creation to _create_concrete_token. ---#
        
        creation_result = cls._create_concrete_token(
            id=id,
            owner=owner,
            formation=formation,
            rank_service=toolkit.rank_service
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
            TokenBuilderException
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
                    opening_square_name=formation.opening_square_name,
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
                    opening_square_name=formation.opening_square_name,
                )
            )
        # --- All other ranks run the CombatantToken build steps. ---#
        
        # Handle the case that its Rank instance request is not satisfied.
        rank_build_result = rank_service.builder.build(persona=formation.persona)
        if rank_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    msg=f"{method}: {TokenBuilderException.ERR_CODE}",
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
                opening_square_name=formation.opening_square_name,
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
            TokenBuilderException
        """
        method = f"{cls.__name__}._create_bindings"
        
        team = token.team
        if token not in team.roster:
            insertion_result = team.roster.insert(item=token)
            # Handle the case that, the token is not successfully registered with its team.
            if insertion_result.is_failure:
                return BuildResult.failure(
                    TokenBuilderException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=TokenBuilderException.OP,
                        msg=TokenBuilderException.MSG,
                        err_code=TokenBuilderException.ERR_CODE,
                        ex=insertion_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(token)
        
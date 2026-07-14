# src/consistency/token/consistency/consistency.py

"""
Module: consistency.token.consistency.consistency
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from factory import ToolkitFactory
from model import Token
from toolkit import TokenToolkit
from database import CoordDatabase
from result import BuildResult, ValidationResult
from util import LoggingLevelRouter
from consistency import  ConsistencyChecker
from controller import WorkerRegistryController
from err import CoordDatabaseNullException, TokenNullException, TokenConsistencyCheckerException


class TokenConsistencyConsistencyChecker(ConsistencyChecker[Token]):
    """
    Role
        -   Transaction Worker
        -   Consistency Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any, toolkit: TokenToolkit) -> ValidationResult[Token]:

    Super Class:
        Consistency
    """
    OPERATION_NAME = "token_consistency"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token
    ) -> ValidationResult[Token]:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a number.
                    _   A Team check fails
                    -   A Rank check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            token: Token
        Returns:
            ValidationResult[Token]
        Raises:
             TokenConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        team = token.team
        board = team.board
        
        token_search_result =
        
        toolkit_build_result = cls._get_toolkit(toolkit=toolkit)
        if toolkit_build_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=toolkit_build_result.exception,
                )
            )
        tools = toolkit_build_result.payload
        
        # Handle the case that, the consistency is not primed.
        consistency_priming_result = tools["priming_consistency"].execute(
            candidate=candidate,
            target_model=Token,
            context_null_exception=TokenNullException(),
        )
        if consistency_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=consistency_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Token for additional tests ---#
        token = cast(Token, candidate)
        
        # Handle the case that, id or designation are not certified safe.
        identity_validation_result = tools["identity_service"].validate_identity_register(
            id_candidate=token.id,
            name_candidate=token.name
        )
        if identity_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=identity_validation_result.exception,
                )
            )
        # Handle the case that, the occupant's team fails consistency.
        team_validation_result = tools["team_consistency"].execute(token.team)
        if team_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=team_validation_result.exception,
                )
            )
        # Handle the case that, the roster or home_square_name are not acceptable.
        home_square_validation_result = toolkit["square_consistency"].execute(token.home_square)
        if home_square_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=home_square_validation_result.exception,
                )
            )
        # Handle the case that, the rank is not safe.
        rank_validation_result = tools["rank_service.consistency"].execute(rank=token.rank)
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=rank_validation_result.exception,
                )
            )
        # Handle the case that the token's CoordDatabase fails it safety checks.
        coord_database_validation_result = tools["priming_consistency"].execute(
            candidate=token.positions,
            target_model=CoordDatabase,
            context_null_exception=CoordDatabaseNullException()
        )
        if coord_database_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=coord_database_validation_result,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(token)

    
    @classmethod
    def verify_token_is_combatant(cls, candidate: Any) -> ValidationResult[CombatantToken]:
        """
        Verify the token can be captured.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CombatantToken]
        Raises:
        
        """
        method = f"{cls.__class__.__name__}.validate_token_is_combatant"
        # Handle the case that, the rank is not certified as a safe occupant.
        validation_result = cls.execute(candidate)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the rank is not a CombatantToken.
        if not isinstance(candidate, CombatantToken):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=TypeError(f"Expected CombatantToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the candidate into CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))
        
    @classmethod
    def verify_token_is_king(cls, candidate: Any) -> ValidationResult[KingToken]:
        method = "TokenConsistencyConsistency.execute_token_is_king"
        # Handle the case that, the rank is not certified as a safe occupant.
        validation = cls.execute(candidate)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=consistency.exception
                )
            )
        # Handle the case that, the rank is not a KingToken.
        if not isinstance(candidate, KingToken):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=TypeError(f"{method}:Expected KingToken, got {type(candidate).__name__} instead.")
                )
            )
        # Tests have been passed return cast the candidate into CombatantToken and return to the caller.
        return ValidationResult.success(payload=cast(CombatantToken, candidate))
    
    @classmethod
    def verify_actionable_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_actionable_token"
        # Handle the case that, the occupantis not safe.
        token_validation = cls.execute(candidate=token)
        if token_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=token_consistency.exception
                )
            )
        # Handle the case that, the occupant has not been placed.
        if token.is_disabled:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=DisabledTokenCannotExploreException(
                        f"{method}: {DisabledTokenCannotExploreException.MSG}"
                    )
                )
            )
        # The occupant is actionable.
        return ValidationResult.success(token)
    
    @classmethod
    def verify_disabled_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_disabled_token"
        # Handle the case that, the occupantis not safe.
        token_validation = cls.execute(candidate=token)
        if token_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=token_consistency.exception
                )
            )
        # Handle the case that, the occupant has not been placed.
        if token.is_active:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=TokenException(
                        f"{method}: {DisabledTokenCannotExploreException.MSG}"
                    )
                )
            )
        # The occupant is disabled
        return ValidationResult.success(token)
    
    @classmethod
    def verify_capture_activated_token(cls, token: Token) -> ValidationResult[Token]:
        method = "TokenService.verify_capture_activated_token"
        # Handle the case that, the occupant is enable.
        token_validation = cls.verify_disabled_token(token)
        if token.is_active:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=token_consistency.exception
                )
            )
        # Handle the case that, the token is a King.
        if isinstance(token, KingToken):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    msg=f"{method}: {TokenConsistencyCheckerException.MSG}",
                    ex=TokenException()
                )
            )
        # The occupant is disabled
        return ValidationResult.success(token)
    
    @classmethod
    def _get_toolkit(cls, toolkit: TokenToolkit) -> BuildResult[TokenToolkit]:
        method = f"{self.__class__.__name__}._get_toolkit"
        
        build_result = ToolkitFactory.build_toolkit(toolkit_class=TokenToolkit, )
        if build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=build_result.exception,
                )
            )
        return BuildResult.success(build_result.payload)

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=TokenConsistencyConsistency)